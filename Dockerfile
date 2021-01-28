FROM python:3

WORKDIR /devops-challenge

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install uwsgi
