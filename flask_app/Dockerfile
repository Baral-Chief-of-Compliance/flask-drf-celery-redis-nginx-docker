FROM python:3.10-slim-bullseye

RUN mkdir -p /home/flaskApp

WORKDIR /home/flaskApp

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn","-b 0.0.0.0:8000", "main:app"]

EXPOSE 8000

