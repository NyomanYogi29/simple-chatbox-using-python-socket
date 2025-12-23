# Simple Group Chat Application (Python Socket)

Proyek ini adalah implementasi aplikasi *Group Chat* sederhana berbasis GUI menggunakan **Python Socket** dan **Tkinter**. Proyek ini dibuat untuk memenuhi tugas **Ujian Akhir Semester (UAS) Praktikum Jaringan Komputer**.

Aplikasi ini menggunakan arsitektur **Client-Server** dengan protokol TCP, memungkinkan beberapa klien untuk terhubung ke server secara bersamaan dan saling bertukar pesan secara *real-time* (Multithreading).

## Fitur

* **Multi-Client Chat:** Server dapat menangani banyak klien sekaligus menggunakan *threading*.
* **GUI (Graphical User Interface):** Antarmuka pengguna yang ramah menggunakan library `tkinter`.
* **Nickname System:** Pengguna dapat memasukkan nama panggilan (nickname) saat bergabung.
* **Real-time Broadcast:** Pesan yang dikirim oleh satu klien akan langsung diterima oleh semua klien lain yang terhubung.
* **Notification:** Notifikasi ketika user bergabung atau meninggalkan chat room.

## Prasyarat (Prerequisites)

Pastikan Python 3.x sudah terinstall di komputer Anda. Library yang digunakan adalah library bawaan Python (Standard Library), sehingga tidak perlu melakukan instalasi `pip install` tambahan.

* `socket`: Untuk koneksi jaringan.
* `threading`: Untuk menangani banyak proses klien secara bersamaan.
* `tkinter`: Untuk antarmuka grafis (GUI).

## Konfigurasi IP Address

Sebelum menjalankan aplikasi, **penting** untuk menyesuaikan alamat IP server pada file `client.py`.

1.  Buka file `client.py`.
2.  Cari baris berikut (sekitar baris 9):
    ```python
    self.HOST = socket.gethostname()
    ```
3.  Ubah `self.HOST` sesuai kebutuhan:
    * Jika menjalankan Server dan Client di **satu komputer yang sama**, ubah menjadi `"127.0.0.1"` atau `"localhost"`.
    * Jika menjalankan di **jaringan LAN (beda komputer)**, ganti dengan IP Address komputer tempat `server.py` berjalan (misal: `192.168.1.X`).

## Cara Menjalankan (How to Run)

Ikuti langkah-langkah berikut untuk menjalankan aplikasi:

### 1. Menjalankan Server
Server harus dinyalakan terlebih dahulu agar bisa menerima koneksi. Buka terminal/cmd dan jalankan:

```bash
python server.py