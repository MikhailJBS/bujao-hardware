# **Link App Tugas: [bujaohardware.adaptable.app][link-adaptable]**

# Tugas 2 PBP 2023/2024
* Nama: Mikhail Haritz
* NPM: 2206082764
* Kelas: PBP-F

## Tautan Adaptable
* Link: [mikhail-haritz-tugas.pbp.cs.ui.ac.id][link-app]

## Pertanyaan Tugas
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
 
4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

## Jawaban Tugas
### Nomor 1.
Berikut adalah langkah-langkah saya mengimplementasikan checklist tugas:

1. Pertama-tama saya membuat direktori baru dengan nama aplikasi saya yakni `bujao_hardware`. Disana saya membuat virtual environment python terlebih dahulu dan menginstall beberapa dependencies yang saya butuhkan. Dependencies ini di-list dalam `requirements.txt`, setelah instalasi selesai, saya membuat project django baru bernama bujao_hardware dengan menjalankan perintah

```bash
> django-admin startproject shopping_list .
```
Setelah itu saya menambahkan `*` pada `ALLOWED_HOSTS` di `settings.py` untuk mendaftarkan **semua host** agar bisa mengakses aplikasi tsb

2. Saya membuat aplikasi `main` dengan menjalankan perintah

```bash
> python manage.py startapp main
```
Dan perintah ini akan membentuk direktori baru bernama `main` yang merupakan direktori aplikasi main.

3. Saya mendaftarkan aplikasi `main` ke dalam proyek dengan cara menambahkan nama aplikasi yang diinginkan, dalam kasus ini `main` kepada variabel `INSTALLED_APPS` dalam `settings.py` yang ada di dalam direktori `bujao_Hardware` agar proyek dapat menjalankan aplikasi `main`

4. Setelah itu saya beralih untuk membuat model pada aplikasi `main` dengan nama `Item` dan memiliki beberapa atribut seperti: `name` dengan tipe `CharField`, `amount` dengan tipe `IntegerField`, `description` dengan tipe `TextField`, `price` dengan tipe `IntegerField`, dan `tier` dengan tipe `TextField`. Dengan itu, model `Item` akan mempunyai semua atribut itu dengan tipe data yang telah ditentukan.

5. Saya membuat fungsi pada `views.py` yang bernama `show_main` yang berfungsi untuk mengembalikan konten di dalamnya (pada kasus ini, nama dan kelas saya) ke dalam sebuah tempalte HTML.

6. Selanjutnya saya membuat file `urls.py` dalam direktori `main` yang berisi `app_name` untuk nama aplikasi `main` dan mengutilisasi fungsi `show_main` dari modul `main.views` sebagai tampilan ketika URL diakses dengan cara menambahkan path URL sesuai yang saya tambahkan tadi yakni,

```bash
path('main/', include('main.urls')),
```
Ke dalam variabel `urlpatterns` di file `urls.py` dalam direktori proyek. Dengan ini saya berhasil routing rute URL proyek ke main, path URL `'main/` akan dialihkan ke rute yang ada dalam berkas `urls.py` di main

7.  Setelah melakukan pengetesan dan pengecekan akhir untuk melihat apakah tampilan `localhost/main` sesuai harapan, saya melakukan push direktori lokal proyek `bujao_Hardware` ke repository github dengan nama yang sama. Setelah itu saya membuat aplikasi baru di `Adaptable` dan memilih branch `main` dari repository `bujao-hardware` sebagai repository app nya. Saya melakukan beberapa pengaturan seperti memilih deploy template `Python App Template` dan database type `PostgreSQL`. Selain itu saya mengatur versi `python` ke 3.10 dan menuliskan start command sebagai berikut,

```bash
python manage.py migrate && gunicorn bujao_Hardware.wsgi
```
Setelah semua proses itu selesai, saya deploy proyek saya dengan tautan [bujaohardware.adaptable.app][link-adaptable]

### Nomor 2.
**Berikut adalah bagan yang telah saya buat:**

