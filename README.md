# Image Restoration Mini Project
## Identitas

# Khalil Gibran Al Azhar
# 5024241100


## Penjelasan Pipeline Restorasi

Proyek ini mengimplementasikan pipeline restorasi citra berwarna untuk memperbaiki kualitas gambar yang terdegradasi oleh noise, kontras rendah, dan kehilangan ketajaman. Proses dilakukan secara berurutan pada setiap channel warna (RGB) menggunakan pendekatan manual berbasis NumPy.

Tahap pertama adalah denoising menggunakan median filter dengan kernel 5x5. Setiap piksel diproses dengan mengambil window lokal di sekitarnya, kemudian nilai-nilai dalam window tersebut diurutkan untuk mendapatkan nilai median sebagai pengganti piksel pusat. Metode ini dipilih karena efektif dalam menghilangkan noise tipe salt-and-pepper sekaligus mempertahankan struktur tepi (edge) objek. Penggunaan kernel 5x5 memungkinkan pengurangan noise yang cukup padat, meskipun dengan risiko sedikit menghaluskan detail halus.

Setelah noise dikurangi, dilakukan penyesuaian kontras dan kecerahan menggunakan transformasi linear dengan parameter α = 1.2 dan β = 15. Transformasi ini bertujuan untuk meningkatkan perbedaan intensitas antar piksel sehingga detail yang sebelumnya kurang terlihat menjadi lebih jelas. Tahap ini penting karena proses denoising cenderung membuat citra terlihat lebih datar (low contrast).

Selanjutnya, Gaussian blur dengan kernel 3x3 dan sigma 1 diterapkan secara manual untuk menghasilkan versi citra yang lebih halus. Proses ini bukan bertujuan sebagai denoising utama, melainkan sebagai bagian dari metode sharpening. Citra hasil blur digunakan sebagai referensi untuk mengekstrak komponen frekuensi tinggi (detail) pada tahap berikutnya.

Tahap sharpening dilakukan menggunakan metode unsharp masking. Dalam metode ini, dibuat sebuah mask yang merupakan selisih antara citra hasil penyesuaian kontras dengan citra hasil Gaussian blur. Mask tersebut kemudian ditambahkan kembali ke citra asli dengan faktor penguat (α = 0.8). Pendekatan ini memungkinkan peningkatan ketajaman secara terkontrol, sehingga detail dan edge menjadi lebih jelas tanpa memperkuat noise secara berlebihan.

Untuk citra berwarna, seluruh proses dilakukan secara terpisah pada masing-masing channel Red, Green, dan Blue. Citra awal dibaca dalam format BGR kemudian dikonversi ke RGB sebelum dipisahkan menjadi tiga channel. Setelah masing-masing channel diproses menggunakan pipeline yang sama, ketiganya digabung kembali untuk menghasilkan citra akhir. Pendekatan ini sederhana dan efektif, meskipun dapat menyebabkan sedikit perubahan warna karena tidak mempertimbangkan hubungan antar channel.

Secara keseluruhan, urutan proses dalam pipeline ini adalah denoising menggunakan median filter, penyesuaian kontras dan kecerahan, Gaussian blur sebagai dasar sharpening, dan diakhiri dengan unsharp masking untuk meningkatkan ketajaman.

## Perbandingan visual



## Analisis Singkat

Hasil yang diperoleh menunjukkan bahwa median filter mampu mengurangi noise secara signifikan tanpa merusak struktur utama gambar. Penyesuaian kontras dan kecerahan berhasil meningkatkan visibilitas detail, sementara unsharp masking memberikan efek penajaman yang cukup natural. Kombinasi tahapan ini menghasilkan citra yang secara visual lebih bersih dan tajam dibandingkan citra awal.

Namun demikian, terdapat beberapa keterbatasan dalam implementasi ini. Penggunaan loop Python dalam proses filtering menyebabkan performa yang relatif lambat untuk citra berukuran besar. Selain itu, penyesuaian kontras masih menggunakan fungsi dari OpenCV sehingga belum sepenuhnya manual. Pendekatan pemrosesan per channel RGB juga berpotensi menyebabkan distorsi warna ringan. Untuk pengembangan lebih lanjut, metode seperti histogram equalization manual atau pemrosesan pada ruang warna lain (misalnya luminance-based) dapat dipertimbangkan.


## Cara Menjalankan Program

1. Install dependensi:

pip install numpy opencv-python matplotlib

2. Letakkan gambar input di folder yang sama:

input.png

3. Jalankan program:

python code.py

4. Output:
- Ditampilkan melalui matplotlib
- Disimpan sebagai:
  output_color_improved4.jpg
  
