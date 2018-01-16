BROKER = 'redis://redis:6379/9'
BACKEND = 'redis://redis:6379/10'

HUA_TONG_URL = 'http://www.ebaiyin.com/Ajax/GetHuaTong'
# header
HEADER = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
          'Host': 'www.ebaiyin.com'
          }
PROXIES = {
        "http": "http://"+'111.2.122.46:8080',
        "https": "http://"+'111.2.122.46:8080',
}

# silver 7*24
MAX_SEARCH_PAGE = 500
MAX_SEARCH_PAGE_NUM = 5

NEWS_LIST_URL = 'http://www.ebaiyin.com/Ajax/GetNewsFlashList'
NEWS_CONTENT_URL = 'http://www.ebaiyin.com/news/{}.shtml'
DATE_LENGTH = 18

# information
INFORMATION_LIST_URL = 'http://www.ebaiyin.com/Ajax/GetInformationNewestList'
TRADE_INFORMATION_LIST_URL = 'http://www.ebaiyin.com/Ajax/GetInformationByModuleList'


