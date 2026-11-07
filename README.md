# Cara menjalankan
1. Clone/pull repositori, lalu masuk ke direktori proyek lewat terminal.
2. Buat virtual environment:
```
python3 -m venv venv
```
3. Aktifkan virtual environment dan install dependensi:
```bash
source venv/bin/activate
pip install -r requirements.txt
```
Di Windows, aktifkan virtual environment dengan `venv\Scripts\activate`.

4. Jalankan server dengan debug aktif dari terminal:
```bash
python3 -m flask --app main run --debug
```
Opsi `--debug` mengaktifkan debug mode dan auto-reload. Buka alamat yang ditampilkan Flask di terminal (biasanya `http://127.0.0.1:5000`).

Untuk menjalankan Jupyter Notebook, gunakan:
```bash
jupyter notebook
```

## Deploy ke Render.com
1. Di Render, buat **New > Web Service**, lalu hubungkan repositori dan pilih branch yang akan di-deploy.
2. Pilih **Python** sebagai runtime, lalu isi perintah berikut:

   **Build Command**
   ```bash
   pip install -r requirements.txt
   ```

   **Start Command**
   ```bash
   gunicorn --bind 0.0.0.0:$PORT main:app
   ```

3. Klik **Create Web Service**. Setelah proses deploy selesai, buka URL yang disediakan Render.

## Migrasi
Silahkan pindah dari Flask ke FastAPI https://github.com/fastapi/fastapi untuk performa dan pengalaman yang lebih baik.