FROM python:3.10-slim-bullseye

RUN mkdir wd

WORKDIR wd

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn","-b 0.0.0.0:8000", "main:app"]

EXPOSE 8000

