# **Copywriting-Otomatis-Produk-Fashion-Menggunakan-T5**
## **Kontributor**

Berikut adalah daftar mahasiswa yang berkontribusi dalam proyek ini:

| Nama                   | NIM        |
| ---------------------- | ---------- |
| Ni Luh Anggita Gayatri | 2105551077 |
| Kristina               | 2105551088 |
| Dyah Putri Maheswari   | 2105551102 |
| Ni Made Naila Nalista  | 2105551115 |

---

## **Deskripsi**

Repository ini berisi implementasi model **T5 (Text-to-Text Transfer Transformer)** untuk menghasilkan teks copywriting deskripsi produk secara otomatis berdasarkan data produk fashion. Proyek ini bertujuan untuk membantu penjual atau pemasar dalam menciptakan deskripsi produk yang menarik dan informatif secara efisien.

---

## **Perbandingan Model**

Proyek ini membandingkan **tiga model** dalam menghasilkan deskripsi copywriting untuk produk fashionn. Berdasarkan evaluasi menggunakan metrik **ROUGE** dan **BLEU**, performa ketiga model adalah sebagai berikut:

| Model                     | ROUGE 1 | ROUGE 2 | ROUGE L | BLEU  |
|---------------------------|---------|---------|---------|-------|
| **T5 Menggunakan Indonesia Dataset**  | 0.83    | 0.76    | 0.81    | 0.70  |
| **T5 Menggunakan English Dataset**    | 0.88    | 0.82    | 0.86    | 0.78  |
| **mT5 Menggunakan Indonesia Dataset** | 0.62    | 0.47    | 0.57    | 0.41  |

---

### **Model Terbaik**  
Model **T5 Using English Dataset** mendapatkan hasil evaluasi terbaik dan dipilih sebagai model utama untuk digunakan dalam API.

---

## **Fitur Utama**

- **Pemrosesan Data**  
   Menyiapkan data produk fashion yang berasal dari website **Matahari** untuk melatih model T5. Data termasuk **nama produk**, **kategori**, **harga**, dan **deskripsi produk**.  
- **Pelatihan Model**  
   Melatih tiga model (**T5 Menggunakan English Dataset**, **T5 Menggunakan Indonesia Dataset**, dan **mT5**) untuk menghasilkan teks copywriting deskripsi produk.  
- **Inferensi**  
   Menghasilkan teks copywriting otomatis berdasarkan input **keywords** dari produk.  
- **Evaluasi Kinerja**  
   Mengevaluasi hasil copywriting menggunakan metrik **BLEU** dan **ROUGE**.  
- **API Integrasi**  
   Model terbaik (**T5 Using English Dataset**) diintegrasikan ke dalam **API** untuk digunakan dalam aplikasi produksi.

---

## **Proses Instalasi API**

Ikuti langkah-langkah berikut untuk menginstal dan menjalankan API:

### **1. Unduh Model T5 dan File API**
- Pastikan Anda memiliki model **T5** yang disimpan dalam direktori yang sama dengan file **`copywriting.py`**.
- Contoh struktur folder:
    ```
    project/
    ├── t5_english/          # Direktori model T5
    ├── copywriting.py       # File API
    └── requirements.txt     # File dependencies
    ```

---
