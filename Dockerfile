FROM python:3.6
ADD ./ebaiyin_spider/ /app/ebaiyin_spider
WORKDIR /app/ebaiyin_spider
RUN pip install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
RUN pip install websocket-client==0.46.0
CMD ["celery", "-A", "tasks.workers", "worker", "-B", "-Q", "info_7x24,info,info_trade", "-l", "info"]