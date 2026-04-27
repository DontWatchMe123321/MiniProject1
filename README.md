# Image Restoration Mini Project

## Penjelasan Pipeline Restorasi

Pipeline restorasi pada proyek ini bertujuan untuk memperbaiki kualitas citra berwarna yang terdegradasi oleh noise, kontras rendah, dan ketajaman yang berkurang. Seluruh proses dilakukan secara berurutan pada setiap channel warna (RGB).

### 1. Denoising — Median Filter (k = 5)
Tahap pertama menggunakan median filter manual dengan kernel 5x5.

Prosesnya:
- Setiap piksel diproses dengan mengambil window 5x5 di sekitarnya
- Nilai dalam window di-flatten lalu diurutkan
- Nilai median digunakan untuk menggantikan piksel pusat

Alasan pemilihan:
- Efektif untuk menghilangkan noise tipe salt-and-pepper
- Lebih baik dalam menjaga edge dibandingkan rata-rata (mean filter)
- Kernel 5x5 dipilih untuk menangani noise yang cukup padat tanpa terlalu mengaburkan detail

---

### 2. Contrast & Brightness Adjustment (α = 1.2, β = 15)
Setelah denoising, citra cenderung kehilangan kontras. Oleh karena itu dilakukan penyesuaian intensitas:

I_out = α * I_in + β

Dengan:
- α = 1.2 → meningkatkan kontras secara moderat
- β = 15 → menambah kecerahan

Tahap ini membantu:
- Memperjelas perbedaan intensitas
- Mengangkat detail yang sebelumnya kurang terlihat

### 3. Gaussian Blur (Kernel 3x3, σ = 1)
Gaussian filter digunakan sebagai bagian dari proses sharpening.
Karakteristik:
- Kernel dibuat manual menggunakan distribusi Gaussian
- Memberikan bobot lebih besar pada piksel pusat
- Menghasilkan citra yang lebih halus (low-pass filtering)
Hasil blur ini tidak digunakan sebagai output akhir, tetapi sebagai referensi untuk mengekstrak detail pada tahap berikutnya.

### 4. Sharpening — Unsharp Masking (α = 0.8)
Sharpening dilakukan dengan metode unsharp masking:

1. Hitung mask:

mask = image - blurred

2. Tambahkan kembali mask:

sharpened = image + α * mask

Dengan α = 0.8:
- Detail diperkuat secara moderat
- Menghindari over-sharpening dan amplifikasi noise

Tujuan:
- Mengembalikan ketajaman yang hilang akibat denoising dan blur
- Memperjelas edge dan tekstur

### 5. Pemrosesan per Channel RGB
Citra diproses sebagai berikut:
- Dibaca dalam format BGR lalu dikonversi ke RGB
- Dipisahkan menjadi channel Red, Green, dan Blue
- Setiap channel diproses secara independen menggunakan pipeline yang sama
- Hasil akhir digabung kembali menjadi citra berwarna

Pendekatan ini menjaga fleksibilitas pemrosesan, meskipun dapat menyebabkan sedikit perubahan warna karena tidak mempertimbangkan korelasi antar channel.

### Urutan Pipeline
Denoising (Median Filter) → Contrast Adjustment → Gaussian Blur → Unsharp Masking → Merge Channel

## Analisis Singkat

### Yang berhasil:
- Median filter efektif mengurangi noise tanpa merusak struktur utama
- Kombinasi contrast adjustment dan sharpening meningkatkan visibilitas detail
- Unsharp masking dengan α rendah menghasilkan ketajaman yang natural
- Pipeline berjalan baik untuk citra berwarna

### Yang bisa ditingkatkan:
- Performa masih lambat karena menggunakan loop Python
- Contrast adjustment masih menggunakan fungsi OpenCV (belum manual)
- Tidak menggunakan histogram equalization untuk peningkatan kontras yang lebih adaptif
- Pemrosesan per channel RGB dapat menyebabkan distorsi warna ringan

---

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
  
