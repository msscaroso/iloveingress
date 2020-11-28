FROM python:3.8

RUN apt-get update && apt-get install nginx -y

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt -r dev-requirements.txt

CMD ["python", "main.py"]
