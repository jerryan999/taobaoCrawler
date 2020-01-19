# taobaoCrawler

step 1: 修改配置文件中爬虫代理相关的参数
```
  cp config.sample.yaml config.yaml 
```

step 2: 将seed url写入redis对应的key中, 类型list
```
  REDIS_HOST = "localhost"
  REDIS_PORT = 6379
  REDIS_DB = 3
  REDIS_URL_KEY_LIST = "taobao_1688_urls" 
```

step 3: 运行爬虫
```
 scrapy crawl taobao1688
```

step 4: 查看数据
```
  MONGODB_SERVER = "localhost"
  MONGODB_PORT = 27017
  MONGODB_DB = "taobao_1688"
  MONGODB_COLLECTION = "product_sku"
```
