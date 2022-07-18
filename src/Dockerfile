# FROM python:3.8-alpine
FROM python:3.8

EXPOSE 8000

# RUN apk update && \
#     apk upgrade && \
#     apk add tzdata && \
#     cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
#     echo "America/Sao_Paulo" > /etc/timezone && \
#     adduser -Ds /bin/ash app

RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install tzdata && \
    cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    echo "America/Sao_Paulo" > /etc/timezone && \
    useradd -m -s /bin/bash app

COPY --chown=app:app main.py requirements.txt .default_envvars /home/app/

RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r /home/app/requirements.txt

USER app

WORKDIR /home/app

RUN chmod 755 ./main.py

CMD [ "./main.py" ]
