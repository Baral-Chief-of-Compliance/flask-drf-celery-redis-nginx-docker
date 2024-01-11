FROM python:3.9.6

RUN mkdir wd

WORKDIR wd

COPY .env tasks.py requirements.txt soiskatel.py employer.py .

RUN pip install --no-cache-dir -r requirements.txt

# COPY tasks.py .

CMD ["celery","-A", "tasks", "worker", "--loglevel=info"]