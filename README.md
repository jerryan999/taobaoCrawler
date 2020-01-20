# taobaoCrawler

step 1: 修改配置文件config.yml，新增阿布云代理参数
```
  cp config.sample.yaml config.yaml 
```

step 2: 将需要抓取的url写入redis对应的key中, 类型list
```
  REDIS_HOST = "localhost"
  REDIS_PORT = 6379
  REDIS_DB = 3
  REDIS_URL_KEY_LIST = "taobao_1688_urls" 
```
step 3: 准备一些session cookie数据到redis对应的key中,类型string,前缀如下
```
  REDIS_SESSION_KEY_PREFIX = taobao_1688_session
```


step 4: 打开终端，执行爬虫
```
 scrapy crawl taobao1688    # 自动把redis中抓取完成的key删除


 scrapy crawl taobao1688 -a remove_key=False   # 不删除redis中抓取完成的key
```

step 5: 在mongo数据库中查看数据
```
  MONGODB_SERVER = "localhost"
  MONGODB_PORT = 27017
  MONGODB_DB = "taobao_1688"
  MONGODB_COLLECTION = "product_sku"
```

