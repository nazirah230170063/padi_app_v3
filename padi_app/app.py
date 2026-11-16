import os, json, sqlite3, secrets, uuid
from functools import wraps
import numpy as np
from PIL import Image
from flask import Flask, g, render_template, request, redirect, url_for, session, flash, abort
from werkzeug.security import generate_password_hash, check_password_hash

BASE = os.path.dirname(os.path.abspath(__file__))
MODEL_FILE = os.path.join(BASE, 'mobilenetv2_padi_terbaik.keras')
KELAS = [l.strip() for l in open(os.path.join(BASE, 'labels.txt'), encoding='utf-8') if l.strip()]
PREPROC = 'mobilenet'      # 'mobilenet' (-1..1) atau 'rescale' (0..1) -> samakan dengan saat training
UP = os.path.join(BASE, 'static', 'uploads')
DB = os.path.join(BASE, 'padi.db')

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024
kf = os.path.join(BASE, 'secret.key')
if not os.path.exists(kf): open(kf, 'w').write(secrets.token_hex(32))
app.secret_key = open(kf).read()
app.jinja_env.globals['token'] = lambda: session.setdefault('t', secrets.token_hex(16))
app.jinja_env.globals['KELAS'] = KELAS
FOTO = os.path.join(BASE, 'static', 'foto'); os.makedirs(FOTO, exist_ok=True)
def _foto(n):
    b = os.path.splitext(n)[0]
    for e in ('.jpg', '.jpeg', '.png', '.webp', '.JPG', '.JPEG', '.PNG'):
        if os.path.isfile(os.path.join(FOTO, b + e)): return url_for('static', filename='foto/' + b + e)
    return None
app.jinja_env.globals['foto_url'] = _foto

from content import PAGES

def db():
    if 'db' not in g:
        g.db = sqlite3.connect(DB); g.db.row_factory = sqlite3.Row; g.db.execute('PRAGMA foreign_keys=ON')
    return g.db
@app.teardown_appcontext
def _close(e):
    d = g.pop('db', None)
    if d: d.close()
def q(sql, a=(), one=False):
    r = db().execute(sql, a).fetchall(); return (r[0] if r else None) if one else r
def ex(sql, a=()):
    c = db().execute(sql, a); db().commit(); return c.lastrowid
def init_db():
    c = sqlite3.connect(DB)
    c.executescript("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,nama TEXT NOT NULL,email TEXT UNIQUE NOT NULL,password TEXT NOT NULL,role TEXT NOT NULL DEFAULT 'user',created_at TEXT DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS prediksi(id INTEGER PRIMARY KEY AUTOINCREMENT,user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,gambar TEXT NOT NULL,label TEXT NOT NULL,confidence REAL NOT NULL,probs TEXT NOT NULL,created_at TEXT DEFAULT CURRENT_TIMESTAMP);""")
    c.commit(); c.close()

@app.before_request
def _gate():
    if request.endpoint not in ('login', 'register', 'static') and not session.get('u'): return redirect(url_for('login'))
@app.before_request
def _csrf():
    if request.method == 'POST' and request.form.get('t') != session.get('t'): abort(400)
@app.context_processor
def _ctx(): return {'user': session.get('u')}

def need(admin=False):
    def deco(f):
        @wraps(f)
        def w(*a, **k):
            u = session.get('u')
            if not u: return redirect(url_for('login'))
            if admin and u['role'] != 'admin': abort(403)
            return f(*a, **k)
        return w
    return deco

_model = None
def model():
    global _model
    if _model is None:
        import keras
        _model = keras.models.load_model(MODEL_FILE, compile=False)
    return _model
def predict(im):
    x = np.asarray(im.convert('RGB').resize((224, 224)), dtype='float32')
    x = x / 127.5 - 1 if PREPROC == 'mobilenet' else x / 255.0
    return [float(v) for v in model()(x[None], training=False).numpy()[0]]

def get_pred(i):
    r = q('SELECT p.*,u.nama FROM prediksi p JOIN users u ON u.id=p.user_id WHERE p.id=?', (i,), True)
    if not r or (r['user_id'] != session['u']['id'] and session['u']['role'] != 'admin'): abort(404)
    return r
def rm_img(name):
    try: os.remove(os.path.join(UP, name))
    except OSError: pass

@app.route('/')
def index():
    n = q('SELECT COUNT(*) c FROM prediksi WHERE user_id=?', (session['u']['id'],), True)['c']
    return render_template('index.html', title='Beranda', n=n)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        n, m, p = request.form['nama'].strip(), request.form['email'].strip().lower(), request.form['password']
        if not n or '@' not in m or len(p) < 6: flash('Isi nama, email valid, dan password minimal 6 karakter.')
        elif q('SELECT 1 FROM users WHERE email=?', (m,), True): flash('Email sudah terdaftar.')
        else:
            role = 'admin' if q('SELECT COUNT(*) c FROM users', one=True)['c'] == 0 else 'user'   # akun pertama = admin
            i = ex('INSERT INTO users(nama,email,password,role) VALUES(?,?,?,?)', (n, m, generate_password_hash(p), role))
            session['u'] = {'id': i, 'nama': n, 'role': role}; return redirect(url_for('index'))
    return render_template('register.html', title='Register')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        r = q('SELECT * FROM users WHERE email=?', (request.form['email'].strip().lower(),), True)
        if r and check_password_hash(r['password'], request.form['password']):
            session['u'] = {'id': r['id'], 'nama': r['nama'], 'role': r['role']}; return redirect(url_for('index'))
        flash('Email atau password salah.')
    return render_template('login.html', title='Login')

