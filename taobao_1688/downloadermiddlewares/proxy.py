import logging
import base64
from taobao_1688.middlewares import Taobao1688DownloaderMiddleware

logger = logging.getLogger(__name__)

class ProxyMiddleWare(Taobao1688DownloaderMiddleware):

    def process_request(self, request, spider):
        proxyUser = spider.settings.get('PROXY_USER')
        proxyPass = spider.settings.get('PROXY_PASS')
        proxyServer = spider.settings.get('PROXY_SERVER')
        
        proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")

        request.meta["proxy"] = proxyServer
        request.headers["Proxy-Authorization"] = proxyAuth
