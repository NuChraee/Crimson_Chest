Nama    : Caesar Syahru Ramadhan

NPM     : 2206819092

Kelas   : PBP C

Berikut adalah tautan link adaptable saya. [Adaptable Link](https://crimson-chestvol2.adaptable.app)

##(Membuat proyek Django baru)

1. Pastikan kita sudah membuat direktori yang ingin kita gunakan untuk membuat proyek Django baru.
2. Lalu buka command prompt atau terminal shell di dalam direktori yang sudah kita buat sebelumnya.
3. setelah membuka command prompt jalankan perintah ini '(python -m venv env)' pada command prompt untuk membuat lingkungan virtual Python menggunakan modul 'venv', serta untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer kita.
4. Lalu aktifkan virtual environment dengan perintah '(env\Scripts\activate.bat)' (Windows) atau source '(env/bin/activate)' (Linux/Mac).
5. Buat file pada direktori yang sama, dan diberi nama '(requirements.txt)' lalu tambahkan dependencies yang dibutuhkan
6. Install dependencies yang diperlukan dengan perintah '(pip install -r requirements.txt)', kemudian buat proyek Django dengan menjalankan perintah '(django-admin startproject (nama_app) .)'
7. Buka file '(settings.py)' yang ada di dalam folder proyek, lalu cari variabel '(ALLOWED_HOSTS)' dan ubah nilainya menjadi ["*"] untuk mengizinkan akses dari semua host.
8. Kembali ke command prompt atau terminal dan jalankan perintah '(python manage.py runserver)' di dalam direktori proyek untuk menjalankan server.
9. Kita dapat membuka proyek Django baru di browser dengan mengakses '(http://localhost:8000)'. Jika melihat animasi roket, maka proyek Django sudah berhasil.
10. Untuk menghentikan server, cukup tekan '(Ctrl+C)' di command prompt atau terminal. Lalu jalankan perintah '(deactivate)' untuk mematikan virtual enviroment

