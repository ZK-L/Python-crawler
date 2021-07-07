import scrapy
from crawlBigW.items import CrawlbigwItem

class BackingSpider(scrapy.Spider):
    name = 'backing'
    start_urls = ['https://www.bigw.com.au/home/kitchen/baking/c/6517117//']

    def parse(self, response):
        images = response.css("div.delayed-image-load::attr(data-src)").getall()
        itemName = response.css("h4.name a::text").getall()
        price = response.css("span.priceClass::text").getall()
        print(len(images), len(itemName), len(price),"-------")
        for a,b in enumerate(itemName):
            newItem = CrawlbigwItem()
            newItem["name"] = b.strip()
            newItem["price"] = price[a]
            newItem["image"] = images[a]
            yield newItem