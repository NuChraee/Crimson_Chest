Nama    : Caesar Syahru Ramadhan

NPM     : 2206819092 

Kelas   : PBP C

Berikut adalah tautan link adaptable saya. [Adaptable Link](https://crimson-chestvol2.adaptable.app/main/)

berikut adalah link tugas:

[Tugas 2](#Tugas-2)

[Tugas 3](#tugas-3)

[Tugas 4](#tugas-4)

[Tugas 5](#tugas-5)


# Tugas 2

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

# Tugas 3

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

### XML by ID
![Postman XML by ID](/IMG/XML%20by%20ID%20Screenshot.png)

### JSON by ID
![Postman JSON by ID](/IMG/JSON%20by%20ID%20Screenshot.png)


# TUGAS 4

## Membuat Fungsi dan Form Registrasi

1. Pastikan program anda sudah menjalankan virtual environment
2. Buka `views.py` pada subdirektori `main` lalu masukan import dibawah ini
```py
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
```

Lalu masukan kode ini
```py
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

3. Lalu, buatlah file baru dengan nama `register.html` pada folder `main/templates` lalu masukan kode ini
```py
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```

4. Buka `urls.py` pada subdirektori `main`, lalu tambah import ini
```py
from main.views import register #pastikan import sesuai dengan fungsi yang sudah anda buat
```

5. Lalu, tambahkan path url ini pada `urls.py`
```py
path('register/', register, name='register'), #Sesuaikan dengan fungsi yang sudah anda buat
```

## Membuat Fungsi Login

1. Buka `views.py` pada subdirektori `main` lalu masukan import dibawah ini
```py
from django.contrib.auth import authenticate, login
```

Lalu masukan kode ini
```py
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```

2. Lalu, buatlah file baru dengan nama `login.html` pada folder `main/templates` lalu masukan kode ini
```py
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```

3. Buka `urls.py` pada subdirektori `main`, lalu tambah import ini
```PY
from main.views import login_user #Sesuaikan dengan fungsi yang anda buat
```

4. Lalu, tambahkan path url ini pada `urls.py`
```py
path('login/', login_user, name='login'), #Sesuaikan dengan fungsi yang anda buat
```

## Membuat Fungsi Logout

1. Buka `views.py` pada subdirektori `main` lalu masukan import dibawah ini
```py
from django.contrib.auth import logout
```

Lalu masukan kode ini
```py
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

2. Lalu, buka file `main.html` pada folder `main/templates` lalu masukan kode ini
```py
...
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
...
```

3. Buka `urls.py` pada subdirektori `main`, lalu tambah import ini
```PY
from main.views import logout_user
```

4. Lalu, tambahkan path url ini pada `urls.py`
```py
path('logout/', logout_user, name='logout'),
```

## Merestriksi Akses Halaman

1. Buka `views.py` pada subdirektori `main` lalu masukan import dibawah ini
```py
from django.contrib.auth.decorators import login_required
```

Lalu, tambahkan kode `@login_required(login_url='/login')` di atas fungsi `show_main`
```py
...
@login_required(login_url='/login')
def show_main(request):
...
```

## Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi

1. jika kita sedang berada di halaman yang berisikan daftar produk, logout terlebih dahulu
2. Buka `views.py` pada subdirektori `main` lalu masukan import dibawah ini
```py
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```

3. Pada fungsi `login_user`, ganti kode yang ada pada blok `if user is not None` menjadi seperti ini
```py
...
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
``` 
Hal ini dilakukan untuk menambahkan cookie yang bernama `last_login` untuk melihat kapan terakhir kali pengguna melakukan login

4. Pada fungsi `show_main`, tambahkan potongan kode `'last_login': request.COOKIES['last_login']` ke dalam `context`
```py
context = {
    ...
    'last_login': request.COOKIES['last_login'],
}
...
```

5. Ubah fungsi `logout_user` menjadi seperti ini
```py
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

6. Buka file `main.html` pada folder `main/templates` dan masukan kode dan sesuaikan dengan kodingan anda
```py
<h5>Sesi terakhir login: {{ last_login }}</h5>
```

## Menghubungkan model Item dengan User

1. Buka `models.py` yang ada pada subdirektori `main` dan tambahkan import ini
```py
from django.contrib.auth.models import User
```

2. Tambahkan kode ini pada model `Item`
```py
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```

3. Buka `views.py` yang ada pada subdirektori `main`, dan ubah potongan kode pada fungsi `create_product` menjadi seperti ini
```py
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```

4. Lalu lakukan perintah `python manage.py makemigrations` pada mode virtual environment
5. Seharusnya, akan muncul error saat melakukan migrasi model. Pilih 1 untuk menetapkan default value untuk field user pada semua row yang telah dibuat pada basis data.
![Alt text](/IMG/makemigrasi1.png) 

6. Ketik angka 1 lagi untuk menetapkan user dengan ID 1 (yang sudah kita buat sebelumnya) pada model yang sudah ada.
![Alt text](/IMG/makemigrasi2.png)

7. Lakukan python manage.py migrate untuk mengaplikasikan migrasi yang dilakukan pada poin sebelumnya.

## Django UserCreationForm:
UserCreationForm adalah form kelas bawaan Django yang digunakan untuk mengatur registrasi pengguna baru. Form ini berisi validasi untuk field seperti username, password1 (untuk password), dan password2 (untuk konfirmasi password).

1. Kelebihan:
    1. Mudah digunakan karena sudah disediakan oleh Django.
    2. Memiliki validasi bawaan untuk kolom-kolom yang umum digunakan dalam pendaftaran.
    3. Memudahkan pembuatan halaman registrasi dengan cepat.

2. Kekurangan:
    1. Tidak fleksibel untuk kebutuhan khusus. Jika Anda membutuhkan field tambahan atau validasi kustom, Anda mungkin harus memperluas atau menggantinya.
    2. Mungkin terlalu sederhana untuk aplikasi dengan kebutuhan pendaftaran yang kompleks.

## Perbedaan Autentikasi dan Otorisasi dalam konteks Django:
1. Autentikasi
    1. Autentikasi adalah proses validasi atau pembuktian terhadap identitas atau kredensial yang hendak memasuki sebuah sistem.
    2. Komponen Django: Django menyediakan modul django.contrib.auth yang memiliki sistem autentikasi bawaan. Modul ini menyertakan views, forms, dan models yang membantu dalam proses autentikasi, seperti login, logout, dan pendaftaran pengguna.

2. Otorisasi
    1. Otorisasi adalah proses menentukan apakah pengguna saat ini diperbolehkan untuk melakukan tugas tertentu atau tidak. Di Django, otorisasi seringkali dikelola melalui sistem perizinan (permissions) dan grup.
    2. Komponen Django: Django juga menyediakan sistem perizinan (permissions) yang memungkinkan pengembang untuk mendefinisikan izin khusus pada objek (misalnya, apakah pengguna tertentu dapat mengedit objek tertentu) atau tindakan (seperti menambah, mengubah, atau menghapus). Selain itu, dengan model Group, Django memungkinkan pengelompokan izin bersama-sama, memudahkan pemberian izin berbasis peran.

3. Pentingnya: 
    1.  Sistem yang memiliki autentikasi dan otorisasi yang baik dapat mencegah akses yang tidak sah dan memastikan bahwa data dan fungsi penting dilindungi dari pengguna yang tidak berwenang.
    2. Dengan mengetahui siapa pengguna dan apa perannya, aplikasi dapat menyesuaikan konten, UI, dan fungsionalitas yang disajikan kepada pengguna, memberikan pengalaman yang lebih relevan dan disesuaikan.
    3. Dalam organisasi atau aplikasi yang besar, tidak semua pengguna harus memiliki akses ke semua fitur. Otorisasi memungkinkan pemisahan tanggung jawab dengan memberikan akses hanya kepada mereka yang membutuhkannya.
    4. Dengan sistem autentikasi, aktivitas pengguna dapat dilacak, memungkinkan kemungkinan audit atau penyelidikan jika diperlukan. 

## Cookies dalam konteks aplikasi web:

1. Cookies adalah potongan data kecil yang disimpan di browser pengguna oleh situs web. Cookies sering digunakan untuk menyimpan informasi sementara, seperti ID sesi, preferensi, dan lainnya.

2. Penggunaan oleh Django: Django menggunakan cookies, khususnya cookie dengan nama sessionid, untuk mengidentifikasi sesi pengguna. Ketika pengguna terautentikasi, ID sesi disimpan dalam cookie, yang kemudian digunakan untuk mengidentifikasi pengguna saat melakukan login kembali ke server atau berpindah antar halaman.

## Keamanan Cookies dalam pengembangan web:

1. Risiko:
   1. Session Hijacking:
        1. Jika cookie, khususnya yang mengandung ID sesi, disadap atau dicuri oleh pihak ketiga, mereka dapat menggunakan informasi ini untuk mengambil alih sesi pengguna dan berpura-pura sebagai pengguna tersebut.

    2. Cross-Site Scripting (XSS):
        1. Jika situs rentan terhadap serangan XSS, penyerang dapat mengeksekusi skrip yang mencuri cookies dari pengguna.

    3. Cross-Site Request Forgery (CSRF):
        1. Penyerang dapat memanipulasi pengguna untuk melakukan tindakan yang tidak disengaja pada suatu situs web tanpa pengetahuan mereka, terkadang memanfaatkan cookies yang ada dalam browser pengguna.

    4. Cookie Theft via Physical Access:
        1. Jika seseorang mendapatkan akses fisik ke komputer pengguna, mereka mungkin dapat membaca cookies yang tersimpan.


# Tugas 5

## Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.

1. Masuk ke file yang ingin anda percantik, disini saya akan mempercantik file `login.html` terlebih dahulu
2. Lalu berikan `id / class` pada fungsi yang akan anda ubah, hal ini bertujuan untuk mempermudah dalam editing
3. Setelah memberikan `id / class` sesuai dengan yang anda inginkan, lalu mulai edit dengan membuat tag `<style>...</style>`
4. Lalu buat css untuk mengedit fungsi yang anda inginkan didalam tag `<style>...</style>`
5. Beginilah css yang ada di file `login.html` saya
```html
<style>
    body {
        background-image: url("https://free4kwallpapers.com/uploads/originals/2015/10/22/sunset-anime-wallpaper.jpg");
        background-size: 100% 100%;
        background-repeat: no-repeat;
        background-attachment: fixed;
        font-family: Arial, sans-serif;
    }

    .login-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        max-width: 100%;
    }

    .login {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 5px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
        text-align: center;
        padding: 30px;
        width: 300px;
    }

    .login h1 {
        color: #333;
        font-size: 24px;
        margin-bottom: 20px;
    }

    .form-group {
        margin-bottom: 20px;
        margin-left: auto;
        margin-right: 15px;
        text-align: left;
    }

    .form-group label {
        display: block;
        font-weight: bold;
        margin-bottom: 5px;
        color: #555;
    }

    .form-group input{
            justify-content: center;
            height: 20px;
            margin: 0;
            border-radius: 5px;
            border: 1px solid #fff;
            padding: 7px;
    }

    .form-control {
        width: 100%;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    .btn.login_btn {
        background-color: #007bff;
        color: #fff;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        font-weight: bold;
        margin: 0 auto;
        display: block;
    }

    .btn.login_btn:hover {
        background-color: #0056b3;
    }

    .message-list {
        list-style: none;
        padding: 0;
        margin-top: 20px;
    }

    .message-list li {
        color: red;
        font-size: 14px;
        margin: 5px 0;
    }

    .register-link {
        margin-top: 20px;
        font-size: 14px;
    }

    .register-link a {
        color: #007bff;
        text-decoration: none;
    }

    .register-link a:hover {
        text-decoration: underline;
    }
</style>
```

jadi pada kode di bawah ini, berfungsi untuk mengubah background dengan memasukan gambar yang diinginkan, serta mengatur background agar sesuai dengan layar
```html 
<style>
body {
        background-image: url("https://free4kwallpapers.com/uploads/originals/2015/10/22/sunset-anime-wallpaper.jpg");
        background-size: 100% 100%;
        background-repeat: no-repeat;
        background-attachment: fixed;
        font-family: Arial, sans-serif;
    }
```
pada kode di bawah ini, berfungsi untuk membuat sebuah container yang mengandung beberapa fungsi seperti label username, password, button login dan lain lain
```html
<style>
.login-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        max-width: 100%;
    }

    .login {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 5px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
        text-align: center;
        padding: 30px;
        width: 300px;
    }

    .login h1 {
        color: #333;
        font-size: 24px;
        margin-bottom: 20px;
    }

    .form-group {
        margin-bottom: 20px;
        margin-left: auto;
        margin-right: 15px;
        text-align: left;
    }

    .form-group label {
        display: block;
        font-weight: bold;
        margin-bottom: 5px;
        color: #555;
    }

    .form-group input{
            justify-content: center;
            height: 20px;
            margin: 0;
            border-radius: 5px;
            border: 1px solid #fff;
            padding: 7px;
    }

    .form-control {
        width: 100%;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
        .btn.login_btn {
        background-color: #007bff;
        color: #fff;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        font-weight: bold;
        margin: 0 auto;
        display: block;
    }

    .btn.login_btn:hover {
        background-color: #0056b3;
    }
    }
```
pada kode di bawah ini, berfungsi untuk menampilkan message yang sudah diinput sebelumnya , dan membuat hyperlink untuk mengarahkan ke laman register
```html
<style>
    .message-list {
        list-style: none;
        padding: 0;
        margin-top: 20px;
    }

    .message-list li {
        color: red;
        font-size: 14px;
        margin: 5px 0;
    }

    .register-link {
        margin-top: 20px;
        font-size: 14px;
    }

    .register-link a {
        color: #007bff;
        text-decoration: none;
    }

    .register-link a:hover {
        text-decoration: underline;
    }
```

6. Mengedit bagian `register.html`, setelah memberikan `id / class` sesuai yang diingginkan
7. Lalu edit sesuai selera, seperti kode di bawah ini, dimana kode di bawah ini berfungsi pada button back dan vutton register
```html
<style>
    .back-button {
    display: inline-block;
    text-align: center;
    width: 80%;
    background-color: #007BFF;
    color: #fff;
    padding: 10px 15px;
    border-radius: 4px;
    cursor: pointer;
    margin-left: 10px;  /* Penambahan margin di sebelah kiri untuk memberi jarak */
    text-decoration: none;
    }

    .back-button:hover {
        background-color: #0056b3;
    }
```

Lalu pada kode di bawah inim berfungsi untuk mengedit bagian background, form register, tabel, dah h1
```html
<style>
body {
        background-image: url("https://free4kwallpapers.com/uploads/originals/2022/03/28/anime-landscape-for-desktop-sea-ships-colorful-clouds-scenic-tree-horizon-wallpaper.jpg");
        background-size: 100% 100%;
        background-repeat: no-repeat;
        background-attachment: fixed;
        font-family: Arial, sans-serif;
    }

    .register {
        max-width: 100%;
        margin: auto auto;
        padding: 20px;
        box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 8px;
    }

    h1 {
        text-align: center;
        margin-bottom: 20px;
        color: #333;
    }

    table {
        width: 100%;
    }

    td {
        padding: 8px 0;
    }
```

Pada kode di bawah ini berguna untuk mengatur input username, password, dan confirm password, serta untuk mengatur message error yang ada
```html
<style>
    input[type="text"], input[type="password"] {
        width: 100%;
        padding: 10px;
        margin-bottom: 10px; /* Ubah margin menjadi margin-bottom */
        border: 1px solid #ccc;
        border-radius: 4px;
    }

    input[type="submit"] {
        background-color: #007BFF;
        color: #fff;
        padding: 10px 15px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        width: 100%;
    }

    input[type="submit"]:hover {
        background-color: #0056b3;
    }

    ul {
        list-style-type: none;
        padding-left: 0;
        margin: 0;
        text-align: center;
    }

    li {
        color: black;
        border-radius: 4px;
        padding: 5px 10px;
        margin-bottom: 10px; 
    }
```

8. Mengedit bagian `create_product.html`, setelah memberikan `id / class` sesuai yang diingginkan
9. Lalu edit sesuai selera, seperti kode di bawah ini, dimana kode di bawah ini berfungsi untuk mempercantik button back dan button add product serta mengubah background
```html
<style>
    body {
        background-image: url("https://free4kwallpapers.com/uploads/wallpaper/yesterday-wallpaper-1920x1080-wallpaper.jpg");
        background-size: 100% 100%;
        background-repeat: no-repeat;
        background-attachment: fixed;
        font-family: Arial, sans-serif;
    }

    #add{
        background: linear-gradient(4deg, #F94C10 6%, #F8DE22 99%);
        color: white;
        font-weight: bold;
        border: 2px solid #25316D;
        border-radius: 10px;
        cursor: pointer;
        padding: 10px 10px;
        
    }

    #back{
        background: linear-gradient(4deg, #F94C10 6%, #F8DE22 99%);
        color: white;
        font-weight: bold;
        border: 2px solid #25316D;
        border-radius: 10px;
        cursor: pointer;
        padding: 10px 10px;
        position: absolute;
        top: 10px; /* Atur posisi vertikal */
        left: 10px;
    }

    h1{
        text-align: center;
    }
```

## Kustomisasi halaman daftar inventori menjadi lebih berwarna

1. bukalah file `main.html` untuk mengedit bagian tersebut, setelah memberikan `id / class` sesuai yang diingginkan
2. Lalu edit sesuai selera, seperti kode di bawah ini, dimana kode di bawah ini berfungsi untuk membuat dan memperindah bagian button back, button add product, button decrease, increase, edit serta delete stock, dan pada kode ini berfungsi untuk mempercantik bagian background, tabel, posisi penulisan last logout dan informasi terkait nama user
```html
<style>
    <style>
            body {
                background-image: url("https://free4kwallpapers.com/uploads/originals/2022/03/28/anime-landscape-for-desktop-anime-garden-sunshine-flowers-wallpaper.jpg");
                background-size: 100% 100%;
                background-repeat: no-repeat;
                background-attachment: fixed;
                font-family: Arial, sans-serif;
            }
            
            #buttonAdd {
                border-width: 2px; 
                padding: 5px;
                border-radius: 50px;
                border-style:groove;
            }

            table{
                background-color: rgba(255, 255, 255, 0.8);
                max-width: 100%;
            }

            #add {
                    background: linear-gradient(4deg, #F94C10 6%, #F8DE22 99%);
                    color: white;
                    font-weight: bold;
                    border: 2px solid #25316D;
                    border-radius: 10px;
                    cursor: pointer;
                    padding: 10px 10px;
            }

            #addbtn {
                width:100% ;
                background: linear-gradient(4deg, #F94C10 6%, #F8DE22 99%);
                color: white;
                font-weight: bold;
                border: 2px solid #25316D;
                border-radius: 10px;
                cursor: pointer;
                padding: 10px 10px;
                display: block
            }
            
            #logout{
                    background: linear-gradient(4deg, #F94C10 6%, #F8DE22 99%);
                    color: white;
                    font-weight: bold;
                    border: 2px solid #25316D;
                    border-radius: 10px;
                    cursor: pointer;
                    padding: 10px 10px;
                    margin-top: 10px; 
                    display: block;
            }

            #intro{
                color :greenyellow;
            }

            #log{
                color:whitesmoke;
                position: absolute;
                top: 10px; /* Atur posisi vertikal */
                right: 10px;
            }
```
## Manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

1. `Element Selector`, merupakan selector yang berfungsi untuk memilih elemen HTML berdasarkan nama dari elemen yang di pilih. 
   1. `Element selector` cocok digunakan untuk mengaplikasikan style CSS pada semua elemen dengan tag yang sama. Sebagai contoh p untuk memilih semua paragraf dalam HTML:
   
```html
<style>
p {
  text-align: center;
  color: red;
}
```

2. `Class Selector`, merupakan selector yang berfungsi untuk memilih elemen HTML berdasarkan atribut class yang di select.
   1. `Class selector` cocok digunakan untuk mengaplikasikan style pada elemen yang memiliki karakteristik yang sama dan cocok untuk dikelompokkan dalam kelompok tertentu. Sebagai contoh, semua elemen dengan class="center" akan di select untuk dibuat menjadi center dan diwarnai merah:

```html
<style>
.center {
  text-align: center;
  color: red;
}
```

3. `ID Selector`, merupakan selector yang berfungsi untuk memilih elemen HTML berdasarkan atribut ID yang didefinisikan. 
   1. `ID selector` cocok digunakan untuk ketika ingin mengaplikasikan style khusus pada satu elemen tertentu dalam HTML. Hal ini karena ID merupakan elemen yang unik dan ID selector digunakan untuk satu elemen khusus. Contoh jika ingin mengaplikasikan dalam elemen dengan id="para1":

```html
<style>
#para1 {
  text-align: center;
  color: red;
}
```

4. `Attribute Selector`, merupakan selector yang berfungsi untuk memilih elemen HTML berdasarkan atribut spesifik yang dipilih.
   1. `Attribute selector` cocok digunakan ketika ingin mengaplikasikan style atau pada elemen-elemen yang memiliki atribut tertentu. Sebagai contoh, jika ingin mengaplikasikan dalam elemen dengan atribut draggable="true":

```html
<style>
p[draggable] {
    color: red;
}
```

5. `Universal Selector`, merupakan selector yang berfungsi untuk memilih semua elemen HTML dalam halaman.
   1. `Universal selector` cocok digunakan ketika ingin mengaplikasikan style untuk keseluruhan elemen HTML dalam halaman. Sebagai contoh kita ingin mengubah seluruh text menjadi center aligned dan berwarna biru:

```html
<style>
* {
  text-align: center;
  color: blue;
}
```

Sumber : [CSS Selectors](https://www.w3schools.com/css/css_selectors.asp#:~:text=CSS%20selectors%20are%20used%20to,a%20specific%20relationship%20between%20them)

## HTML5 Tag

1. `<a>`: Tag ini digunakan untuk membuat hyperlink, yang menghubungkan satu halaman ke halaman lain, atau ke sumber daya lain, seperti email atau file. Atribut 'href' digunakan untuk menentukan URL tujuan.

2. `<abbr>`: Tag ini digunakan untuk menandai singkatan atau akronim. Atribut 'title' dapat digunakan untuk memberikan penjelasan lengkap dari singkatan tersebut.

3.` <br>`: Tag 'break line'. Digunakan untuk memasukkan jeda baris dalam teks.

4. `<body>`: Tag ini mendefinisikan isi dari dokumen HTML. Semua konten yang ditampilkan di browser (teks, gambar, video, dll) berada di dalam tag `<body>`.

5. `<button>`: Digunakan untuk membuat tombol yang dapat diklik. Biasanya digunakan dalam formulir atau untuk trigger JavaScript.

6. `<center>` (Tidak disarankan untuk digunakan): Tag ini digunakan untuk menyelaraskan konten ke tengah. Namun, penggunaannya sudah dianggap usang dan sebaiknya gunakan CSS untuk penyelarasan.

7. `<div>`: Tag 'division'. Digunakan sebagai wadah untuk konten lain dan sering digunakan bersama dengan CSS untuk styling dan layout.

8. `<font>` (Tidak disarankan untuk digunakan): Digunakan untuk mendefinisikan warna, ukuran, dan jenis huruf teks. Namun, penggunaannya sudah dianggap usang dan sebaiknya gunakan CSS untuk styling teks.

9. `<footer>`: Digunakan untuk mendefinisikan footer dari sebuah dokumen atau section. Biasanya berisi informasi hak cipta, link ke kebijakan privasi, dll.

10. `<header>`: Digunakan untuk mendefinisikan header dari sebuah dokumen atau section. Bisa berisi judul, logo, navigasi, dll.

11. `<head>`: Tag ini mengandung informasi meta tentang dokumen, seperti judul, link ke CSS, JavaScript, dll. Ini bukan bagian dari konten yang ditampilkan kepada pengguna.

12. `<h1>` sampai `<h6>`: Ini adalah tag heading (judul). `<h1>` adalah judul utama dan paling penting, dan level kepentingannya menurun hingga `<h6>`.

13. `<hr>`: 'Horizontal rule'. Digunakan untuk memasukkan garis horizontal untuk pemisah konten.

14. `<li>`: 'List item'. Digunakan di dalam list (`<ul>` atau `<ol>`) untuk mendefinisikan setiap itemnya.

15. `<ol>`: 'Ordered list'. Digunakan untuk membuat daftar berurutan, dimana setiap item diawali dengan angka.

16. `<style>`: Digunakan untuk menambahkan styling CSS di dalam dokumen HTML.

17. `<table>`: Tag ini digunakan untuk membuat sebuah tabel. Tabel adalah cara untuk menyajikan data dalam format kolom dan baris.

18. `<td>`: 'Table data'. Tag ini mendefinisikan sebuah sel data dalam tabel. Biasanya berada di dalam sebuah baris tabel (<tr>).

19. `<th>`: 'Table header'. Digunakan untuk mendefinisikan sel header dalam tabel, yang biasanya mengandung judul untuk kolom atau baris. Secara default, teks di dalam `<th>` ditebalkan dan diselaraskan ke tengah.

20. `<tr>`: 'Table row'. Digunakan untuk mendefinisikan baris dalam tabel. Sebuah baris tabel biasanya mengandung beberapa sel data (`<td>`) atau sel header `<th>`

21. `<ul>`: 'Unordered list'. Digunakan untuk membuat daftar yang tidak berurutan, di mana setiap item biasanya ditandai dengan bullet. Setiap item dalam daftar ini ditandai dengan tag `<li>`.

## Perbedaan antara Margin dan Padding:

1. Margin: Mengatur ruang di luar batas elemen. Ini adalah jarak antara elemen dengan elemen lain di sekitarnya.
2. Padding: Jarak antara konten elemen dan border elemen tersebut.

## Perbedaan antara Framework CSS Tailwind dan Bootstrap:

1. Bootstrap:
    1. Bootstrap adalah framework yang mengkombinasikan HTML, CSS, dan JS. Ia menyediakan komponen UI yang telah dirancang sebelumnya.
    2. Memiliki basis pengguna yang besar dan banyak sumber belajar.
    3. Tendensinya lebih berat karena mencakup berbagai komponen dan gaya.
    4. Biasanya, Bootstrap lebih mudah untuk pemula karena komponen-komponennya lebih mudah dipahami.

2. Tailwind:
    1. Tailwind adalah framework utilitas pertama yang memungkinkan Anda membuat desain dengan menambahkan kelas utilitas ke elemen.
    2. Memungkinkan kontrol yang lebih besar atas desain tetapi memerlukan pemahaman yang lebih baik tentang CSS.
    3. Lebih ringan karena Anda hanya memuat gaya yang Anda butuhkan.
    4. Memiliki kurva belajar yang sedikit lebih tinggi tetapi sangat fleksibel.
   
3. Kapan menggunakan Bootstrap daripada Tailwind:
    1. Saat Anda ingin mempercepat proses dengan menggunakan komponen yang sudah jadi.
    2. Saat Anda lebih familiar dengan Bootstrap atau bekerja dengan tim yang sudah menggunakan Bootstrap.
    3. Saat Anda membuat prototipe dengan cepat.
   
4. Kapan menggunakan Tailwind daripada Bootstrap:
   1. Saat Anda ingin kontrol penuh atas desain dan tidak keberatan membangun dari awal.
   2. Saat Anda menginginkan pendekatan utilitas-first yang memungkinkan fleksibilitas lebih.
   3. Saat Anda mencari pendekatan yang lebih modular dan ringan.