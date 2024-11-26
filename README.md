![header](../DBS_Proyek/img/petani.jpg)
# Laporan Proyek Machine Learning - M.TOFIK HIDAYAT

## Project Overview

Kebanyakan Petani masih banyak yang belum mengetahui tanaman apa yang cocok ditanaman di lahannya. Hal ini disebabkan karena kurangnya pengetahuan petani mengenai kesesuaian lahan dengan persyaratan tumbuh suatu tanaman. Lemahnya tingkat pengetahuan petani dan masyarakat tentang evaluasi kesesuaian lahan menyebabkan tanaman yang dibudidayakan tidak berproduksi optimal, karena syarat yang dibutuhkan tanaman tersebut belum sesuai dengan kondisi lahan yang mendukung pertumbuhan tanaman tersebut. Melihat pentingnya proses pemilihan tanaman berdasarkan kesesuain lahan, sedangkan penentuan pemilihan tanaman masih dilakukan hanya berdasarkan dengan melihat pengalaman petani yang belum teruji. Maka penulis merasa perlu membuat penelitian untuk menentukan tanaman pada lahan berdasarkan kesesuain lahan dan persyaratan tumbuh tanaman. Dengan adanya penelitian ini, maka dapat menentukan tanaman perkebunan yang akan ditanam pada suatu lahan berdasarkan tingkat kesesuaian lahan dan persyaratan tumbuh tanaman yang menjadi alternatif secara tepat, akurat dan dinamis.

**Rubrik/Kriteria**:

