BROKER = 'redis://localhost:6379/9'
BACKEND = 'redis://localhost:6379/10'

HUA_TONG_URL = 'http://www.ebaiyin.com/Ajax/GetHuaTong'
# header
HEADER = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
          }
PROXIES = {
        "http": "http://"+'111.2.122.46:8080',
        "https": "http://"+'111.2.122.46:8080',
}

# information 7*24
MAX_SEARCH_PAGE = 500
MAX_SEARCH_PAGE_NUM = 5
INFO_7X24_LIST_URL = 'http://www.ebaiyin.com/Ajax/GetNewsFlashList'
DATE_LENGTH = 18

# information
INFO_LIST_URL = 'http://www.ebaiyin.com/Ajax/GetInformationNewestList'
INFO_TRADE_LIST_URL = 'http://www.ebaiyin.com/Ajax/GetInformationByModuleList'


INFO_CONTENT_URL = 'http://www.ebaiyin.com/news/{}.shtml'

# market data
MARKET_URL = 'https://www.jin10.com/newest_1.js?rnd={}'
