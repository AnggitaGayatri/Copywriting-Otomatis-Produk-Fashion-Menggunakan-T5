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

### **1. Unduh Model T5 Bahasa Inggris dan File API**
- Pastikan Anda memiliki model **T5** yang disimpan dalam direktori yang sama dengan file **`copywriting.py`**.
- Contoh struktur folder:
    ```
    project/
    ├── t5_english/          # Direktori model T5
    ├── copywriting.py       # File API
    └── requirements.txt     # File dependencies
    ```
### **2. Buat Virtual Environment**
Buka terminal atau CMD, lalu arahkan direktori ke folder proyek:
```
cd path/to/project
```
Buat virtual environment dengan perintah berikut:
```
python -m venv venv
```
### **3. Aktifkan Virtual Environment**
- Untuk Windows:
```
venv\Scripts\activate
```
- Untuk Linux/Mac:
```
source venv/bin/activate
```
### **4. Install Dependencies**
Pastikan file requirements.txt berisi semua library yang dibutuhkan. Install library dengan perintah:
```
pip install -r requirements.txt
```
Jika muncul error terkait Rust atau Cargo, install Rust terlebih dahulu melalui https://rustup.rs/
### **5. Jalankan API**
Setelah instalasi selesai, jalankan API dengan perintah berikut:
```
python copywriting.py
```
Jika berhasil, server akan berjalan di:
```
http://127.0.0.1:8000
```
### **6. Akses Dokumentasi API**
Anda dapat mengakses dokumentasi API melalui endpoint /docs dengan mengunjungi:
```
http://127.0.0.1:8000/docs
```

---

## **Cara Menggunakan API**
### **Endpoint Utama**
| Method                     | Endpoint | Deskripsi |
|----------------------------|----------|-----------|
| GET  | /                     | Endpoint utama (welcome message) |
| POST | /generate_copywriting | Menghasilkan teks copywriting    |

---

### **Contoh Input dan Output**
Request:
```
POST /generate_copywriting
Content-Type: application/json

{
  "product_description": "baju koko pria"
}
```
Response:
```
{
  "input_language": "id",
  "translated_input": "Men's koko shirt",
  "generated_copywriting": "Men's koko shirt with a simple and casual design suitable as an everyday outfit for activities soft and quality material will be comfortable when used all day long"
}
```

---

### **Fitur Utama API**
1. Deteksi Bahasa Otomatis: API mendeteksi bahasa input dan menerjemahkannya ke dalam bahasa Inggris (jika bukan bahasa Inggris).
2. Pemrosesan Model T5: Menggunakan Hugging Face Transformers untuk menghasilkan teks copywriting.
3. Optimasi Output: Parameter seperti num_beams, temperature, dan length_penalty dikustomisasi untuk menghasilkan teks berkualitas tinggi.
4. Dokumentasi Interaktif: Endpoint tersedia dalam format Swagger UI di /docs.

---

### **Dependencies**
API ini menggunakan library berikut:
```
fastapi
uvicorn
transformers
torch
googletrans==4.0.0-rc1
```

---

## **Penutup**
Dengan mengikuti langkah-langkah di atas, Anda dapat menjalankan API copywriting berbasis model T5 dengan mudah. Jika ada kendala, silakan hubungi salah satu kontributor proyek.

---
