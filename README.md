Nama    : Caesar Syahru Ramadhan

NPM     : 2206819092

Kelas   : PBP C

Berikut adalah tautan link adaptable saya. [Adaptable Link](https://crimson-chestvol2.adaptable.app)

## Membuat proyek Django baru

1. Pastikan kita sudah membuat direktori yang ingin kita gunakan untuk membuat proyek Django baru.
2. Lalu buka command prompt atau terminal shell di dalam direktori yang sudah kita buat sebelumnya.
3. setelah membuka command prompt jalankan perintah ini ``python -m venv env`` pada command prompt untuk membuat lingkungan virtual Python menggunakan modul ``venv``, serta untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer kita.
4. Lalu aktifkan virtual environment dengan perintah ``env\Scripts\activate.bat`` (Windows) atau source ``env/bin/activate`` (Linux/Mac).
5. Buat file pada direktori yang sama, dan diberi nama ``requirements.txt`` lalu tambahkan dependencies yang dibutuhkan
6. Install dependencies yang diperlukan dengan perintah ``pip install -r requirements.txt``, kemudian buat proyek Django dengan menjalankan perintah ``django-admin startproject (nama_app) .``
7. Buka file ``settings.py`` yang ada di dalam folder proyek, lalu cari variabel ``ALLOWED_HOSTS`` dan ubah nilainya menjadi ["*"] untuk mengizinkan akses dari semua host.
8. Kembali ke command prompt atau terminal dan jalankan perintah `python manage.py runserver` di dalam direktori proyek untuk menjalankan server.
9. Kita dapat membuka proyek Django baru di browser dengan mengakses `http://localhost:8000`. Jika melihat animasi roket, maka proyek Django sudah berhasil.
10. Untuk menghentikan server, cukup tekan ``Ctrl+C`` di command prompt atau terminal. Lalu jalankan perintah ``deactivate`` untuk mematikan virtual enviroment

## Membuat aplikasi dengan nama main pada proyek tersebut

1. Buka direktori utama dan buka Command Prompt. Selanjutnya, aktifkan virtual environment menggunakan perintah `env\Scripts\activate.bat`.

2. Buat folder baru dengan nama `main` dengan menjalankan perintah `python manage.py startapp main`.

3. Untuk mendaftarkan aplikasi `main` ke dalam proyek, Anda perlu mengedit file `settings.py` yang terletak dalam direktori proyek. Tambahkan `main` ke dalam daftar variabel INSTALLED_APPS.

## Melakukan routing pada proyek agar dapat menjalankan aplikasi main.

1. Buatlah berkas `urls.py` di dalam direktori main. Lalu isi `urls.py` dengan kode ini
```
    from django.urls import path 
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
```
2. Berkas urls.py pada aplikasi main bertanggung jawab untuk mengatur rute URL yang terkait dengan aplikasi main.

## Membuat model pada aplikasi `main`

1. Buka file `models.py` dan isi file tersebut dengan nama Item dan atribut-atribut dan tipe data yang ingin digunakan.
2. Lalu salin kode di bawah ini, dan letakkan pada file `models.py`
```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
```
3. Jalankan perintah `python manage.py makemigrations` di command prompt untuk mempersiapkan migrasi skema model ke dalam database Django lokal.

4. Jalankan perintah `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.

## Membuat sebuah fungsi pada `views.py`

1. Buka file `views.py` yang ada di dalam direktori aplikasi main.
2. Tambahkan import berikut 
```
from django.shortcuts import render
```
3. Lalu tambahkan fungsi `show_main`
```
def show_main(request):
    context = {
        'name': '(nama kalian)',
        'class': '(kelas PBP kalian)'
    }

    return render(request, "main.html", context)
```
4. Setelah itu buka file `main.html`yang adad di dalam direktori templates pada direktori `main` dan ubah nama dan kelas yang sebelumnya dibuat secara statis menjadi kode Django yang sesuai untuk menampilkan data.

```
<h5>Name: </h5>
<p>{{ name }}<p>
<h5>Class: </h5>
<p>{{ class }}<p>
```
Penjelasan : Sintaks Django {{ name }} dan {{ class }} digunakan untuk menampilkan nilai dari variabel yang telah didefinisikan dalam context.

## Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

1. Membuat file `urls.py` pada direktori `main`. Lalu, isi `urls.py` yang telah kita buat sebelumnya dengan kode berikut.
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
Penjelasan : Berkas urls.py pada aplikasi main bertanggung jawab untuk mengatur rute URL yang terkait dengan aplikasi main dan impor path dari django.urls untuk mendefinisikan pola URL.

## Mengonfigurasi Routing URL Proyek

1. Buka berkas urls.py di dalam direktori proyek, bukan yang ada di direktori main
2. Impor fungsi include dari django.urls. 
    `from django.urls import path, include`
3. Tambahkan rute URL seperti berikut untuk mengarahkan ke tampilan main di dalam variabel urlpatterns.
    `path('main/', include('main.urls')),`

    penjelasan : Berkas `urls.py` dalam proyek memiliki tanggung jawab untuk mengelola pengaturan URL pada tingkat proyek. Fungsi `"include"` digunakan untuk memasukkan atau mengintegrasikan pengaturan URL dari aplikasi lain (dalam hal ini, dari aplikasi `"main"`) ke dalam berkas `urls.py` proyek.

4. Jalankan proyek Django dengan perintah `python manage.py runserver`
5. Bukalah [http://localhost:8000/main/](http://localhost:8000/main/) di peramban web, untuk melihat halaman yang sudah dibuat

## Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat

1. Setelah login, pilih "New App" dan "Connect an Existing Repository".
2. Pilih repositori proyek aplikasi yang telah diunggah ke github dan branch untuk deployment.
3. Pilih template deployment "Python App Template" dan pilih PostgreSQL sebagai tipe basis data.
4. Sesuaikan versi Python dengan yang dibutuhkan (cek menggunakan perintah python --version pada command prompt).
5. Isi Start Command dengan python manage.py migrate && gunicorn (nama direktori utama).wsgi.
6. Tentukan nama aplikasi yang juga akan menjadi nama domain situs web.
7. Centang "HTTP Listener on PORT" dan klik "Deploy App" untuk memulai proses deployment aplikasi.
8. Lalu tunggu hingga semua indikasi berwarna hijau, yang menanjakan semua proses telah berhasil