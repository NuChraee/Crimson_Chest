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

## Implementasi Skeleton sebagai Kerangka Views

1. Buat folder bernama `templates` pada root folder lalu buat file HTML baru di dalam folder `templates` dengan nama `base.html`, serta isi base html dengan kode ini
```py
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
```

2. Buka `settings.py` yang ada pada subdirektori yang kita miliki (dalam kasus ini subdirektori saya adalah `Crimson_Chest`) lalu cari baris yang mengandung `TEMPLATES`. Setelah sesuaikan dengan kode berikut
```py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini pada settings.py
        'APP_DIRS': True,
        ...
    }
]
```

3. Buka file `main.html` yang terdapat pada subdirektori templates yang ada di direktori main, lalu ubah kode di dalamnya agar menjadi seperti ini
```py
{% extends 'base.html' %}

{% block content %}
    ...
    Kode yang ingin kita masukkan
    ...
{% endblock content %}
```

## Membuat Input Data pada Form Agar Dapat Menampilkan Data Produk Pada HTML

1. Buat file baru pada direktori `main` dengan nama `forms.py` untuk membuat struktur form yang dapat menerima data produk baru. Sebelum menambahkan kode pada file `forms.py` pastikan sudah mengaktifkan virtual environment terlebih dahulu. Setelah virtual environment sudah aktif isi file `forms.py` dengan kode ini
```py
from django.forms import ModelForm
from main.models import Item

class ProductForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name","amount", "price","sell", "description", "modifiers" ]
```
Sesuaikan value model dan fields sesuai dengan yang anda butuhkan

2. Buka file `views.py` yang ada pada folder `main` dan tambahkan import dan kode berikut
```py
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```
## Menambahkan fungsi views untuk melihat objek yang sudah ditambahkan Pada HTML, XML, JSON, XML by ID, dan JSON by ID

### Pada HTML
1. Ubah fungsi `show_main` pada file `views.py` menjadi seperti ini
```py
def show_main(request):
    products = Item.objects.all()

    context = { #sesuaikan isi context dengan kode anda
        'appname' : 'Crimson Chest',
        'name': 'Caesar Syahru Ramadhan',
        'class': 'PBP C',
        'products': products,
    }

    return render(request, "main.html", context)
```

2. Buka file `urls.py` yang ada pada direktori `main` dan import fungsi create_product
```py
from main.views import show_main, create_product
```

3. Lalu tambahkan path url ke dalam urlpatterns pada `urls.py` di `main` untuk mengakses fungsi yang sudah di-import sebelumnya.
```py
path('create-product', create_product, name='create_product'),
```

4. Buat file HTML baru dengan nama `create_product.html` pada subdirektori `templates` yang ada pada direktori `main`, lalu isi file tersebut dengan kode berikut
```py
{% extends 'base.html' %} 

{% block content %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        *{
                background-color:antiquewhite;
            }
            
        #add {
                background: linear-gradient(4deg, #F94C10 6%, #F8DE22 99%);
                color: white;
                font-weight: bold;
                border: 2px solid #25316D;
                border-radius: 10px;
                cursor: pointer;
                padding: 10px 10px;
        }

        #tabel{
            background: linear-gradient(4deg, #F94C10 6%, #F8DE22 99%);
        }
    </style>
</head>
<body>
    <h1 style="text-align: center;">Add New Product</h1>

<form method="POST" >
    {% csrf_token %}
    <center>
    <table >
        {{ form.as_table }}
        <tr >
            <td ></td>
            <td >
                <input id="add" type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
    </center>
</form>
</body>
</html>


{% endblock %}
```
Anda dapat menambahkan style menggunakan css sesuai dengan kebutuhan anda

5. Buka `main.html` dan tambahkan kode berikut di dalam `{% block content %}` dan sebelum `{% endblock content %}`
```PY
...
<table>
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Date Added</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

    {% for product in products %}
        <tr>
            <td>{{product.name}}</td>
            <td>{{product.price}}</td>
            <td>{{product.description}}</td>
            <td>{{product.date_added}}</td>
        </tr>
    {% endfor %}
</table>

<br />

<a href="{% url 'main:create_product' %}">
    <button>
        Add New Product
    </button>
</a>

```

### Pada XML
1. Buka `views.py` yang ada pada folder `main`, lalu tambahkan import ini
```py
from django.http import HttpResponse
from django.core import serializers
```

2. Lalu tambahkan kode ini 
```py
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

3. Buka `urls.py` yang ada pada folder `main`, lalu tambahkan import ini
```py
from main.views import show_main, create_product, show_xml 
```

4. Lalu tambahkan path url ini ke dalam `urlpatterns`
```py
path('xml/', show_xml, name='show_xml'), 
```

### Pada JSON
1. Buka `views.py` yang ada pada folder `main`, lalu buat fungsi baru yang menerima parameter request
```py
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

2. Buka `urls.py` yang ada pada folder `main`, lalu tambahkan import ini
```py
from main.views import show_main, create_product, show_xml, show_json
```

3. Lalu tambahkan path url ini ke dalam `urlpatterns`
```py
path('json/', show_json, name='show_json'), 
```

### Pada XML by ID, dan JSON by ID
1. Buka `views.py` yang ada pada folder `main` dan buatlah sebuah fungsi baru yang menerima parameter request, seperti kode dibawah ini

Dalam format XML
```py
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

Dalam format JSON
```py
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

2. Buka `urls.py` yang ada pada folder `main`, lalu tambahkan import ini
```py
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
```
Jika sudah memasukan import di atas, kalian bisa menghapus beberapa import yang sudah terkandung pada import di atas, karena import di atas sudah mengandung beberapa import

3. Lalu tambahkan path url ini ke dalam `urlpatterns`
```py
path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
```

