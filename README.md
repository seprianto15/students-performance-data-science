# **Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech**
## **Business Understanding**
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan.  
Guna mengatasi permasalahan ini, perlu dilakukan analisis mendalam untuk mengidentifikasi faktor-faktor pemicu dropout serta pengembangan business dashboard sebagai alat monitoring. Solusi ini bertujuan mempermudah institusi dalam memantau performa mahasiswa sekaligus mempercepat pengambilan langkah intervensi yang tepat sasaran.

## **Permasalahan Bisnis**
Permasalahan utama yang sedang dihadapi Jaya Jaya Institut meliputi : 
1. Belum teridentifikasinya faktor-faktor determinan yang menjadi pemicu utama tingginya angka dropout siswa.
2. Belum tersedianya business dashboard untuk memantau performa siswa secara efektif.

## **Cakupan Proyek**
Proyek ini berfokus pada pengolahan data historis seluruh siswa yang bersumber dari Jaya Jaya Institut. Lingkup pekerjaan utama meliputi transformasi data menjadi business dashboard untuk mengidentifikasi berbagai faktor pemicu dropout, serta menerapkan sistem berbasis machine learning untuk memprediksi probabilitas dropout.  
Berdasarkan cakupan proyek tersebut, dibutuhkan beberapa resource dan tool seperti berikut :
1. Bahasa pemrograman Python sebagai tool utama dalam proyek ini.
2. Berbagai library pendukung untuk pengolahan data dan pengembangan model machine learning.
3. Tableau Public sebagai tool yang digunakan untuk membuat business dashboard.
4. Streamlit sebagai tool yang digunakan untuk membuat sebuah prototype sederhana berbasis machine learning.

## **Persiapan**
| <div align="center">Deskripsi</div> | <div align="center">Command</div> |
| :--- | :--- |
| Sumber Data | [Click here to Dataset](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/refs/heads/main/students_performance/data.csv) | 

```bash
# Setup Environment - Anaconda 
conda create --name students-performance python=3.13 
conda activate students-performance 
pip install numpy pandas scipy matplotlib seaborn jupyter scikit-learn imbalanced-learn
```

## **Business Dashboard**
Student Performance Dashboard ini dirancang dalam bentuk visualisasi chart/grafik untuk membantu Jaya Jaya Institut dalam mengidentifikasi faktor-faktor yang mempengaruhi atau memicu terjadinya dropout.

![Dashboard](dashboard.png)

Adapun bentuk visualisasi yang telah dibuat pada dashboard ini meliputi :
| <div align="center">Indikator</div> | <div align="center">Deskripsi</div> |
| :--- | :--- |
| Total Student | Menampilkan jumlah keseluruhan siswa dalam institut. |
| Dropout | Menampilkan jumlah siswa yang telah dinyatakan putus studi (dropout). |
| Enrolled | Menampilkan jumlah siswa aktif yang saat ini tengah menempuh pendidikan. |
| Graduate | Menampilkan jumlah siswa yang telah berhasil menyelesaikan masa studi (lulus). |
| Average Previous Qualification Grade vs Admission Grade by Student Status | Visualisasi perbandingan antara rata-rata previous qualification grade dengan admission grade berdasarkan status akademik siswa (Dropout, Enrolled, dan Graduate). |
| 1st Semester Academic Performance Comparison by Student Status | Visualisasi perbandingan antara rata-rata jumlah mata kuliah yang diuji (*evaluations*), yang lulus (*approved*), dan nilai rata-rata (*grade*) pada semester pertama berdasarkan status akademik siswa (Dropout, Enrolled, dan Graduate). |
| 2nd Semester Academic Performance Comparison by Student Status | Visualisasi perbandingan antara rata-rata jumlah mata kuliah yang diuji (*evaluations*), yang lulus (*approved*), dan nilai rata-rata (*grade*) pada semester kedua berdasarkan status akademik siswa (Dropout, Enrolled, dan Graduate). |
| Tuition Fees up to date by Student Status | Menampilkan status pembayaran uang kuliah mahasiswa (apakah paid atau unpaid) berdasarkan status akademik siswa (Dropout, Enrolled, dan Graduate). |  

