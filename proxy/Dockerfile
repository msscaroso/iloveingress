FROM python:3.8

RUN apt-get update && apt-get install nginx -y

WORKDIR /app

COPY ../requirements.txt /app

RUN pip install -r requirements.txt



