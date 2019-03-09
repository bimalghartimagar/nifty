FROM python:3.7-alpine

COPY requirements.txt /

RUN apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install -r requirements.txt

COPY src/  /app/src/

COPY localhost-key.pem localhost.pem /app/

WORKDIR /app/
ENV DB_USERNAME=postgres
ENV DB_PASSWORD=
ENV DB_NAME=postgres
ENV DB_IP=psql
ENV ENV_TYPE=test
EXPOSE 8000

# localhost-key.pem and localhost.pem are private and public keys for ssl certificate
CMD ["gunicorn", "-w 4", "--reload-extra-file=src/templates", "--reload", "--access-logfile=-", "--error-logfile=-", "--log-file=-", "--certfile=localhost.pem", "--keyfile=localhost-key.pem", "--bind=0.0.0.0:8000", "src.main:app"]