#!/bin/bash

# Menjalankan aplikasi Clever
python3 clever.py &

# Menunggu beberapa saat agar aplikasi dapat memulai
sleep 5

# Menjalankan modul Indomie
python3 -m indomie
