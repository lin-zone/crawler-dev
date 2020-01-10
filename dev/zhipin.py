# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess


class ZhipinSpider(scrapy.Spider):
    name = 'zhipin'
    allowed_domains = ['www.zhipin.com']
    start_urls = 'https://www.zhipin.com/c101280100-p100109/?page=2&ka=page-2'

    def start_requests(self):
        yield scrapy.Request(self.start_urls, callback=self.parse, errback=self.parse_err)

    def parse(self, response):
        with open('index.html', 'wt', encoding='utf-8') as f:
            f.write(response.text)

    def parse_err(self, failure):
        print(failure.request.headers)


#ITEM_PIPELINES = {
#    'crawler.pipelines.CrawlerPipeline': 300,
#}
#SPIDER_MIDDLEWARES = {
#    'crawler.middlewares.CrawlerSpiderMiddleware': 543,
#}
DOWNLOADER_MIDDLEWARES = {
   'scrapyu.UserAgentMiddleware': 543,
}

settings = dict(
#    ITEM_PIPELINES=ITEM_PIPELINES,
#    SPIDER_MIDDLEWARES=SPIDER_MIDDLEWARES,
   DOWNLOADER_MIDDLEWARES=DOWNLOADER_MIDDLEWARES,
)


def main():
    process = CrawlerProcess(settings)
    process.crawl(ZhipinSpider)
    process.start()


if __name__ == "__main__":
    main()