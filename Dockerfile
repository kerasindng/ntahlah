# ━━━━━ Userbot Telegram ━━━━━
FROM python:3.8-slim

# ━━━━━ By IndomieUserbot ━━━━━

# Pindah ke direktori /root
WORKDIR /root

# Instalasi git
RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

# Clone repository Userbot
RUN git clone -b Userbothon https://github.com/kerasindng/ntahlah Userbothon && \
    chmod -R 777 Userbothon && \
    mkdir Userbothon/bin

# Pindah ke direktori Userbothon
WORKDIR /root/Userbothon

# Instalasi dependensi
RUN pip install --no-cache-dir -r requirements.txt

# Ekspose port yang diperlukan (sesuaikan dengan kebutuhan aplikasi)
EXPOSE 8080

# Perintah untuk menjalankan aplikasi
CMD ["bash", "start.sh"]
