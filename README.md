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

1.   
### Nomor 2.

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
