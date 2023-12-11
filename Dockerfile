#━━━━━ Userbot Telegram ━━━━━
FROM indomie/indomie:buster
#━━━━━ By IndomieUserbot ━━━━━

RUN git clone -b Userbothon https://github.com/Friscay/Userbothon /home/Userbothon/ \
    && chmod 777 /home/Userbothon \
    && mkdir /home/Userbothon/bin/

WORKDIR /home/Userbothon/
RUN pip3 install flask
RUN pip3 install flask_restful
RUN pip install -r requirements.txt

CMD ["bash","start.sh"]
