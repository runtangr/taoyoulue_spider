FROM python:3.6
ADD ./ebaiyin_spider/ /app/ebaiyin_spider
WORKDIR /app/ebaiyin_spider
RUN pip install -r requirements.txt
CMD ["celery", "-A", "tasks.workers", "worker", "-l", "info", "-c", "1"]