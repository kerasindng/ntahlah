#━━━━━ Userbot Telegram ━━━━━
FROM indomie/indomie:buster
#━━━━━ By IndomieUserbot ━━━━━

RUN git clone -b IndomieUserbot https://github.com/IndomieGorengSatu/IndomieUserbot /home/IndomieUserbot/ \
    && chmod 777 /home/IndomieUserbot \
    && mkdir /home/IndomieUserbot/bin/

WORKDIR /home/IndomieUserbot/

RUN pip install -r requirements.txt

CMD ["python3", "-m", "indomie"]
