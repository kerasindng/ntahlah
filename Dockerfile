#━━━━━ Userbot Telegram ━━━━━
FROM indomie/indomie:buster
#━━━━━ By IndomieUserbot ━━━━━

RUN git clone -b Userbothon https://github.com/kerasindng/ntahlah /home/Userbothon/ \
    && chmod 777 /home/Userbothon \
    && mkdir /home/Userbothon/bin/

# Pindah ke direktori Userbothon
WORKDIR /root/Userbothon

# Instalasi dependensi
RUN pip3 install flask flask_restful gunicorn
# Ekspose port yang diperlukan (sesuaikan dengan kebutuhan aplikasi)
EXPOSE 8080

# Perintah untuk menjalankan aplikasi
CMD ["bash", "start.sh"]