![alt text](https://i.imgur.com/Z3jN0d5.png?raw=true)

**Selanjutnya, saya akan menjelaskan keterkaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html` sesuai dengan bagan diatas.**<br>

1. Sebuah request dimulai saat sang user melakukan request dan request tersebut dikirimkan kepada `urls.py`. Setelah itu `urls.py` akan mmemilih view sesuai request di `views.py`. Selanjutnya data dari `views.py` akan diteruskan kepada `models.py` sebagai query untuk merespon data tersebut. Setelah itu `models.py` akan melakukan transaksi data yang tepat dengan database.

2. Setelah data dapat ditentukan, database akan mengirim data ke `models.py` dan ia akan mengembalikannya ke `views.py` agar dapat menentukan template HTML sesuai request diawal. Tahap selanjutnya, `views.py` akan memilih template pada `Templates` dan akan mengembalikan sebuah tampilan halaman yang user request di awal. 

3. Keterkaitan antara komponen-komponen tersebut terlihat jelas dengan satu komponen saling membantu komponen lainnya dalam menentukan data yang benar untuk nanti di tampilkan sesuai request user. Hal ini membuktikan bahwa komponen-komponen tersebut saling mendukung dan bergantung satu sama lain sehingga tidak akan berfungsi bahkan jika ada hanya satu komponen yang hilang.

### Nomor 3.
Virtual environment sangat berguna untuk mengisolasi package dan dependencies dari aplikasi guna menghindari konflik dengan versi lain yang ada pada komputer lokal. Hal ini kita lakukan demi kenyamanan dan keamanan development proyek kita untuk menghindari kendala.

Ya, kita tetap dapat membuat sebuah aplikasi web berbasis **Django** tanpa menggunakan virtual environment, tapi sebaiknya jangan. Penggunaan Virtual environment sangat dianjurkan karena alasan-alasan yang telah diberikan sebelumnya, selain itu, **Django** sendiri bahkan memiliki dukungan bawaan untuk virtual environment, dan hampir semua tutorial dan dokumentasi **Django** akan mengasumsikan penggunaannya.
### Nomor 4.
MVT, MVC, dan MVVM secara umum merupakan arsitektur software yang digunakan dalam pengembangan aplikasi untuk memisahkan logika operasi dari presentasinya, berikut adalah perbedaan dari masing-masing model itu.

1. **MVT (Model-View-Template):**

   MVT merupakan konsep yang digunakan oleh **Django**. Konsep ini sekilas serupa dengan MVC, tetapi perbedaannya adal dalam penggunaan Template yang secara khusus mengatur tampilan pada lingkungan **Django**

2. **MVC (Model-View-Controller):**

   MVC berfokus pada isolasi antara Model, View, dan Controller. Model bertanggung jawab atas data dan logika, View untuk tampilan, dan Controller untuk mengendailkan alur aplikasi.

3. **MVVM (Model-View-ViewModel):**
   
   MVVM dapat ditemukan dalam kerangka kerja pengembangan UI, terutama untuk aplikasi desktop atau mobile. MVVM menekankan pemisahan antara tampilan dan logika, hal ini memungkinkan development UI yang lebih terstruktur.

<br>
<br>
<br>
<br>
<br>
<br>

# Tugas 3 PBP 2023/2024
* Nama: Mikhail Haritz
* NPM: 2206082764
* Kelas: PBP-F

## Perbedaan antara form `POST` dan form `GET` dalam Django?
* Dalam Django `POST` dan `GET` adalah dua metode `HTTP` yang digunakan untuk mengirim dan menerima data dari browser ke server. Berikut adalah perbedaan utamanya:
1. `GET` digunakan untuk mengambil data dari server. Data dikirim melalui URL sebagai parameter query string. Metode ini umum digunakanan ketika useringin mengambil data dari server seperti contoh, misal saat user ingin mengakses tampilan halaman web atau melakukan pencarian.
2. `POST` digunakan untuk mengirim data ke server. Data dikirim dalam bentuk permintaan HTTP yang tidak terlihat dalam URL. Metode ini umumnya digunakan ketika user inign mengirim data atau mengubah data pada server, seperti mengirimkan form atau register user baru.

## Perbedaan utama antara `XML`, `JSON`, dan `HTML` dalam konteks pengiriman data?
* `XML` (eXtensible Markup Language), `JSON` (JavaScript Object Notation), dan `HTML` (HyperText Markup Language) adalah tiga format yang sering kita jumpai pada pengembangan web. Berikut adalah penjelasan ketiganya:
1. `XML` digunakan terutama untuk pertukaran data antar sistem dan untuk mendefinisikan struktur data yang kustom dan hierarkis. `XML` biasa digunakan untuk pertukaran data atau konfigurasi
2. `JSON` adalah format pertukaran data yang ringan yang umumnya digunakan dalam pengembangan web dan aplikasi, terutama untuk mengirim data antara server dan klien.
3. `HTML` adalah bahasa markup yang digunakan untuk membuat tampilan dan struktur halaman web. `HTML` bukan sebuah format pertukaran data, melainkan untuk mengatur antarmuka pengguna web.

* Walau `HTML` sangat beda dengan dua lainnya, `XML` dan `JSON` sangat mirip fungsinya. Tetapi ada beberapa perbedaan diantara mereka. `XML` lebih cocok untuk mendefinisikan struktur data yang rumit dan hierarkis, tetapi `XML` tidak seringan `JSON` ataupun gampang dibaca sepertinya. `JSON` cocok digunakan untuk pertukaran data web dikarenakan keringanannya dan integrasinya dengan `JavaScript` yang banyak digunakan pada saat pengembangan web. Selain itu, `JSON` juga mempunyai sintaksis yang sangat mudah untuk dibaca dan sangat fleksibel dalam struktur datanya, hal ini memungkinkan perubahan data yang lebih dinamis dibandingkan `XML`

## Mengapa `JSON` sering digunakan dalam pertukaran data antara aplikasi web modern?
* Pada zaman ini, `JSON` lebih sering digunakan untuk pertukaran data antar aplikasi web modern, dan berikut ada beberapa alasan mengapa hal itu terjadi:
1. `JSON` merupakan format yang sangat ringan dan efisien, biasanya data yang direpresentasikan dalam `JSON` lebih kecil dibanding `XML` hal ini memungkinkan komunikasi cepat antara klien dan server.
2. `JSON` adalah format yang sangat mudah untuk dipahami dan diproses, dengan sintaksis nya yang sederhana, para developer tentu akan melirik format yang satu ini. Selain itu, `JSON` juga mudah diproses oleh bahasa pemrograman dan framework web.
3. `JSON` sangat kompatibel dengan `JavaScript`. Karena aplikasi web modern pada umumnya ditulis dalam `JavaScript` maka `JSON` adalah pilihan yang tepat untuk format pertukaran data dikarenakan kompatibilitasnya dengan hampir semua framework.
4. `JSON` mempunyai struktur data yang sangat fleksibel, hal ini memungkinkan developer untuk perubahan data yang lebih gampang dan dinamis dibandingkan format lainnya.
5. `JSON` juga mempunyai dukungan Cross-Platform yang berarti bahwa format ini dapat digunakan di mayoritas platform modern seperti smartphone, server, atau perangkat mobile.

## Penjelasan pengimplementasian checklist pada soal.
1. Membuat input `form`. Pertama saya membuat berkas python baru dengan nama `forms.py` di dalam direktori main dengan struktur form yang dapat menerima data item baru. Saya menamakan formnya ItemForm sesuai dengan nama model saya dan menambahkan field sesuai atribut model saya seperti ini:
```bash
class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "tier", "amount", "price", "description"]
```
2. Menambahkan fungsi pada `views.py`. Saya menambahkan fungsi fungsi berikut:
```bash
def show_main(request):
    items = Item.objects.all()

    context = {
        'name': 'Mikhail Haritz',
        'class': 'PBP F',
        'items': items
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def delete_item(request, id):
    item = Item.objects.get(pk=id)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
Sesuai namanya masing masing, fungsi fungsi tersebut berguna untuk melihat data objek yang sudah ditambahkan dalam format `HTML`, `XML`, `JSON`, `XML` by ID, dan `JSON` by ID. dan fungsi `show_main` untuk menampilkan dalam format `HTML` dengan mengubah nya menjadi tabel. Saya juga menambahkan fungsi `delete_item` untuk menghapus item berdasarkan `ID` nya

3. Terakhir saya menambahkan routing `URL` untuk setiap fungsi `views` yang telah ditambahkan seperti ini:
```bash
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('delete-item/<int:id>/', delete_item, name='delete_item'),
]
```
path `' '` untuk tampilan utama, `/create-item` untuk ke halaman form input `Item`, `/xml` untuk melihat seluruh item dalam format `XML`, `/json` untuk melihatnya dalam format `JSON`, `/json/[id]` untuk melihat data `Item` tertentu dalam format `JSON` berdasarkan `ID` nya, `/xml/[id]` untuk melihat data tsb dalam format `XML` dan `/delete-item/[id]` untuk menghapus suatu `Item` berdasarkan `ID` nya.

## Postman.
1. Main `' '`
![alt text](https://i.imgur.com/L7DnRUe.png)
2. Item Form `/create-item`
![alt text](https://i.imgur.com/QU7bDN7.png)
3. Data barang `XML` `/xml`
![alt text](https://i.imgur.com/zoC2iS5.png)
4. Data barang `JSON` `/json`
![alt text](https://i.imgur.com/IzS7TTU.png)
5. Data barang (id) `XML` `/xml/[id]`
![alt text](https://i.imgur.com/cm8Yhky.png)
6. Data barang (id) `JSON` `/json/[id]`
![alt text](https://i.imgur.com/Zn8JVFO.png)

<br>
<br>
<br>
<br>
<br>
<br>

# Tugas 4 PBP 2023/2024
* Nama: Mikhail Haritz
* NPM: 2206082764
* Kelas: PBP-F

## Django `UserCreationForm` serta kelebihan dan kekurangannya
Django UserCreationForm adalah salah satu komponen framework `Django` yang digunakan untuk pendaftaran user dalam sebuah aplikasi web. Form ini memungkinkan user untuk membuat sebuah akun dengan mengisi data seperti username, password, email dll. Berikut adalah kelebihan dan kekurangan dari Django `UserCreationForm`:
<br>
<br>
* **Kelebihan:**
1. Integrasi dengan Django `Authentication`<br>
`UserCreationForm` terintegrasi dengan sistem autentikasi bawaan Django, hal ini membuatnya mudah digunakan dengan fitur autentikasi Django
2. Penggunaan yang mudah <br>
Dengan `UserCreationForm`, pembuatan akun user baru menjadi proses yang lebih sederhana. Kita hanya perlu menambahkan formulir ini di `views` dan mengatur tindakan untuk memproses data yang dikirim oleh pengguna
3. Mudah di kustomisasi <br>
Kita dapat menyesuaikan `UserCreationForm` sesuai kebutuhan aplikasi dengan mudah, seperti contoh kita bisa menambahkan atau menghilangkan `field` atau mengubah pesan error dengan mudah.

* **Kekurangan**
1. Tampilan basic <br>
`UserCreationForm` hanya menyediakan tampilan formulir yang sangat basic. Kita harus merancang tampilan ini secara khusus jika ingin membuatnya sesuai dengan tampilan aplikasi web.
2. Kurang perlindungan terhadap serangan <br>
`UserCreationForm` secara eksplisit tidak menyertakan serangan `CSRF` (Cross-Site Request Forgery) atau bruteforce. Kita harus mengimplementasikan fitur-fitur keamanan ini secara terpisah.
3. Fitur dasar <br>
`UserCreationForm` di design untuk penggunaan ayng umum dan hanya menyediakan fitur dasar untuk mendaftarkan pengguna. Kita harus menyesuaikan formulir ini atau membangun formulir pendaftaran kuston sendiri jika butuh fitur yang lebih spesifik.

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
* **Autentikasi** <br>
Autentikasi adalah proses verifikasi identitas pengguna yang mencoba untuk mengkases aplikasi web. Dengan kredensial yang telah mereka berikan pada saat pendaftaran, proses ini memeriksa pengguna apakah mereka benar benar siapa yang mereka klaim. Sistem autentikasi bawaan Django tergolong kuat dengan kemampuan untuk mengelola autentikasi pengguna dan mengenkripsi kata sandi. Autentikasi berguna untuk memastikan bahwa hanya pengguna yang sah yang dapat mengakses data web tersebut.

* **Otorisasi** <br>
Otorisasi adalah proses menentukan izin yang dimiliki oleh user yang sudah di autentikasi. Otorisasi pada Django umumnya dikelola melalui sistem berbasis peran. Kita dapat menentukan peran dan menentukan izin setiap peran tersebut. Dengan ini, otorisasi memastikan bahaw pengguna hanya dapat mengkases data sesuai izin peran yang mereka miliki untuk melindungi data sensitif aplikasi itu sendiri

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies merupakan data kecil yang disimpan di sisi client (dalam web browser user) dan digunakan untuk menyimpan informasi yang diperlukan aplikasi web tersebut. Cookies membantu aplikasi web untuk mengidentifikasi dan mengingat sesi user ketika mereka berinterkasi. Django menggunakan cookies untuk mengelola data sesi user dengan cara berikut:
1. Django menciptakan ID sesi unik untuk setiap user yang mengakses aplikasi web untuk bisa mengidentifikasi user tersebut lebih mudah.
2. Data sesi user, informasi login, bahkan preferensi disimpan dalam server Django
3. ID setiap sesi disimpan dalam cookies di sisi klien user untuk kemudahan identifikasi user.
4. Setiap kali user mengakses halaman atau melakukan permintaan, cookie dengan ID sesi dikirimkan ke server Django.
5. Django menggunakan ID sesi untuk mengidentifikasi sesi user yang sesuai dan mengambil data sesi dari server.
6. Saat user berinteraksi dengan aplikasi, data sesi akan diperbarui di server

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies secara default aman digunakan jika diimplementasikan dengan benar, ini termasuk enkripsi data sensitif, menghindari menyimpan data sensitif dalam cookies di sisi client, dll. Tapi tetap ada beberapa risiko potensial sebagai berikut:
1. **Keamanan Data:** Cookies dapat membawa data sensitif, dan jika tidak dienkripsi, informasi ini bisa menjadi rentan terhadap pencurian atau penyalahgunaan oleh pihak yang tidak sah
2. **CSRF (Cross-Site Request Forgery):** Cookies yang digunakan untuk autentikasi dapat digunakan oleh penyerang untuk melakukan serangan CSRF, yaitu mengirimkan permintaan yang tidak diinginkan namun sah dari pengguna yang terautentikasi.
3. **Cross-Site Scripting (XSS):** Jika aplikasi web membiarkan input dari pengguna disimpan dalam cookies tanpa validasi, itu dapat memungkinkan serangan XSS di mana penyerang menyisipkan kode berbahaya dalam cookies.
4. **Pelanggaran Privasi:** Penggunaan cookies untuk melacak perilaku pengguna atau menyimpan informasi pribadi tanpa izin atau pemahaman yang jelas bisa melanggar privasi pengguna.

## Penjelasan pengimplementasian checklist pada soal.
1. Mengimplementasikan fungsi registrasi, login dan logout. Untuk fungsi registrasi saya membuat file html baru bernama `register.html` sebagai template form registrasi sebagai berikut:
```
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
Dimana dia akan menampilkan form registrasi sesuai template Django dengan meminta username, password dan verifikasi password yang sama. Setelah itu saya import beberapa hal yang dibutuhkan dari Django untuk membuat fungsi login, registrasi dan logout. Setelah itu saya membuat function untuk registrasi seperti berikut:
```
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
Dan menyambungkannya dengan html register sebelumnya. Setelah itu saya mengimport fungsi tersebut ke `urls.py` dan merouting path url untuk fungsi tersebut.

Selanjutnya ada fungsi login. Saya membuat file html bernama `login.html` sebagai template login page saya, dan saya membuat function baru di `views.py` sebagai berikut:
```
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```
Setelah itu saya menyambungkannya dengan `login.html` tadi, dan saya melakukan routing dengan mengimport function ini ke `urls.py` dan menambahkan path url nya. Pada fungsi itu saya menggunakan cookies untuk mendapatkan data last_login agar user bisa melanjutkan session loginnya walau web sudah di tutup. Saya juga mengubah function `show_main` agar dia tidak bisa ke halaman utama sebelum ada yang login seperti ini:
```
@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'class': 'PBP F',
        'items': items,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)
```

Terakhir ada function logout, function ini berguna untuk logout dari akun pada web tersebut. Fungsi tersebut terlihat seperti:
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
Dia akan delete cookies last_login setelah logout, dan akan keluar dari web aplikasi dengan fitur Django. Seperti biasa saya melakukan routing url untuk logout di `urls.py` dan setelah itu merouting url nya ke sebuah button pada `main.html`.
<br>
<br>

2. Membuat dua akun pengguna dengan masing masing tiga dummy data menggunakan model yang telah dibuat untuk setiap akun di lokal. Pertama, saya mengubah function `create_item` agar dia hanya membuat item untuk satu user saja yakni user yang login saat itu seperti ini:
```
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
```
Setelah itu saya mengubah model saya agar dia mempunyai atribut user dengan `ForeignKey` user yang sedang login saat itu untuk memunculkan bahwa item itu ada untuk user itu. Dengan melakukan hal hal tadi, kita bisa mempunyai inventory yang berbeda untuk setiap akun yang ada di aplikasi web tersebut seperti ini:

**AKUN 1** <br>
![alt text](https://i.imgur.com/oOe3p3R.png) <br>
Akun JBS dengan item yang berbeda dari akun Mikhail

**AKUN 2** <br>
![alt text](https://i.imgur.com/ImZTZZp.png) <br>
Akun Mikhail dengan item yang berbeda dari akun JBS

3. Menhubungkan model `Item` dengan `User`. Hal ini dilakukan agar setiap user mempunyai kumpulan item yang berbeda satu sama lain, hal ini dilakukan dengan cara mengubah kode `models.py` menjadi seperti:
```
from django.contrib.auth.models import User

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    tier = models.CharField(max_length=255)
    price = models.IntegerField()
    amount = models.IntegerField()
    description = models.TextField()
```

4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menggunakan `cookies` seperti `last login`. Setelah mengimplementasikan `cookies` seperti `last login` pada fungsi sebelumnya di `views.py` seperti pada poin 1 diatas, saya menampilkan detail informasi pengguna yang sedang logged in pada main page aplikasi dengan cara mengubah fungsi show main dengan menambahkan variabel `last_login` yang berisi `cookies` akun `last_login` tsb, hal ini akan memunculkan nama dan data dengan lengkap. Pada `main.html` juga dibagian paling bawah saya menambahkan paragraph untuk menunjukan detail last login seperti ini:
<br>

![alt text](https://i.imgur.com/ImZTZZp.png) <br>
Dapat kita lihat bahwa pada bagian paling bawah terlihat kapan akun dengan nama Mikhail terakhir login pada aplikasi web ini. Dan dibawah nama juga terlihat nama akun yang `last_login` jadi tidak perlu login ulang lagi sampai kita logout manual, hal ini bisa dilakukan dengan mengutiliasai `cookies` `last_login` pada aplikasi web ini.

<br>
<br>
<br>
<br>
<br>
<br>

# Tugas 5 PBP 2023/2024
* Nama: Mikhail Haritz
* NPM: 2206082764
* Kelas: PBP-F

## Manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
Element selector dalam CSS digunakan untuk memilih elemen-elemen HTML tertentu yang ingin diatur tampilannya. Berikut adalah beberapa element selector umum digunakan:
<br>
<br>
1. Selector Universal `*`<br>
Fungsi dari selector ini adalah untuk memilih semua elemen di halaman. Biasanya digunakan untuk memberikan gaya dasar, tetapi sebaiknya digunakan dengan bijak karena dapat memengaruhi kode.

2. Selector Tag `<p>`, `<h1>`,`<div>`<br>
Memilih semua elemen dengan tag HTML tertentu. Cocok digunakan untuk mengatur gaya dasar elemen-elemen HTML. Umum digunakan secara luas dalam pembuatan tata letak.

3. Selector Class `.classname` <br>
Digunakan untuk memilih elemen-elemen dengan kelas tertentu. Digunakan untuk menggabungkan elemen-elemen yang memiliki fungsi atau styling yang sama. Cocok untuk menyusun gaya khusus bagi elemen dengan kelas tertentu.

4. Selector ID `#idname` <br>
Digunakan untuk memilih elemen dengan ID tertentu. Cocok untuk mengatur gaya khusus untuk elemen dengan ID tertentu. Umumnya digunakan untuk menerapkan styling atau perilaku JavaScript khusus pada elemen tersebut.

5. Selector Pseudo-class `:pseudo-class` <br>
Memilih elemen berdasarkan keadaan atau interaksi pengguna, seperti `:hover`, `:active`, `:focus`, dll. Biasanya digunakan untuk mengatur gaya khusus untuk elemen yang sedang diinteraksikan oleh pengguna.

3. Selector Pseudo-element `::pseudo-element` <br>
Memilih bagian khusus dari elemen, seperti `::before`, `::after`, `::first-line`, dll. Digunakan untuk mengatur gaya khusus untuk bagian-bagian elemen tertentu.

7. Selector Kombinasi <br>
Memilih elemen berdasarkan hubungan atau konteks mereka dalam dokumen, seperti `element1 element2`, `element1 > element2`, `element1 + element2`, dll. Digunakan untuk menargetkan elemen-elemen yang memiliki hubungan tertentu dalam tata letak halaman.

8. Selector Atribut `[attribute]`, `[attribute=value]`, `[attribute~=value]`, dll. <br>
Memilih elemen berdasarkan atribut HTML mereka. Digunakan untuk menargetkan elemen-elemen yang memiliki atribut tertentu atau nilai atribut tertentu.

## HTML5 Tag
HTML5 adalah versi terbaru dari HTML yang mendukung fitur-fitur baru untuk memperluas kemampuan bahasa HTML dan memberikan struktur yang lebih baik untuk menggambarkan konten web. Berikut adalah beberapa tag HTML5 yang sering digunakan:
<br>
<br>
1. `<header>` <br>
Tag ini digunakan untuk menunjukkan bagian header dari halaman web. Biasanya berisi judul, logo, dan navigasi utama. Tag ini biasanya digunakan di bagian atas halaman web.

2. `<nav>` <br>
Tag ini digunakan untuk menunjukkan bagian navigasi dari halaman web. Biasanya berisi tautan ke halaman lain di situs web. Tag ini biasanya digunakan di bagian atas halaman web.

3. `<section>` <br>
Tag ini digunakan untuk menunjukkan bagian utama dari halaman web. Biasanya berisi konten utama dari halaman web. Tag ini biasanya digunakan di bagian tengah halaman web.

4. `<article>` <br>
Tag ini digunakan untuk menunjukkan bagian artikel dari halaman web. Biasanya berisi konten yang berdiri sendiri, seperti posting blog, artikel berita, dll. Tag ini biasanya digunakan di bagian tengah halaman web.

5. `<aside>` <br>
Tag ini digunakan untuk menunjukkan bagian samping dari halaman web. Biasanya berisi konten yang terkait dengan konten utama, seperti daftar tautan, iklan, dll. Tag ini biasanya digunakan di bagian samping halaman web.

6. `<footer>` <br>
Tag ini digunakan untuk menunjukkan bagian footer dari halaman web. Biasanya berisi informasi kontak, tautan ke halaman lain, dll. Tag ini biasanya digunakan di bagian bawah halaman web.

7. `<video>` <br>
Tag ini digunakan untuk menampilkan video di halaman web. Tag ini biasanya digunakan untuk menampilkan video yang terkait dengan konten halaman web.

8. `<audio>` <br>
Tag ini digunakan untuk menampilkan audio di halaman web. Tag ini biasanya digunakan untuk menampilkan audio yang terkait dengan konten halaman web.

9. `<canvas>` <br>
Tag ini digunakan untuk membuat grafik dan animasi di halaman web. Tag ini biasanya digunakan untuk membuat grafik dan animasi yang terkait dengan konten halaman web.

10. `<svg>` <br>
Tag ini digunakan untuk membuat grafik vektor di halaman web. Tag ini biasanya digunakan untuk membuat grafik vektor yang terkait dengan konten halaman web.

## Perbedaan antara margin dan padding.
* **Margin** <br>
Margin adalah ruang di luar elemen, di antara elemen dan elemen lain di sekitarnya. Margin berpengaruh pada ruang antara elemen dengan elemen tetangganya atau elemen luar terdekat. Margin biasanya digunakan untuk mengatur jarak antara elemen-elemen, membuat elemen terpisah dari elemen lain, atau mengontrol tata letak secara keseluruhan.

* **Padding** <br>
Padding adalah ruang di dalam elemen, di antara elemen dan konten di dalamnya. Padding memengaruhi tata letak elemen itu sendiri dan tidak memiliki dampak pada elemen-elemen lain di sekitarnya. Padding Biasanya digunakan untuk mengatur jarak antara konten elemen dan batas elemen tersebut, sehingga mempengaruhi tampilan dan tata letak konten dalam elemen tersebut.

## Perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
Tailwind CSS dan Bootstrap adalah dua kerangka kerja (framework) CSS yang digunakan untuk mempercepat pengembangan desain web. Mereka memiliki pendekatan dan filosofi yang berbeda, dan perbedaan utama antara keduanya adalah dalam gaya penulisan dan pendekatan penggunaan.

* **Tailwind** <br>
Tailwind CSS adalah pendekatan CSS utilitarian yang fokus pada penggunaan kelas-kelas kecil untuk menggabungkan gaya yang dibutuhkan secara langsung dalam HTML. Ini memberikan fleksibilitas tinggi tetapi memerlukan pembelajaran pola kelas yang cukup berbeda. Tailwind juga tidak menyediakan komponen UI yang siap pakai, tetapi menyediakan utilitas yang dapat digunakan untuk membuat komponen-komponen tersebut. Tailwind memungkinkan kustomisasi yang lebih dalam, tetapi memerlukan penulisan kode yang lebih banyak. Tailwind memiliki ukuran yang lebih kecil karena hanya menggunakan kelas-kelas yang diperlukan

* **Bootstrap** <br>
Bootstrap adalah kerangka kerja CSS yang lebih tradisional dengan gaya pra-didefinisi. Ini menggunakan kelas-kelas yang lebih deskriptif dan bawaan untuk mengatur tampilan elemen, ini memberikan konsistensi dan kemudahan penggunaan tetapi kurang fleksibel. Bootstrap juga menyediakan komponen-komponen UI yang siap pakai. Bootstrap memungkinkan kustomisasi, itu biasanya melibatkan penyesuaian variabel SASS atau LESS yang lebih dalam untuk mengubah warna, ukuran, dan komponen jadi tidak se flexible Tailwind. Bootstrap memiliki banyak class CSS bawaan yang menyebabkan ukurannya menjadi cenderung lebih besar dibanding Tailwind

* **Kapan menggunakan Tailwind dan kapan menggunakan Bootstrap?** <br>
<br>***Tailwind*** <br>
Tailwind cocok digunakan untuk proyek-proyek yang membutuhkan fleksibilitas tinggi dan kustomisasi yang lebih dalam. Ini juga cocok untuk proyek-proyek yang membutuhkan tampilan yang unik dan tidak biasa. <br>
<br>***Bootstrap*** <br>
Bootstrap cocok digunakan untuk proyek-proyek yang membutuhkan konsistensi dan kemudahan penggunaan. Ini juga cocok untuk proyek-proyek yang membutuhkan tampilan yang umum dan biasa.


## Penjelasan pengimplementasian checklist pada soal.
1. Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin. Pada tugas ini saya menggunakan framework CSS Bootstrap untuk kustomisasi halaman login, register, dan tambah inventori. Saya mendesain ketiga komponen tersebut agar mirip satu sama lain karena saya ingin menunjukan aspek kontinuitas dari desain web saya. Untuk membuatnya saya pertama tama menambahkan link dan script Bootstrap di `base.html`. Untuk login dan register saya menggunakan template yang sudah disediakan oleh Bootstrap, dan saya mengubahnya sedikit agar sesuai dengan kebutuhan saya. Untuk tambah inventori saya membuat template sendiri dengan menggunakan komponen Bootstrap. Untuk ketiga halaman ini saya mengedepankan aspek simplisitas dari desain web saya. Berikut adalah tampilan ketiga halaman tersebut:<br>
<br>***Login***<br>
![alt text](https://i.imgur.com/gl6aPBl.png) <br>
<br>***Register***<br>
![alt text](https://i.imgur.com/evVSFD8.png) <br>
<br>***Tambah Inventori***<br>
![alt text](https://i.imgur.com/7gnEuYb.png) <br>
<br>
<br>

2. Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan **Card**.  Saya mendesain halaman daftar inventori yang ada di `main.html` dengan menggunakan beberapa komponen Bootstrap seperti `stripped-table` dan beberapa button lain. Saya ingin membuat website yang terlihat simple tapi fungsional dengan menonjolkan beberapa fungsi penting dari website ini. Berikut adalah tampilan dari daftar inventori saya:<br>
<br>***Daftar Inventori***<br>
![alt text](https://i.imgur.com/er4JtQe.png) <br>

<br>
<br>
<br>
<br>
<br>
<br>

# Tugas 6 PBP 2023/2024
* Nama: Mikhail Haritz
* NPM: 2206082764
* Kelas: PBP-F

## Perbedaan antara Asynchronous Programming dan Synchronous Programming
* **Synchronous Programming:**<br> Pada synchronous programming, tugas-tugas dieksekusi secara berurutan, satu per satu. Setiap tugas harus menunggu tugas sebelumnya selesai sebelum dapat dijalankan. Ini berarti jika ada tugas yang memakan waktu lama, maka semua tugas berikutnya akan terhenti atau diblokir hingga tugas tersebut selesai.

* **Asynchronous Programming:**<br> Asynchronous programming merupakan sebuah pendekatan pemrograman yang tidak terikat pada input output (I/O)  protocol. Ini menandakan bahwa pemrograman asynchronous tidak melakukan pekerjaannya secara old style / cara lama yaitu dengan eksekusi baris program satu persatu secara hirarki. Artinya, tugas-tugas dapat dijalankan secara bersamaan tanpa harus menunggu tugas sebelumnya selesai. Ini sangat berguna saat ada tugas yang memerlukan waktu lama, karena tugas lainnya tetap dapat berjalan tanpa terhenti.

## Paradigma Event-Driven Programming pada JavaScript dan Contohnya dalam Tugas Ini
Paradigma event-driven programming adalah pendekatan di mana program merespon peristiwa (event) yang terjadi. Program akan menjalankan fungsi tertentu ketika suatu event terjadi. Pada tugas ini, contoh penerapannya adalah penggunaan event listeners dalam JavaScript untuk merespons event seperti tombol diklik (misalnya, saat tombol "Add Item" diklik untuk membuka modal) yang dapat kita lihat pada kode dibawah ini:

```
function addItem(){
    fetch("{% url 'main:add_item_ajax' %}", {
        method: "POST",
        body: new FormData(document.getElementById("form"))
    }).then(refreshItems)

    document.getElementById("form").reset();
    return false;
}


document.getElementById("button_add").onclick = addItem;
```

Kode diatas akan menjalankan fungsi `addItem` ketika tombol dengan id `button_add` diklik. Fungsi ini akan mengambil data dari form dengan id `form` dan mengirimkannya ke server menggunakan `fetch`. Setelah itu, fungsi `refreshItems` akan dijalankan untuk memperbarui daftar item.

## Penerapan Asynchronous Programming pada AJAX
AJAX (Asynchronous JavaScript and XML) adalah teknologi yang memanfaatkan asynchronous programming untuk melakukan komunikasi antara browser dan server tanpa harus me-refresh seluruh halaman web. Saat melakukan permintaan AJAX (misalnya, permintaan GET atau POST), browser dapat melanjutkan menjalankan kode JavaScript lainnya tanpa harus menunggu respons dari server. Ketika respons dari server tiba, callback atau promise akan dijalankan untuk menangani data tersebut. Pada tugas ini, AJAX digunakan untuk mengirimkan data ke server dan memperbarui halaman web tanpa harus me-refresh seluruh halaman web. Contoh penerapannya adalah pada kode dibawah ini:

```
function addItem(){
    fetch("{% url 'main:add_item_ajax' %}", {
        method: "POST",
        body: new FormData(document.getElementById("form"))
    }).then(refreshItems)

    document.getElementById("form").reset();
    return false;
}
```

## Bandingkan Fetch API dan jQuery untuk Penerapan AJAX
* **Fetch API** <br>
Ini adalah API bawaan JavaScript yang menyediakan cara yang kuat dan modern untuk melakukan permintaan HTTP secara asinkronus. Kelebihannya termasuk desain yang lebih modern, dukungan untuk Promise yang membuat penanganan error lebih baik, dan ringan karena tidak memerlukan dependensi tambahan. Fetch API lebih cocok untuk proyek-proyek yang lebih kecil dan ketika Anda ingin menghindari overhead dari pustaka pihak ketiga. Namun, Fetch API memiliki dukungan yang lebih rendah untuk browser lama dan tidak memiliki dukungan untuk JSONP. <br> <br>
* **Jquery** <br>
jQuery adalah pustaka JavaScript yang telah ada selama beberapa tahun dan memiliki dukungan untuk AJAX yang kuat. Kelebihannya termasuk kompatibilitas lintas-browser yang baik, sintaks yang sederhana, dan banyak plugin yang tersedia. Namun, jQuery memiliki ukuran yang lebih besar dan mungkin tidak diperlukan jika Anda hanya menggunakan fitur-fitur AJAX. jQuery lebih cocok untuk proyek-proyek yang lebih besar dan ketika Anda ingin menggunakan fitur lainnya seperti manipulasi DOM, animasi, dll. <br><br>

Pilihan antara keduanya tergantung pada kebutuhan proyek. Untuk proyek-proyek kecil atau saat Anda ingin menghindari dependensi tambahan, Fetch API bisa menjadi pilihan yang baik. Namun, jika Anda bekerja dalam lingkungan yang sudah menggunakan jQuery atau memiliki kompatibilitas lintas-browser yang penting, maka jQuery masih bisa digunakan dengan baik. Yang terpenting adalah memahami prinsip-prinsip dasar AJAX dan asynchronous programming yang digunakan di kedua teknologi ini.

## Penjelasan pengimplementasian checklist pada soal.
### **1. Ubahlah kode tabel data item agar dapat mendukung AJAX GET dan melakukan pengambilan task menggunakan AJAX GET.**
Untuk mengubah kode tabel data item agar dapat mendukung AJAX GET dan melakukan pengambilan task menggunakan AJAX GET, saya mengubah kode `main.html` dengan menghapus tabel yang telah didefinisikan sebelumnya secara synchronus, dan menggantinya dengan membuat tabel kosong dengan id `table_items` yang akan diisi dengan data dari server menggunakan AJAX pada `JavaScript`. Berikut adalah kode fungsi `refreshItems` yang akan mengambil data dari server dan memasukkannya ke dalam tabel:
```
async function getItems() {
    return fetch("{% url 'main:get_item_json' %}").then((res) => res.json())
}

async function refreshItems() {
    document.getElementById("item-table").innerHTML = ""
    const items = await getItems()
    let htmlString = `<tr>
        <th>Name</th>
        <th>Tier</th>
        <th>Price</th>
        <th>Amount</th>
        <th>Description</th>
        <th>Action</th>
    </tr>`
    items.forEach((item) => {
        htmlString += `\n<tr>
            <td>${item.fields.name}</td>
            <td>${item.fields.tier}</td>
            <td>${item.fields.price}</td>
            <td>${item.fields.amount}</td>
            <td>${item.fields.description}</td>
            <td>
                <a href="edit-item/${item.pk}">
                    <button class='btn btn-primary'>Edit</button>
                </a>
                <a href="delete-item/${item.pk}">
                    <button class='btn btn-danger'>Delete</button>
                </a>
            </td>
        </tr>`;
    })
    
    document.getElementById("item-table").innerHTML = htmlString
}
```
### **2. Penerapan AJAX Post dengan sebuah modal berisi form untuk menambahkan suatu item baru.**
Untuk penerapan AJAX Post dengan sebuah modal berisi form untuk menambahkan suatu item baru, saya membuat modal dengan id `modal_fade` yang akan muncul ketika tombol `Add Item by AJAX` diklik. Modal ini akan menampilkan form untuk menambahkan item baru dengan tampilan Pop-up seperti ini:
![alt text](https://i.imgur.com/N8LxbF5.png) <br>

Pada form modal tsb terdapat button `Add Item` yang akan mengirimkan data dari form tersebut ke server menggunakan AJAX. Berikut adalah kode fungsi `addItem` yang akan mengambil data dari form dan mengirimkannya ke server menggunakan AJAX:
```
function addItem(){
    fetch("{% url 'main:add_item_ajax' %}", {
        method: "POST",
        body: new FormData(document.getElementById("form"))
    }).then(refreshItems)

    document.getElementById("form").reset();
    return false;
}
```
Kode diatas akan mengambil data dari form dengan id `form` dan mengirimkannya ke server menggunakan `fetch`. Setelah itu, fungsi `refreshItems` akan dijalankan untuk memperbarui daftar item. Kode itu juga memanggil url `main:add_item_ajax` yang akan memanggil fungsi `add_item_ajax` pada `views.py` untuk menambahkan item baru ke database. Berikut adalah kode fungsi `add_item_ajax` yang akan menambahkan item baru ke database:
```
@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        tier = request.POST.get("tier")
        price = request.POST.get("price")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, tier=tier, price=price, amount = amount, description=description, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```
Lalu fungsi itu dihubungkan dengan url `main:add_item_ajax` pada `urls.py` dengan nama path `create-ajax/` seperti ini:
```
path('create-ajax/', add_item_ajax, name='add_item_ajax'),
```
Yang selanjutnya dihubungkan dengan button `Add Item` pada form modal seperti diatas tadi. Dengan begitu, ketika button `Add Item` diklik, data dari form akan dikirimkan ke server menggunakan AJAX dan item baru akan ditambahkan ke database. Setelah itu, daftar item akan diperbarui dengan menampilkan item baru tersebut.

### **3. Melakukan perintah `collectstatic`**
Perintah collectstatic digunakan untuk mengumpulkan semua file static yang dibutuhkan oleh aplikasi web ke satu folder. File-file tersebut nantinya akan digunakan oleh server untuk melayani permintaan dari client. Tujuan dari mengumpulkan file-file ini kedalam satu folder di root adalah agar folder yang berisi file-file tersebut dapat diakses dengan mudah. Cara melakukannya adalah dengan menjalankan perinaht `python manage.py collectstatic` pada terminal. Berikut adalah hasil dari perintah tersebut:
![alt text](https://i.imgur.com/Pr9xpVq.png) <br>

<!-- Links -->
[link-app]: mikhail-haritz-tugas.pbp.cs.ui.ac.id
