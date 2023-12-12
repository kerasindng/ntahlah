#!/bin/bash

# Pindah ke direktori proyek
cd /root/Userbothon/

# Instalasi dependensi
pip install -U -r requirements.txt

# Menjalankan aplikasi Clever
python3 clever.py &

# Menunggu beberapa saat agar aplikasi dapat memulai
sleep 5

# Menjalankan modul Indomie
python3 -m indomie
