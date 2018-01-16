FROM python:3.6
ADD ./* /app/ebaiyin_spider
WORKDIR /app/ebaiyin_spider
RUN pip install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
CMD ["celery", "-A", "tasks.workers", "worker", "-l", "info", "-c", "1"]