Diharapkan dengan adanya visualisasi data ini, institut dapat mengambil langkah strategis untuk menekan angka dropout dan meningkatkan tingkat kelulusan siswa.  
Student Performance Dashboard dapat diakses pada tautan ini : [Click here to view dashboard](https://public.tableau.com/views/student_performance_17701627938620/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## Menjalankan Sistem Machine Learning
Prototype ini dirancang untuk mengotomatisasi prediksi dropout berbasis machine learning, guna menghasilkan wawasan preventif yang lebih akurat dibandingkan sekadar analisis data statis.  
Berikut adalah langkah-langkah untuk menjalankan prototype berbasis machine learning secara lokal :
```bash 
# Instal library streamlit dan babel
pip install streamlit babel
# Ekspor daftar dependensi ke file requirements.txt
pip freeze > requirements.txt 
# Instal semua dependensi dari file requirements
pip install -r requirements.txt
# Jalankan aplikasi dashboard secara local
streamlit run app.py
```
Berikut adalah tautan untuk mengakses prototype berbasis machine learning secara public :
[Click here to view application](https://app-students-performance.streamlit.app)

## Conclusion
Proyek ini dirancang untuk membantu Jaya Jaya Institut dalam mengidentifikasi faktor-faktor yang memicu terjadinya dropout. Berdasarkan integrasi business dashboard dan analisis prediktif, ditemukan bahwa :
1. Dari total 4424 siswa, sebanyak 2209 telah lulus (Graduate), sementara 1421 mengalami dropout, dan 794 sisanya masih dalam masa studi (Enrolled).
2. Berdasarkan performa akademik pada semester 1 dan 2, siswa yang lulus (Graduate) dan yang masih aktif (Enrolled) secara konsisten menunjukkan tingkat keberhasilan mata kuliah (approved) serta nilai rata-rata (grade) yang jauh lebih tinggi dengan rata-rata nilai 13 dan 12 dibandingkan mahasiswa yang Dropout, yang hanya memiliki rata-rata nilai di kisaran 9-10.
3. Berdasarkan Previous Qualification Grade dan Admission Grade, tidak terdapat perbedaan signifikan pada nilai kualifikasi sebelumnya (Previous Qualification Grade) maupun nilai seleksi masuk (Admission Grade) di antara ketiga status siswa (Dropout, Enrolled, dan Graduate), yang menunjukkan bahwa faktor eksternal setelah masuk kuliah lebih berpengaruh terhadap risiko dropout.
4. Berdasarkan data pembayaran SPP terbaru (Tuition Fees up to date), terdapat korelasi yang signifikan antara stabilitas finansial dan keberhasilan studi. Mayoritas siswa yang lulus (Graduate) tercatat telah melunasi kewajiban SPP (Paid) dengan total 2180 siswa. Sebaliknya, pada kategori Dropout, ditemukan tren yang menonjol pada kelompok dengan status SPP menunggak (Unpaid) sebanyak 457 siswa. Hal ini menegaskan bahwa hambatan finansial merupakan faktor kritis yang menghambat keberlanjutan studi.
5. Dengan adanya sistem berbasis Machine Learning, Jaya Jaya Institut kini memiliki kemampuan untuk mengambil langkah intervensi proaktif bagi siswa yang menunjukkan indikasi risiko dropout, guna meningkatkan angka keberhasilan studi dan efisiensi manajemen pendidikan.

## Rekomendasi Action Items
1. Memberikan prioritas bantuan beasiswa atau skema opsi cicilan SPP yang lebih ringan bagi siswa dengan status Unpaid.
2. Mengevaluasi tingkat kesulitan mata kuliah di setiap semester serta menginisiasi program Peer-to-Peer Mentoring sebagai sarana dukungan akademik tambahan bagi siswa.