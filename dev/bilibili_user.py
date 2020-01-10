# -*- coding: utf-8 -*-
"""
bilibili user
~~~~~~~~~~~~~
目标网站: www.bilibibli.com
爬虫描述: 爬取 bilibili 用户信息
示例链接: https://space.bilibili.com/33683045/
接口格式: 
示例接口:
    用户信息 - https://api.bilibili.com/x/space/acc/info?mid=26019347&jsonp=jsonp
    收藏夹 - https://api.bilibili.com/medialist/gateway/base/created?pn=1&ps=10&up_mid=26019347&jsonp=jsonp
    订阅番剧 - https://space.bilibili.com/ajax/Bangumi/getList?mid=26019347
    订阅标签 - https://space.bilibili.com/ajax/tags/getSubList?mid=26019347
    直播间 - https://api.live.bilibili.com/room/v1/Room/getRoomInfoOld?mid=26019347
反爬策略:
数据格式:
数据字段:
"""
import scrapy
from scrapy.crawler import CrawlerProcess


class BilibiliUserSpider(scrapy.Spider):
    name = 'bilibili_user'
    allowed_domains = ['space.bilibili.com']
    start_urls = ['https://api.bilibili.com/x/space/acc/info?mid=26019347&jsonp=jsonp']

    def parse(self, response):
        pass


#ITEM_PIPELINES = {
#    'crawler.pipelines.CrawlerPipeline': 300,
#}
#SPIDER_MIDDLEWARES = {
#    'crawler.middlewares.CrawlerSpiderMiddleware': 543,
#}
#DOWNLOADER_MIDDLEWARES = {
#    'crawler.middlewares.CrawlerDownloaderMiddleware': 543,
#}

settings = dict(
#    ITEM_PIPELINES=ITEM_PIPELINES,
#    SPIDER_MIDDLEWARES=SPIDER_MIDDLEWARES,
#    DOWNLOADER_MIDDLEWARES=DOWNLOADER_MIDDLEWARES,
)


def main():
    process = CrawlerProcess(settings)
    process.crawl(BilibiliUserSpider)
    process.start()


if __name__ == "__main__":
    main()