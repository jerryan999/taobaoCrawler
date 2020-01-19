import scrapy
import re
import demjson
import redis
import datetime


class MySpider(scrapy.Spider):

    name = 'taobao1688'
    # allowed_domains = ['1688.com']

    start_time = datetime.datetime.now()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def start_requests(self):
        self.redis_client = redis.Redis(host=self.settings.get('REDIS_HOST'), 
                        port=self.settings.get('REDIS_PORT'), 
                        db=self.settings.get('REDIS_DB'))

        for url in self.redis_client.lrange(self.settings.get('REDIS_URL_KEY_LIST'),0, -1):
            yield scrapy.Request(url.decode("utf-8"), 
                meta= {'dont_redirect': True, 'handle_httpstatus_list':[302]})

    def parse(self, response):
        # scrapy.shell.inspect_response(response,self)
        # if response.status == 302: 
        #     return scrapy.Request(response.request.url, 
        #         meta= {'dont_redirect': True, 
        #             'handle_httpstatus_list':[302],
        #             'referrer_policy':'no-referrer'},
        #         dont_filter=True)

        item = {}
        item['url'] = response.url
        item['crawled_stamp'] = self.start_time

        # parse sku field
        pattern = re.compile(r'var iDetailData = ({.+?});',re.DOTALL)
        s = pattern.search(response.text).group(1)
        item['sku'] = demjson.decode(s)['sku']

        return item
