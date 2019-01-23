# Nifty Web Application

## Run using docker 
``` docker build . -t nifty; docker run --name nifty -v ./src:/app/src --link pgsql:pgsql --rm -p 8888:8000 nifty ```