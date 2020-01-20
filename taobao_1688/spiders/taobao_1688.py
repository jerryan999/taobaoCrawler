import scrapy
import re
import demjson
import redis
import datetime
import random

headers = {
                "Accept-Encoding": "gzip, deflate, br",
                "Upgrade-Insecure-Requests": "1",
                "Authority": "detail.1688.com",
                "Sec-Fetch-Site": "none",
                "Cache-Control": "no-cache",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Pragma": "no-cache",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Language": "en",
            }

class MySpider(scrapy.Spider):

    name = 'taobao1688'
    # allowed_domains = ['1688.com']

    start_time = datetime.datetime.now()


    def __init__(self, remove_key=True, *args, **kwargs):
        self.remove_key = remove_key
        super().__init__(*args, **kwargs)

    def start_requests(self):
        self.redis_client = redis.StrictRedis(host=self.settings.get('REDIS_HOST'), 
                        port=self.settings.get('REDIS_PORT'), 
                        db=self.settings.get('REDIS_DB'))

        for url in self.redis_client.lrange(self.settings.get('REDIS_URL_KEY_LIST'),0, -1):
            yield scrapy.Request(url.decode("utf-8"),
                headers=headers, 
                meta= {'dont_redirect': True, 
                     'cookiejar':random.randint(0,200) 
                     }, 
                    )

    def parse(self, response):
        item = {}
        item['url'] = response.url
        item['crawled_stamp'] = self.start_time

        # 从redis中删除相应的key
        if self.remove_key==True:
            print(item['url'])
            self.redis_client.lrem(self.settings.get('REDIS_URL_KEY_LIST'),1,item['url'])

        # parse sku field
        pattern = re.compile(r'var iDetailData = ({.+?});',re.DOTALL)
        s = pattern.search(response.text).group(1)
        item['sku'] = demjson.decode(s)['sku']

        return item
