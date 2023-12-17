#━━━━━ Userbot Telegram ━━━━━
FROM indomie/indomie:buster
#━━━━━ By IndomieUserbot ━━━━━

RUN git clone -b Userbothon https://github.com/Friscay/Userbothon /home/Userbothon/ \
    && chmod 777 /home/Userbothon \
    && mkdir /home/Userbothon/bin/

WORKDIR /home/Userbothon/

RUN pip install -r requirements.txt

CMD ["python3", "-m", "indomie"]
