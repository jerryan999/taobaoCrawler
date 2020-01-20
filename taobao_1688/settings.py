# -*- coding: utf-8 -*-

# Scrapy settings for taobao_1688 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import yaml

with open('taobao_1688/config.yaml') as f:
    config = yaml.load(f)

BOT_NAME = 'taobao_1688'

SPIDER_MODULES = ['taobao_1688.spiders']
NEWSPIDER_MODULE = 'taobao_1688.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True


TELNETCONSOLE_USERNAME = "scrapy"
TELNETCONSOLE_PASSWORD = "pass"

# mongo for store data
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "taobao_1688"
MONGODB_COLLECTION = "product_sku"

# redis to store seed url
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 3
REDIS_URL_KEY_LIST = "taobao_1688_urls"  # 存储种子url的键
REDIS_SESSION_KEY_PREFIX = "taobao_1688_session"  # 存储网站session的key


# Proxy
PROXY_SERVER = config['proxy']['server']
PROXY_USER = config['proxy']['user']
PROXY_PASS = config['proxy']['password']

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1

# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 8
CONCURRENT_REQUESTS_PER_IP = 8

# Disable cookies (enabled by default)
COOKIES_ENABLED = False
COOKIES_DEBUG = False


# retry
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 429, 302]
RETRY_PRIORITY_ADJUST = -2

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'taobao_1688.middlewares.Taobao1688SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'taobao_1688.middlewares.Taobao1688DownloaderMiddleware': 543,
   
   'taobao_1688.downloadermiddlewares.cookies.TaobaoCookiesMiddleware': 700,
   'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,

   'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':None,
   'taobao_1688.downloadermiddlewares.proxy.ProxyMiddleWare':750
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'taobao_1688.pipelines.Taobao1688Pipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