Proyek ini bertujuan untuk menganalisis hubungan antara kondisi tanah, faktor iklim, dan rekomendasi tanaman yang optimal menggunakan Agricultural Crop Dataset. Dataset ini mencakup parameter penting seperti kandungan nutrisi tanah (Nitrogen, Fosfor, Kalium), suhu, kelembapan, pH tanah, dan curah hujan. Dengan memanfaatkan teknik Machine Learning, proyek ini dapat menghasilkan model prediksi tanaman yang sesuai untuk ditanam berdasarkan kondisi lingkungan tertentu.
  
  Format Referensi: [PEMILIHAN TANAMAN BERDASARKAN KONDISI LAHAN DAN PERSYARATAN TUMBUH TANAMAN MENGGUNAKAN GABUNGAN METODE AHP DAN TOPSIS](https://jurnal.stmikroyal.ac.id/index.php/jurteksi/article/view/430) 

## Business Understanding

Penggunaan lahan pertanian dan perkebunan saat sekarang masih banyak petani yang belum mengetahui kesesuain dari lahan tersebut. Petani   masih banyak yang belum mengetahui tanaman  apa  yang  cocok ditanaman di lahannya. Hal ini disebabkan karena kurangnya pengetahuan petani mengenai kesesuaian lahan dengan persyaratan tumbuh suatu tanaman. Kesesuaian lahan adalah penggambaran tingkat kecocokan sebidang lahan untuk suatu penggunaan tertentu. Kesesuaian lahan merupakan bagian dari evaluasi lahan. Evaluasi kesesuaian lahan sangat diperlukan dalam  perencanaan penggunaan lahan agar lahan dapat digunakan secara optimal, produktif dan berkelanjutan. Lemahnya tingkat pengetahuan petani dan masyarakat tentang evaluasi kesesuaian lahan menyebabkan tanaman yang dibudidayakan tidak berproduksi optimal, karena syarat yang dibutuhkan tanaman tersebut belum sesuai dengan kondisi lahan yang mendukung pertumbuhan tanaman tersebut.

Melihat betapa pentingnya proses pemilihan lahan yang cocok untuk ditanami beberapa tumbuhan dengan mempertimbangkan segi unsur-unsur dari tanah itu sendiri maka peneliti membantu untuk membuatkan sebuah program kecerdasan buatan guna untuk mengklasifikasi tanah mana yang cocok dengan tumbuhan yang akan di tanam oleh petani itu sendiri, hal ini sangat membantu petani untuk menghindari panen yang kurang maksimal bahkan gagal panen.

### Problem Statements

Menjelaskan pernyataan masalah:
- Bagaimana model prediksi berbasis data dapat membantu memberikan rekomendasi tanaman yang paling cocok?
- Bagaimana data ini dapat digunakan untuk memberikan panduan penggunaan sumber daya secara efisien?

### Goals

Menjelaskan tujuan proyek yang menjawab pernyataan masalah:
- Mengembangkan model prediksi berbasis data yang memberikan rekomendasi tanaman terbaik berdasarkan kondisi tanah (N, P, K, pH) dan faktor lingkungan (suhu, kelembapan, curah hujan).
- Menyediakan panduan berbasis data untuk optimalisasi penggunaan pupuk dan air, berdasarkan analisis kandungan nutrisi tanah dan kebutuhan tanaman tertentu.

**Rubrik/Kriteria**:
- Menambahkan bagian “Solution Approach” yang menguraikan cara untuk meraih goals. Bagian ini dibuat dengan ketentuan sebagai berikut: 

    ### Solution statements
    - Menggunakan algoritma Supervised Machine Learning seperti Random Forest, Gradient Boosting (XGBoost/LightGBM), atau Logistic Regression untuk membangun model klasifikasi.
    - Mengadaptasi pendekatan sistem rekomendasi berbasis collaborative filtering. Petani atau wilayah yang memiliki kondisi tanah dan lingkungan serupa dianalisis untuk memberikan rekomendasi tanaman berdasarkan data historis.

## Data Understanding
Pada Agricultural Crop Dataset memiliki 1697 baris dan 8 kolom, kolom-kolomnya dirancang untuk memberikan informasi yang relevan tentang kondisi tanah, lingkungan, dan rekomendasi tanaman yang cocok. Dataset bisa diakses pada link berikut : [KAGGLE Agricultural Crop Dataset](https://www.kaggle.com/datasets/agriinnovate/agricultural-crop-dataset/data).

Berikut penjelasan dari setiap kolom utama::  

Variabel-variabel pada Agricultural Crop Dataset adalah sebagai berikut:
- N (Nitrogen) : Tingkat kandungan Nitrogen di tanah.
- P (Phosphorus) : Tingkat kandungan Fosfor di tanah.
- K (Potassium) : Tingkat kandungan Kalium di tanah.
- Temperature (Suhu) : Suhu rata-rata lingkungan (dalam derajat Celcius).
- Humidity (Kelembaban) : Deskripsi: Persentase kelembapan udara.
- PH (Derajat Keasaman Tanah) : Nilai pH tanah.
- Rainfall (Curah Hujan) :  Curah hujan rata-rata (dalam mm).
- Label : Rekomendasi tanaman yang cocok untuk ditanam berdasarkan parameter lainnya.

**Rubrik/Kriteria**:
- Melakukan beberapa analisa dan visualisasi terhadap kolom target.
- Melakukan analisa terhadap kolom categorical dengan target.
- Melakukan analisa terhadap kolom numerical dengan target.
- Melakukan analisis korelasi dari semua kolom dengan target.
## Data Preparation
Tahap ini mempersiapkan dan membersihkan dataset untuk memastikan data siap digunakan oleh model Machine Learning.

**Rubrik/Kriteria**: 
- Memastikan tidak ada nilai yang hilang (missing values).
- Menstandarkan skala data, seperti suhu, kelembapan, dan kandungan nutrisi tanah, menggunakan normalisasi atau standardisasi.
- Menangani data yang outlier untuk meningkatkan akurasi prediksi.
## Modeling
Tahap ini yaitu memilih beberapa algoritma machine learning yang mengklasifikasikan beberapa macam tumbuhan.

**Rubrik/Kriteria**: 
- Menggunakan model algoritma Random Forest, Xgboots dan Logistic Regression .
- Kelebihan Random Forest : 
    1.Dapat menangani data dengan hubungan non-linear
    2.Tidak mudah overfitting karena menggunakan banyak pohon.
    3.Memberikan feature importance untuk memahami kontribusi setiap fitur.
- Kekurangan Random Forest : 
    1.Membutuhkan banyak sumber daya komputasi.
    2.Kurang efisien untuk dataset yang sangat besar.
- Kelebihan Logistic Regression:
    1.Mudah diimplementasikan dan diinterpretasikan.
    2.Cocok untuk data dengan jumlah fitur kecil.
    3.Tidak membutuhkan banyak daya komputasi.
- Kekurangan Logistic Regression:
    1.Tidak cocok untuk data dengan hubungan non-linear.
    2.Membutuhkan preprocessing yang baik agar hasil akurat.

## Evaluation
Pada bagian ini, peneliti menggunakan metrik F1-Score untuk mengevaluasi performa model. F1-Score dipilih karena memberikan keseimbangan antara Precision dan Recall, yang sangat penting dalam konteks sistem rekomendasi tanaman. Sistem harus tidak hanya akurat dalam memilih tanaman yang relevan (Precision) tetapi juga mampu merekomendasikan semua tanaman yang cocok dengan kondisi tertentu (Recall).

![evaluation](../DBS_Proyek/img/Cv_matrik.png)

**Rubrik/Kriteria**: 
- Dalam sistem rekomendasi, penting untuk meminimalkan False Positives (rekomendasi yang tidak cocok) dan False Negatives (tanaman yang cocok tetapi tidak direkomendasikan).
- Peneliti mempertimbangkan F1-score sebagai metrik evaluasion guna memungkinkan para petani tidak salah dalam menanam tumbuhan yang ingin ditanam.
