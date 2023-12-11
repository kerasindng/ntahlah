#━━━━━ Userbot Telegram ━━━━━
FROM indomie/indomie:buster
#━━━━━ By IndomieUserbot ━━━━━

RUN git clone -b Userbothon https://github.com/Friscay/Userbothon /root/Userbothon/ \
    && chmod 777 /root/Userbothon \
    && mkdir /root/Userbothon/bin/

WORKDIR /root/Userbothon/

RUN pip3 install flask
RUN pip3 install flask_restful 
RUN pip3 install gunicorn
CMD ["sudo","/root/start.sh"]
