Nama: Nabila
Nim: 240907501011

Web Scraping Books to Scrape

Deskripsi

Project ini dibuat untuk memenuhi tugas Aktivitas Scraping Data pada mata kuliah Social Media Analysis. Data diperoleh dengan melakukan web scraping pada website Books to Scrape.

Sumber Data

Website yang digunakan:

https://books.toscrape.com/

Books to Scrape merupakan website latihan yang menyediakan data buku untuk keperluan pembelajaran web scraping.

Library yang Digunakan

Project ini menggunakan beberapa library Python:

- "requests" untuk mengambil halaman website.
- "BeautifulSoup" untuk membaca dan mengambil data dari struktur HTML.
- "pandas" untuk mengolah data dan menyimpannya dalam format CSV.

Data yang Diambil

Data buku yang dikumpulkan meliputi:

- Title – judul buku
- Price – harga buku
- Rating – rating buku
- Availability – ketersediaan buku

Proses Scraping

Program mengambil data dari setiap halaman Books to Scrape. Program akan mencari halaman berikutnya secara otomatis sampai seluruh halaman selesai diproses.

Data yang diperoleh kemudian dikumpulkan menggunakan Pandas DataFrame dan disimpan dalam file:

"books.csv"

Cara Menjalankan Program

Pastikan Python sudah terinstal dan environment sudah aktif.

Install library yang diperlukan:

python -m pip install requests beautifulsoup4 pandas

Kemudian jalankan program:

python scraping_books.py

Setelah proses selesai, hasil scraping akan tersimpan dalam file:

books.csv

Struktur Project

scraping-books/
│
├── scraping_books.py
├── books.csv
├── README.md
└── .gitignore

Hasil

Hasil scraping disimpan dalam bentuk file CSV dan dapat digunakan untuk melihat serta mengolah data buku lebih lanjut.