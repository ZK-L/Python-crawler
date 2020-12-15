import scrapy
from myCrawler.items import imageItem
import time

class ImagcrawlerSpider(scrapy.Spider):
    name = 'imagCrawler'
    # allowed_domains = ['https://www.mzitu.com/']
    start_urls = ['https://www.mzitu.com/tag/xiameijiang/']

    def parse(self, response):
        nextPage = response.css('a.next.page-numbers::text').get()
        if nextPage != None:
            nextPageUrl = response.css('a.next.page-numbers::attr(href)').get()
            # with open('url.txt', 'a+') as fp:
            #     fp.writelines(nextPageUrl+'\n')
            allUrl = response.css('div.postlist a::attr(href)').getall()
            for url in allUrl:
                yield scrapy.Request(url, callback = self.parseitem)
            time.sleep(1)
            yield scrapy.Request(nextPageUrl, callback = self.parse)
        


    def parseitem(self, response):
        item = imageItem()
        file_name = response.css('div.main-image img::attr(alt)').getall()
        img_src = response.css('div.main-image img::attr(src)').getall()
        item['file_name'] = file_name
        item['img_src'] = img_src
        time.sleep(1)
        yield item 
        if response.css('div.pagenavi span::text').getall()[-1] == '下一页»':
            nextPage = response.css('div.pagenavi a::attr(href)').getall()[-1]
            yield scrapy.Request(nextPage, callback = self.parseitem)

