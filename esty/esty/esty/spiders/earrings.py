import scrapy
from esty.items import EstyItem
import time 


class EarringsSpider(scrapy.Spider):
    name = 'earrings'
    start_urls = ['https://www.etsy.com/au/search?q=earring&page=1']
    pageNo = 1


    def parse(self, response):
        items = response.css('ul.wt-grid.wt-grid--block.wt-pl-xs-0.tab-reorder-container a::attr(href)').getall()
        self.pageNo = self.pageNo + 1 
        nextPage = 'https://www.etsy.com/au/search?q=earring&page={}'.format(self.pageNo)
        for item in items:
            yield scrapy.Request(item, callback=self.parseItem)
        time.sleep(0.2)
        if self.pageNo<251: 
            yield scrapy.Request(nextPage, callback = self.parse)


    def parseItem(self, response):
        newItem = EstyItem()
        newItem['link'] = response.url
        newItem['name'] = response.css('h1.wt-text-body-03.wt-line-height-tight.wt-break-word.wt-mb-xs-1::text').get().strip()
        newItem['seller'] = response.css('p.wt-text-body-01.wt-mr-xs-1 span::text').get().strip()
        seller =  response.css('div.wt-display-inline-flex-xs.wt-align-items-center.wt-mb-xs-3.wt-flex-wrap span.wt-text-caption::text').getall()
        newItem['sold'] = seller[1].strip()
        newItem['sellerArea'] = seller[0].strip()
        yield newItem