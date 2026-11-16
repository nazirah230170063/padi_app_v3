# Materi edukasi. type: cards | facts | steps | table | text. 'img' = nama file di static/foto.
def C(t, d, img=None, pts=None): return {'t': t, 'd': d, 'img': img, 'pts': pts}
PAGES = {
'info-tikus': {'title': 'Informasi Hama Tikus',
 'lead': 'Tikus sawah (Rattus argentiventer) adalah hama utama tanaman padi di Indonesia. Kenali ciri, perilaku, gejala, dan tanda keberadaannya agar bisa bertindak sebelum kerusakan meluas.',
 'sections': [
  {'h': 'Karakteristik tikus sawah', 'type': 'cards', 'cols': 2, 'items': [
    C('Bulu cokelat keabuan', 'Punggung cokelat kekuningan berbintik gelap, perut keabu-abuan hingga keperakan (asal nama argentiventer). Warna ini membuatnya menyamar di pematang dan semak.', 'tikus-bulu.jpg'),
    C('Ekor lebih pendek', 'Ekor sama atau lebih pendek dari panjang kepala dan badan, bagian atas lebih gelap dibanding bawah.', 'tikus-ekor.jpg'),
    C('Ukuran dan bentuk tubuh', 'Panjang badan dewasa sekitar 17 sampai 21 cm, telinga relatif kecil dan moncong meruncing. Pandai menggali, memanjat, dan berenang.', 'tikus-sawah.jpg'),
    C('Aktif malam hari', 'Siang hari bersembunyi di lubang pada pematang, tanggul, atau semak. Malam hari keluar mencari makan di rumpun padi.', 'tikus-habitat.jpg')]},
  {'h': 'Berkembang biak sangat cepat', 'type': 'facts', 'intro': 'Inilah sebabnya populasi bisa meledak dalam satu musim tanam jika tidak dikendalikan sejak awal.', 'items': [
    {'v': 'Sekitar 3 minggu', 'd': 'masa bunting induk'}, {'v': 'Beberapa - belasan', 'd': 'anak dalam sekali lahir'},
    {'v': 'Sekitar 1 bulan+', 'd': 'anak mencapai dewasa kelamin'}, {'v': 'Fase bunting', 'd': 'puncak perkembangbiakan'}]},
  {'h': 'Gejala serangan pada tanaman', 'type': 'cards', 'cols': 2, 'items': [
    C('Batang terpotong miring', 'Batang terpotong rata dan bersih dengan sudut sekitar 45 derajat, ciri paling khas serangan tikus.', 'gejala-batang.jpg'),
    C('Rumpun rebah dan anakan hilang', 'Rumpun tampak jarang, rebah, atau anakan hilang sehingga petak terlihat berlubang.', 'gejala-rumpun.jpg'),
    C('Malai terpotong, bulir dimakan', 'Pada fase berbunga hingga pemasakan, malai dipotong dan bulir dimakan.', 'gejala-malai.jpg'),
    C('Pola dari tepi petak', 'Kerusakan biasanya dimulai dari tepi dekat pematang atau semak, lalu menjalar ke tengah.', 'gejala-pola.jpg')],
   'note': 'Gejala inilah yang dipelajari model CNN pada foto: rumpun terpotong, rebah, dan kerapatan tanaman yang berkurang.'},
  {'h': 'Fase rawan: bunting hingga pengisian malai', 'type': 'cards', 'cols': 3, 'intro': 'Kerusakan pada fase generatif tidak dapat dipulihkan karena tanaman tidak sempat membentuk anakan atau malai baru.', 'items': [
    C('Fase bunting', 'Batang bunting dipotong sehingga malai tidak sempat keluar.', 'fase-bunting.jpg'),
    C('Pengisian malai', 'Bulir yang sedang terisi dimakan atau malai dipotong.', 'fase-pengisian.jpg'),
    C('Kerusakan generatif', 'Hasil panen hilang langsung dan tidak dapat dipulihkan.', 'kerusakan-generatif.jpg')]},
  {'h': 'Fase tanam dan akibat serangan', 'type': 'table', 'head': ['Fase', 'Perkiraan umur', 'Bentuk serangan', 'Peluang pulih'], 'rows': [
    ['Persemaian', '0-21 hari', 'Bibit dicabut atau dimakan', 'Bisa disemai ulang'],
    ['Vegetatif', 'sampai sekitar 45 HST', 'Batang dan anakan dipotong', 'Sebagian pulih lewat anakan baru'],
    ['Bunting', 'sekitar 45-65 HST', 'Batang bunting dipotong', 'Sulit pulih'],
    ['Berbunga - pemasakan', 'sekitar 65-105 HST', 'Malai dipotong, bulir dimakan', 'Tidak dapat pulih']]},
  {'h': 'Tanda keberadaan tikus di lahan', 'type': 'cards', 'cols': 2, 'items': [
    C('Lubang aktif', 'Lubang di pematang atau tanggul dengan tanah di mulut lubang tampak segar dan bersih.', 'tanda-lubang.jpg'),
    C('Kotoran', 'Butiran kecil memanjang di sekitar lubang dan jalur lintasan. Kotoran segar berwarna gelap dan lembap.', 'tanda-kotoran.jpg'),
    C('Jalur dan jejak kaki', 'Jalur sempit terinjak antara lubang dan rumpun padi, kadang dengan jejak kaki di lumpur.', 'tanda-jalur.jpg'),
    C('Bekas gigitan', 'Sisa batang dan bulir bekas gigitan di sekitar lubang.', 'tanda-gigitan.jpg')]}]},

'pencegahan': {'title': 'Pencegahan Hama',
 'lead': 'Pencegahan jauh lebih murah dan efektif daripada menangani serangan yang sudah meluas. Kuncinya pengendalian terpadu (PHT): gabungan beberapa cara yang dilakukan bersama-sama sejak sebelum tanam.',
 'sections': [
  {'h': 'Prinsip pengendalian terpadu', 'type': 'facts', 'items': [
    {'v': 'Sejak awal', 'd': 'kendalikan sebelum tanaman rusak'}, {'v': 'Serentak', 'd': 'dilakukan satu hamparan bersama'},
    {'v': 'Terpadu', 'd': 'budidaya, hayati, mekanis, kimia terakhir'}, {'v': 'Dipantau', 'd': 'keputusan berdasar kondisi lapang'}]},
  {'h': 'Lima cara pencegahan utama', 'type': 'cards', 'cols': 3, 'items': [
    C('Sanitasi habitat', 'Hilangkan tempat bersarang tikus.', 'cegah-sanitasi.jpg', ['Bersihkan pematang, tanggul, dan semak', 'Pematang kecil (kira-kira maks. 30 cm)', 'Buang sisa jerami']),
    C('Tanam serempak', 'Memperpendek masa tersedianya pakan tikus.', 'cegah-serempak.jpg', ['Selisih tanam umumnya maks. 2 minggu', 'Varietas dengan umur panen seragam', 'Beri jeda tanam (bera)']),
    C('TBS dan LTBS', 'Pagar plastik dengan bubu dan tanaman perangkap.', 'cegah-tbs.jpg', ['Tanaman perangkap ditanam 2-3 minggu lebih awal', 'Pagar plastik sekitar 60 cm', 'Periksa bubu rutin']),
    C('Burung hantu', 'Pemangsa alami yang memburu tikus tiap malam.', 'cegah-burunghantu.jpg', ['Pasang rubuhan di tiang tinggi', 'Jangan diganggu atau ditembak', 'Kurangi penggunaan racun']),
    C('Pemantauan rutin', 'Deteksi dini sebelum populasi melonjak.', 'cegah-pantau.jpg', ['Periksa minimal 2 kali seminggu', 'Hitung lubang aktif dan rumpun terpotong', 'Foto dan cek di Klasifikasi Citra'])]},
  {'h': 'Cara kerja pagar perangkap (TBS)', 'type': 'text', 'intro': 'Petak kecil padi yang ditanam lebih awal menarik tikus karena lebih dulu berbulir. Tikus yang mendekat masuk ke bubu di celah pagar. Satu unit umumnya melindungi hamparan di sekitarnya hingga belasan hektar.', 'fig': ('ltbs.svg', 'Skema tampak atas sistem pagar perangkap (tidak sesuai skala).'), 'note': 'Ukuran dan jumlah unit sebaiknya disesuaikan dengan anjuran penyuluh pertanian setempat.'},
  {'h': 'Kalender pencegahan', 'type': 'steps', 'items': [
    {'t': 'Sebelum tanam', 'd': 'Sanitasi pematang dan saluran, sepakati jadwal tanam serempak, pasang pagar perangkap dan rubuhan.'},
    {'t': 'Fase vegetatif', 'd': 'Pantau lubang aktif baru, perbaiki pematang, periksa bubu secara rutin.'},
    {'t': 'Fase bunting (paling rawan)', 'd': 'Pantau paling ketat, lakukan pengendalian serentak bila ada tanda serangan.'},
    {'t': 'Berbunga sampai pemasakan', 'd': 'Pertahankan perangkap, lindungi malai dari serangan.'},
    {'t': 'Setelah panen', 'd': 'Bersihkan sisa jerami dan bongkar sarang agar populasi tidak terbawa ke musim berikutnya.'}]}]},

'perawatan': {'title': 'Perawatan Padi',
 'lead': 'Padi yang dirawat baik tumbuh seragam, lebih tahan gangguan, dan lebih cepat pulih bila diserang. Setiap fase pertumbuhan punya kebutuhan yang berbeda.',
 'sections': [
  {'h': 'Fase pertumbuhan padi', 'type': 'text', 'fig': ('fase.svg', 'Skema fase pertumbuhan dan tingkat kerugian bila diserang tikus. HST = hari setelah tanam, umur fase hanya perkiraan.')},
  {'h': 'Perawatan menurut fase', 'type': 'cards', 'cols': 3, 'intro': 'Panduan umum. Takaran dan jadwal pupuk mengikuti rekomendasi setempat dan varietas.', 'items': [
    C('Persemaian', 'Siapkan bibit sehat dan seragam.', 'perawatan-semai.jpg', ['Air: lembap hingga genangan tipis', 'Hama: cek bibit tercabut, pasang pagar']),
    C('Vegetatif', 'Fase pembentukan anakan.', 'perawatan-vegetatif.jpg', ['Air: genangan dangkal', 'Pupuk: dasar dan susulan awal', 'Hama: cari lubang baru di pematang']),
    C('Bunting', 'Pembentukan malai di dalam batang.', 'perawatan-bunting.jpg', ['Air: genangan terjaga', 'Pupuk: sesuai bagan warna daun', 'Hama: pantau ketat, paling rawan']),
    C('Berbunga', 'Malai keluar dan bunga terbuka.', 'perawatan-berbunga.jpg', ['Air: jaga ketersediaan', 'Hama: periksa malai terpotong']),
    C('Pemasakan', 'Bulir terisi dan menguning.', 'perawatan-pemasakan.jpg', ['Air: dikurangi bertahap', 'Pupuk: jangan berlebihan nitrogen', 'Hama: pasang perangkap']),
    C('Panen', 'Panen pada waktu yang tepat.', 'perawatan-panen.jpg', ['Air: dikeringkan', 'Panen tepat waktu agar tidak dimakan tikus'])]},
  {'h': 'Empat faktor kunci perawatan', 'type': 'cards', 'cols': 2, 'items': [
    C('Benih dan varietas', 'Gunakan benih bersertifikat, sehat, dan sesuai musim serta kondisi lahan. Seragamkan varietas dalam satu hamparan.', 'perawatan-benih.jpg'),
    C('Pengelolaan air', 'Atur genangan dangkal pada fase vegetatif dan keringkan menjelang panen. Rawat saluran agar tidak jadi sarang tikus.', 'perawatan-air.jpg'),
    C('Pemupukan berimbang', 'Kombinasi N, P, dan K yang seimbang membuat tanaman kokoh. Nitrogen berlebihan membuat tanaman lunak dan mudah rebah.', 'perawatan-pupuk.jpg'),
    C('Pengendalian gulma', 'Siangi gulma awal agar tidak bersaing dengan padi, termasuk gulma pematang yang menjadi tempat berlindung tikus.', 'perawatan-gulma.jpg')],
   'note': 'Lakukan uji tanah atau ikuti rekomendasi penyuluh agar dosis pupuk tepat.'}]},

'penanganan': {'title': 'Penanganan Hama',
 'lead': 'Setelah serangan terdeteksi, tentukan dulu seberapa berat serangannya, lalu pilih tindakan yang sesuai. Pengendalian paling efektif bila dilakukan serentak oleh seluruh petani di hamparan.',
 'sections': [
  {'h': 'Menilai tingkat serangan', 'type': 'table', 'head': ['Tingkat', 'Ciri di lahan', 'Tindakan utama'], 'rows': [
    ['Ringan', 'Sedikit rumpun terpotong, lubang aktif sedikit', 'Sanitasi, pasang perangkap, pantau harian'],
    ['Sedang', 'Rumpun terpotong tersebar, lubang aktif cukup banyak', 'Gropyokan, emposan, perangkap tambahan'],
    ['Berat', 'Banyak rumpun rebah atau hilang, lubang aktif banyak', 'Gerakan bersama kelompok tani dan lapor penyuluh (PPL)']],
   'note': 'Hasil klasifikasi aplikasi hanya alat bantu. Cocokkan selalu dengan pengamatan langsung di sawah.'},
  {'h': 'Tiga cara pengendalian langsung', 'type': 'cards', 'cols': 3, 'items': [
    C('Gropyokan', 'Perburuan massal serentak, sebaiknya sebelum fase bunting.', 'tangani-gropyok.jpg', ['Mulai dari pematang dan tanggul', 'Atur barisan agar tikus tidak lolos', 'Musnahkan tikus yang tertangkap']),
    C('Emposan belerang', 'Asap belerang dialirkan ke lubang aktif.', 'tangani-emposan.jpg', ['Tutup lubang lain agar asap tidak bocor', 'Gunakan sesuai petunjuk dan hati-hati']),
    C('Perangkap', 'Bubu atau jebakan di jalur lintasan.', 'tangani-perangkap.jpg', ['Pasang di jalur ramai dilalui', 'Periksa setiap hari'])]},
  {'h': 'Rodentisida: pilihan terakhir', 'type': 'steps', 'intro': 'Dipakai hanya bila cara lain tidak cukup. Gunakan produk terdaftar dan ikuti petunjuk label.', 'items': [
    {'t': 'Pasang di tempat aman', 'd': 'Jauhkan dari anak-anak, ternak, dan hewan peliharaan.'},
    {'t': 'Lindungi diri', 'd': 'Pakai sarung tangan dan cuci tangan sesudahnya.'},
    {'t': 'Bersihkan sisa', 'd': 'Kumpulkan dan kubur bangkai tikus serta sisa umpan.'},
    {'t': 'Hindari fumigan sendiri', 'd': 'Fumigan berbahaya dan sebaiknya dikerjakan petugas terlatih.'}]},
  {'h': 'Memulihkan tanaman setelah serangan', 'type': 'steps', 'items': [
    {'t': 'Nilai fase tanaman', 'd': 'Serangan di fase vegetatif awal masih bisa dipulihkan, fase generatif tidak.'},
    {'t': 'Lakukan penyulaman', 'd': 'Ganti rumpun yang hilang bila masih fase awal.'},
    {'t': 'Rawat anakan baru', 'd': 'Jaga air dan pemupukan sesuai anjuran.'},
    {'t': 'Cegah penyebaran', 'd': 'Pada fase generatif, fokus menahan serangan agar tidak meluas.'}],
   'note': 'Hubungi penyuluh pertanian lapangan (PPL) atau petugas POPT setempat bila serangan meluas dalam hitungan hari.'}]},

'tentang': {'title': 'Tentang Sistem',
 'lead': 'PadiScan adalah aplikasi web untuk mengklasifikasikan kondisi tanaman padi akibat serangan hama tikus dari foto, menggunakan Convolutional Neural Network (CNN) arsitektur MobileNetV2.',
 'sections': [
  {'h': 'Tahapan penelitian', 'type': 'steps', 'fig': ('metodologi.svg', 'Tahapan penelitian dari pengumpulan data hingga implementasi aplikasi.'), 'items': [
    {'t': 'Pengumpulan citra', 'd': 'Foto tanaman padi dikumpulkan dari lapangan atau sumber dataset.'},
    {'t': 'Pelabelan kelas', 'd': 'Setiap foto diberi label sesuai kelas kondisi tanaman.'},
    {'t': 'Praproses dan augmentasi', 'd': 'Foto diubah ke 224 x 224 piksel, dinormalisasi, dan diaugmentasi (balik dan putar).'},
    {'t': 'Pelatihan model', 'd': 'MobileNetV2 dilatih dengan transfer learning dan lapisan klasifikasi tambahan.'},
    {'t': 'Evaluasi', 'd': 'Model diuji pada data uji memakai akurasi, presisi, recall, F1-score, dan confusion matrix.'},
    {'t': 'Implementasi', 'd': 'Model terbaik dipasang pada aplikasi web ini.'}]},
  {'h': 'Arsitektur model', 'type': 'text', 'intro': 'MobileNetV2 dipakai sebagai pengekstraksi ciri, lalu diikuti lapisan klasifikasi untuk menghasilkan peluang tiap kelas.', 'fig': ('arsitektur.svg', 'Susunan lapisan model klasifikasi pada PadiScan.')},
  {'h': 'Ringkasan model', 'type': 'facts', 'items': [
    {'v': 'MobileNetV2', 'd': 'arsitektur CNN ringan'}, {'v': '224 x 224 x 3', 'd': 'ukuran input citra'},
    {'v': 'Dense 128', 'd': 'lapisan klasifikasi (ReLU)'}, {'v': '3 kelas', 'd': 'keluaran softmax'}]},
  {'h': 'Cara kerja prediksi', 'type': 'text', 'fig': ('alur.svg', 'Alur klasifikasi dari foto hingga hasil.'), 'intro': 'Foto diubah ke ukuran 224 x 224 piksel lalu dinormalisasi. Model menghitung peluang untuk setiap kelas dengan softmax, dan kelas dengan peluang tertinggi ditampilkan beserta tingkat keyakinannya, lalu disimpan ke riwayat.'},
  {'h': 'Alur penggunaan aplikasi', 'type': 'steps', 'items': [
    {'t': 'Daftar dan masuk', 'd': 'Buat akun lalu login. Semua halaman hanya bisa diakses setelah login.'},
    {'t': 'Unggah foto', 'd': 'Pilih foto tanaman pada halaman Klasifikasi.'},
    {'t': 'Lihat hasil', 'd': 'Hasil berisi kelas, keyakinan, dan langkah yang disarankan.'},
    {'t': 'Cek riwayat', 'd': 'Semua pemeriksaan tersimpan dan dapat dibuka kembali di detail.'},
    {'t': 'Pelajari penanganan', 'd': 'Gunakan halaman edukasi untuk menindaklanjuti hasil.'}]},
  {'h': 'Membaca hasil dan tips memotret', 'type': 'cards', 'cols': 3, 'items': [
    C('Tingkat keyakinan', 'Menunjukkan seberapa kuat model memilih kelas itu dibanding kelas lain. Nilai tinggi belum menjamin benar pada foto yang jauh berbeda dari data latih.'),
    C('Foto yang baik', 'Ambil dari jarak dekat, cahaya cukup, fokus pada batang dan malai, serta hindari foto buram atau terlalu gelap.'),
    C('Keterbatasan', 'Model hanya mengenali kelas pada data latihnya. Varietas, sudut, dan kualitas foto memengaruhi hasil. Aplikasi bukan pengganti ahli.')]},
  {'h': 'Data dan evaluasi penelitian', 'type': 'cards', 'cols': 3, 'intro': 'Isi bagian ini dengan hasil penelitian Anda: taruh gambar di static/foto lalu ubah teks di content.py.', 'items': [
    C('Contoh citra dataset', 'Sumber dataset, jumlah citra tiap kelas, dan pembagian data latih dan uji.', 'dataset-contoh.jpg'),
    C('Grafik pelatihan', 'Kurva akurasi dan loss selama pelatihan.', 'grafik-training.png'),
    C('Confusion matrix', 'Hasil evaluasi pada data uji beserta nilai akurasi, presisi, recall, dan F1.', 'confusion-matrix.png')]}]}}
