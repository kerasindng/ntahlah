# ━━━━━ Userbot Telegram ━━━━━
FROM python:3.8-slim

# ━━━━━ By IndomieUserbot ━━━━━

RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

RUN git clone -b Userbothon https://github.com/Friscay/Userbothon /root/Userbothon/ \
    && chmod 777 /root/Userbothon \
    && mkdir /root/Userbothon/bin/

WORKDIR /root/Userbothon/

RUN pip3 install flask flask_restful gunicorn

CMD ["bash", "start.sh"]
