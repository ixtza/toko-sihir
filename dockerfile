# 1. Memilih base image, seperti memilih lokasi toko
FROM python:3.9

# 2. Menentukan tempat kerja toko sihir
WORKDIR /app

# 3. Menyalin semua file ke dalam toko
COPY . /app

# 4. Menginstal bahan-bahan penting (pip dan Flask)
RUN pip install flask dotenv psycopy2

# 5. Menentukan pintu masuk pelanggan (port 5000)
EXPOSE 5000

# 6. Mantra untuk membuka toko saat dijalankan
CMD ["python", "app.py"]
