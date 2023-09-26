# Tugas 2 PBP 2023/2024
* Nama: Mikhail Haritz
* NPM: 2206082764
* Kelas: PBP-F

## Tautan Adaptable
* Link: [bujaohardware.adaptable.app][link-adaptable]

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


<!-- Links -->
[link-adaptable]: https://bujaohardware.adaptable.app/main
