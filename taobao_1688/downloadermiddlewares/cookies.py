import logging
import json
from scrapy.exceptions import NotConfigured


logger = logging.getLogger(__name__)

class TaobaoCookiesMiddleware(object):
    """This middleware enables working with sites that need cookies"""
    def __init__(self, debug=False):
        self.debug = debug

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool('COOKIES_ENABLED'):
            raise NotConfigured
        return cls(crawler.settings.getbool('COOKIES_DEBUG'))

    def process_request(self, request, spider):
        if request.meta.get('dont_merge_cookies', False):
            return

        session_prefix = spider.settings.get('REDIS_SESSION_KEY_PREFIX')

        while True:
          key = spider.redis_client.randomkey()
          if session_prefix in key.decode("utf-8"):
            break

        cookie = json.loads(spider.redis_client.get(key))
        request.cookies=cookie
