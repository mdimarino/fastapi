FROM python:3.8-bullseye

EXPOSE 8000

RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install redis-tools telnet dnsutils -y && \
    useradd -ms /bin/bash app

COPY --chown=app:app main.py requirements.txt .env /home/app/

RUN pip install --no-cache-dir -r /home/app/requirements.txt

USER app

WORKDIR /home/app

RUN chmod 755 ./main.py

CMD [ "./main.py" ]
