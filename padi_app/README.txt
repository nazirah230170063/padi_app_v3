CARA MENJALANKAN (Windows/Mac/Linux)
1. Install Python 3.10 - 3.12 (centang "Add Python to PATH" saat install di Windows).
2. Buka terminal/CMD di folder ini, lalu:   pip install -r requirements.txt
3. Edit labels.txt: satu nama kelas per baris, URUTAN sama dengan saat training.
   (Kelas yang namanya mengandung kata "sehat" dianggap tanaman sehat.)
4. Jika training memakai rescale=1/255, ubah PREPROC = 'rescale' di app.py (bagian atas).
5. Jalankan:   python app.py      lalu buka  http://127.0.0.1:5000
6. Daftar akun pertama -> otomatis menjadi ADMIN.
Catatan: butuh internet untuk tampilan (Bootstrap CDN). Data tersimpan di padi.db & static/uploads.
