Nama    : Caesar Syahru Ramadhan

NPM     : 2206819092 

Kelas   : PBP C

Berikut adalah tautan link adaptable saya. [Adaptable Link](https://crimson-chestvol2.adaptable.app/main/)

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
```py
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
```py
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
    modifiers = models.TextField()
    amount = models.IntegerField()
```
3. Jalankan perintah `python manage.py makemigrations` di command prompt untuk mempersiapkan migrasi skema model ke dalam database Django lokal.

4. Jalankan perintah `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.

## Membuat sebuah fungsi pada `views.py`

1. Buka file `views.py` yang ada di dalam direktori aplikasi main.
2. Tambahkan import berikut 
```py
from django.shortcuts import render
```
3. Lalu tambahkan fungsi `show_main` dengan context sesuai kebutuhan kalian
```py
def show_main(request):
    context = {
        'name': '(nama kalian)',
        'class': '(kelas PBP kalian)'
        'dan lainnya sesuai kebutuhan kalian'
    }

    return render(request, "main.html", context)
```
4. Setelah itu buka file `main.html`yang ada di dalam direktori templates pada direktori `main` dan ubah nama dan kelas dan hal lainnya sesuai dengan isi context yang telah anda isi sebelumnya yang awalnya dibuat secara statis menjadi kode Django yang sesuai untuk menampilkan data.

```py
<h5>Name: </h5>
<p>{{ name }}<p>
<h5>Class: </h5>
<p>{{ class }}<p>
```
Penjelasan : Sintaks Django {{ name }} dan {{ class }} digunakan untuk menampilkan nilai dari variabel yang telah didefinisikan dalam context.

## Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

1. Membuat file `urls.py` pada direktori `main`. Lalu, isi `urls.py` yang telah kita buat sebelumnya dengan kode berikut.
```python
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

## Bagan yang berisi request client ke web aplikasi berbasis Django
![How Django Framework Works](/main/templates/Caesar%20PBP%20C.png) 

Pertama user akan meminta request kepada Django, lalu Django akan menggunakan `urls.py`. Setelah itu, `views.py` akan mengatur berbagai macam bentuk interaksi agar di dalam `models.py` dapat mengelola dan menyajikan data agar data yang telah diolah oleh `models.py` dapat ditampilkan pada templates dalam berkas `html`. Pada berkas `html`, berisi berbagai macam kode html seperti kode untuk membuat tabel, list, menentukan ukuran font dan lain lain, serta pada berkas `html` juga mengandung tag template Django agar dapat memasukan data dari dalam `views.py` ke dalam berkas `html`. Setelah selesai diolah, output tersebut akan dikirimkan sebagai respon kepada user.

## Mengapa kita menggunakan virtual Environment

Virtual environment adalah cara untuk menjaga proyek perangkat lunak Anda tetap rapi dan teratur. Virtual environment adalah seperti punya tempat khusus untuk setiap resep, sehingga Anda bisa bekerja dengan lebih teratur dan aman.  Virtual environment membantu kita membuat "lingkungan" terpisah untuk setiap proyek. Ini berguna karena setiap proyek mungkin memerlukan versi yang berbeda dari perpustakaan Python atau paket tambahan. Dengan virtual environment, kita dapat mengisolasi proyek-proyek tersebut sehingga tidak ada konflik antara mereka.

Dengan virtual environment, kita dapat menginstal paket-paket Python yang diperlukan untuk proyek kita tanpa merusak instalasi Python global pada komputer kita. Ini memudahkan kita dalam mengelola dependensi proyek secara terpisah. Serta Virtual environment membantu menjaga kebersihan dan keamanan sistem kita. Kita dapat menginstal atau menghapus paket dengan bebas dalam lingkungan virtual tanpa mengkhawatirkan dampaknya pada sistem operasi utama.

## Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jadi, kenapa kita perlu virtual environment saat membuat aplikasi web berbasis Django? Karena dalam pengembangan perangkat lunak, kita seringkali harus menggunakan berbagai versi berbeda dari bahasa pemrograman, perpustakaan, atau alat tertentu. Ini bisa menjadi seperti resep-resep yang berbeda dalam masak. Virtual environment memungkinkan kita untuk memiliki lingkungan yang terisolasi di dalam proyek kita, di mana kita dapat menginstal versi tertentu dari bahasa pemrograman dan perpustakaan yang kita butuhkan tanpa merusak atau mengganggu proyek lain.

## Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya

MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah tiga kerangka kerja desain yang umumnya digunakan dalam pengembangan perangkat lunak, terutama dalam lingkungan pengembangan aplikasi berbasis web dan antarmuka pengguna (UI). Tujuan utama dari kerangka kerja ini adalah untuk memecah aplikasi menjadi komponen-komponen yang terpisah, sehingga mempermudah proses pengembangan, perawatan, dan pengelolaan kode yang lebih terstruktur dan rapi.

##  perbedaan dari ketiganya

1. MVC (Model-View-Controller):

Pemisahan Kontrol: MVC memisahkan komponen-komponen aplikasi menjadi Model (data dan logika), View (tampilan), dan Controller (logika pengendalian). Controller bertindak sebagai perantara antara Model dan View.
Umumnya Digunakan di Aplikasi Web: MVC adalah arsitektur yang umum digunakan dalam pengembangan aplikasi web dan desktop.
Contoh: Ruby on Rails, AngularJS (versi lama).

2. MVT (Model-View-Template):

Mirip dengan MVC: MVT adalah konsep yang serupa dengan MVC, dengan Model yang mewakili data dan logika, View yang menampilkan data, dan Template yang mengatur cara data ditampilkan dalam HTML.
Khusus untuk Django: MVT adalah konsep yang khusus digunakan dalam kerangka kerja web Django untuk pengembangan aplikasi web berbasis Python.

3. MVVM (Model-View-ViewModel):

Peran ViewModel: MVVM mempertahankan Model (data dan logika), View (tampilan), dan menambahkan komponen ViewModel. ViewModel berfungsi sebagai perantara antara Model dan View, mengubah data dari Model ke format yang dapat ditampilkan oleh View dan mengatur tindakan pengguna pada tampilan.
Umumnya Digunakan di Aplikasi UI: MVVM adalah arsitektur yang sering digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI), seperti aplikasi mobile dan desktop.