@app.route('/logout')
def logout(): session.clear(); return redirect(url_for('index'))

@app.route('/dashboard')
@need()
def dashboard():
    u = session['u']['id']
    return render_template('dashboard.html', title='Dashboard',
        stat=q('SELECT label,COUNT(*) c FROM prediksi WHERE user_id=? GROUP BY label', (u,)),
        last=q('SELECT * FROM prediksi WHERE user_id=? ORDER BY id DESC LIMIT 5', (u,)))

@app.route('/klasifikasi', methods=['GET', 'POST'])
@need()
def klasifikasi():
    if request.method == 'POST':
        f = request.files.get('foto')
        try: im = Image.open(f.stream).convert('RGB')
        except Exception: flash('File bukan gambar yang valid.'); return redirect(url_for('klasifikasi'))
        try:
            p = predict(im)
            if len(p) != len(KELAS): raise ValueError(f'Model punya {len(p)} kelas, labels.txt berisi {len(KELAS)} baris.')
        except Exception as e:
            flash('Gagal memprediksi: ' + str(e)); return redirect(url_for('klasifikasi'))
        im.thumbnail((800, 800)); nm = uuid.uuid4().hex + '.jpg'; im.save(os.path.join(UP, nm), quality=88)
        i = p.index(max(p))
        pid = ex('INSERT INTO prediksi(user_id,gambar,label,confidence,probs) VALUES(?,?,?,?,?)',
                 (session['u']['id'], nm, KELAS[i], p[i], json.dumps(p)))
        return redirect(url_for('hasil', i=pid))
    return render_template('klasifikasi.html', title='Klasifikasi Citra')

@app.route('/hasil/<int:i>')
@need()
def hasil(i):
    r = get_pred(i); return render_template('hasil.html', title='Hasil Prediksi', r=r, ok='sehat' in r['label'].lower())

@app.route('/riwayat')
@need()
def riwayat():
    return render_template('riwayat.html', title='Riwayat Prediksi', rows=q('SELECT * FROM prediksi WHERE user_id=? ORDER BY id DESC', (session['u']['id'],)))

@app.route('/detail/<int:i>', methods=['GET', 'POST'])
@need()
def detail(i):
    r = get_pred(i)
    if request.method == 'POST':
        rm_img(r['gambar']); ex('DELETE FROM prediksi WHERE id=?', (i,)); return redirect(url_for('riwayat'))
    return render_template('detail.html', title='Detail Prediksi', r=r, probs=json.loads(r['probs']))

def _info(k):
    return render_template('info.html', title=PAGES[k]['title'], p=PAGES[k])
for _k in PAGES: app.add_url_rule('/' + _k, 'info_' + _k.replace('-', '_'), (lambda k=_k: _info(k)))

@app.route('/profil', methods=['GET', 'POST'])
@need()
def profil():
    u = session['u']['id']
    if request.method == 'POST':
        n = request.form['nama'].strip()
        if n: ex('UPDATE users SET nama=? WHERE id=?', (n, u)); session['u'] = {**session['u'], 'nama': n}; flash('Profil diperbarui.')
        pw = request.form['password']
        if pw:
            if len(pw) < 6: flash('Password minimal 6 karakter.')
            else: ex('UPDATE users SET password=? WHERE id=?', (generate_password_hash(pw), u)); flash('Password diubah.')
    return render_template('profil.html', title='Profil', me=q('SELECT * FROM users WHERE id=?', (u,), True))

@app.route('/admin')
@need(True)
def admin():
    return render_template('admin.html', title='Admin Dashboard', n=q('SELECT COUNT(*) c FROM users', one=True)['c'],
        stat=q('SELECT label,COUNT(*) c FROM prediksi GROUP BY label'))

@app.route('/admin/pengguna', methods=['GET', 'POST'])
@need(True)
def admin_pengguna():
    if request.method == 'POST':
        i = int(request.form['id'])
        if i != session['u']['id']:
            if request.form['a'] == 'del':
                for g_ in q('SELECT gambar FROM prediksi WHERE user_id=?', (i,)): rm_img(g_['gambar'])
                ex('DELETE FROM users WHERE id=?', (i,))
            else: ex("UPDATE users SET role=CASE role WHEN 'admin' THEN 'user' ELSE 'admin' END WHERE id=?", (i,))
        return redirect(url_for('admin_pengguna'))
    return render_template('admin_pengguna.html', title='Kelola Pengguna', rows=q('SELECT * FROM users ORDER BY id'))

@app.route('/admin/prediksi', methods=['GET', 'POST'])
@need(True)
def admin_prediksi():
    if request.method == 'POST':
        r = q('SELECT gambar FROM prediksi WHERE id=?', (int(request.form['id']),), True)
        if r: rm_img(r['gambar']); ex('DELETE FROM prediksi WHERE id=?', (int(request.form['id']),))
        return redirect(url_for('admin_prediksi'))
    return render_template('admin_prediksi.html', title='Kelola Data Prediksi',
        rows=q('SELECT p.*,u.nama FROM prediksi p JOIN users u ON u.id=p.user_id ORDER BY p.id DESC LIMIT 300'))

if __name__ == '__main__':
    init_db()
    print('Memuat model...'); 
    try: model(); print('Model siap.')
    except Exception as e: print('PERINGATAN: model gagal dimuat ->', e)
    print('Buka http://127.0.0.1:5000'); app.run(host='127.0.0.1', port=5000)
