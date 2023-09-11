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

<!-- Links -->
[link-adaptable]: https://bujaohardware.adaptable.app/main
