#━━━━━ Userbot Telegram ━━━━━
FROM indomie/indomie:buster
#━━━━━ By IndomieUserbot ━━━━━

RUN git clone -b Userbothon https://github.com/kerasindng/ntahlah /home/Userbothon/ \
    && chmod 777 /home/Userbothon \
    && mkdir /home/Userbothon/bin/

WORKDIR /home/Userbothon/

RUN pip install -r requirements.txt

CMD ["bash", "start.sh"]