Hasil akhir akan terlihat seperti ini
```py
from django.urls import path
from main.views import show_main, create_product,delete_element, show_xml, show_json, show_xml_by_id, show_json_by_id 


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]
```

## Perbedaan Antara Form POST dan Form GET dalam Django

1. Metode HTTP yang digunakan:
    1. POST: Mengirim data melalui tubuh permintaan HTTP. Data ini biasanya disembunyikan dari URL dan dapat digunakan untuk mengirim data yang sensitif atau besar. Biasanya digunakan untuk mengirim data yang akan membuat perubahan di sisi server, seperti mengirim formulir untuk membuat, mengedit, atau menghapus entitas.

    2. GET: Mengirim data sebagai parameter yang terlihat di URL. Data ini terbatas dalam ukuran dan biasanya digunakan untuk permintaan pencarian atau permintaan yang bersifat idempoten, yang berarti permintaan dapat dieksekusi beberapa kali tanpa menghasilkan perubahan yang tidak diinginkan.

2. Keamanan:
    1. POST: Lebih aman daripada GET karena data tidak terlihat di URL, yang berarti data sensitif seperti kata sandi tidak akan tampil secara terbuka.

    2. GET: Kurang aman karena data terlihat di URL dan dapat dengan mudah diakses oleh pihak ketiga.

3. Penggunaan:
    1. POST: Digunakan untuk mengirim data yang mengubah status atau membuat perubahan di sisi server.
    2. GET: Digunakan untuk mengambil data dari server tanpa membuat perubahan.

## Perbedaan Utama Antara XML, JSON, dan HTML Dalam Konteks Pengiriman Data

Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data adalah dalam tujuan dan format representasi data mereka:

1. XML (Extensible Markup Language):
    1. `Tujuan Utama`: XML adalah bahasa markup yang digunakan untuk mendefinisikan struktur data. Ini lebih berfokus pada representasi struktur data dan tidak memiliki tujuan khusus dalam hal tampilan atau interaksi pengguna.

    2. `Sintaks`: XML menggunakan tag dan atribut yang dapat diatur secara bebas untuk menggambarkan data. hal ini membuatnya sangat fleksibel tetapi juga cenderung memiliki sintaksis yang lebih berat dan sulit dibaca oleh manusia.

    3. `Penggunaan Umum`: XML sering digunakan untuk pertukaran data yang terstruktur antara aplikasi atau sistem yang berbeda, seperti konfigurasi, SOAP dalam layanan web, atau penyimpanan data.

2. JSON (JavaScript Object Notation):
    1. `Tujuan Utama`: JSON adalah format ringan yang digunakan untuk pertukaran data antara aplikasi. Ini dirancang dengan tujuan mudah dibaca oleh manusia dan mudah diproses oleh komputer.

    2. `Sintaks`: JSON menggunakan struktur objek yang mirip dengan sintaks di JavaScript. Hal ini membuatnya sederhana dan mudah dipahami.

    3. `Penggunaan Umum`: JSON sangat umum digunakan dalam aplikasi web modern sebagai format pertukaran data antara server dan klien, terutama dalam pengembangan API RESTful.

3. HTML (Hypertext Markup Language):
    1. `Tujuan Utama`: HTML adalah bahasa markup yang digunakan untuk membuat tampilan halaman web. Ini berfokus pada representasi visual dan interaksi pengguna pada halaman web.

    2. `Sintaks`: HTML menggunakan tag dan atribut khusus yang mendefinisikan elemen-elemen tampilan seperti teks, gambar, tautan, dan formulir. Ini lebih terfokus pada tampilan daripada pada struktur data.

    3. `Penggunaan Umum`: HTML digunakan untuk membuat halaman web dan mengatur cara elemen-elemen ini ditampilkan kepada pengguna melalui browser web. Ini tidak digunakan untuk pertukaran data antara aplikasi, kecuali dalam konteks web scraping.

Jadi, perbedaan utama antara ketiganya adalah dalam tujuan dan sintaksis mereka. XML digunakan untuk mendefinisikan struktur data, JSON digunakan untuk pertukaran data antara aplikasi, dan HTML digunakan untuk mengatur tampilan dan interaksi pada halaman web.

## Alasan JSON sering digunakan dalam pertukaran data antara aplikasi web modern

1. JSON memiliki sintaks yang sederhana dan mudah dipahami oleh manusia, karena struktur objeknya  mirip dengan sintaks di JavaScript
2. Format JSON sangat ringan dalam hal ukuran file, bahkan untuk data yang besar. Hal ini mengurangi overhead dalam komunikasi data antara server dan klien
3. JSON mendukung struktur data nested, yang memungkinkan pengiriman data yang kompleks dengan representasi yang hierarkis dan terstruktur
4. JSON dapat dengan mudah diurai dan dibuat dalam JavaScript, yang merupakan bahasa pemrograman yang umum digunakan dalam pengembangan aplikasi web
5. JSON mendukung tipe data dasar seperti string, angka, dan objek
6. Banyak sistem database modern memiliki dukungan untuk menyimpan dan mengambil data dalam format JSON. Hal ini mempermudah integrasi antara aplikasi web dan database
7. Ada banyak pustaka dan alat yang tersedia dalam berbagai bahasa pemrograman untuk penguraian dan pembuatan JSON

## Screenshot dari hasil akses URL pada Postman

### HTML
![Postman HTML](/IMG/HTML%20Screenshot.png)

### XML
![Postman XML](/IMG/XML%20Screenshot.png)

### JSON
![Postman JSON](/IMG/JSON%20Screenshot.png)

## XML by ID
![Postman XML by ID](/IMG/XML%20by%20ID%20Screenshot.png)

## JSON by ID
![Postman JSON by ID](/IMG/JSON%20by%20ID%20Screenshot.png)