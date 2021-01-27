FROM python:3

WORKDIR /devops-challenge

COPY /app .env requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install uwsgi


CMD uwsgi --socket 0.0.0.0:5000 --protocol=http -w main:app
