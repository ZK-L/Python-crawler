import scrapy
import time
import random


class WallpaperSpider(scrapy.Spider):
    name = 'wallPaper'
    # allowed_domains = ['https://wallhaven.cc']
    page = random.randint(1,1000)
    start_urls = ['https://wallhaven.cc/search?categories=111&purity=110&ratios=16x9&sorting=favorites&order=desc&page='+str(page)]

    def parse(self, response):
        wallPaperLInks = response.css('a.preview::attr(href)').getall()
        for wallPaper in wallPaperLInks:
            yield scrapy.Request(wallPaper, callback =self.parseItem)

        

    def parseItem(self, response):
        img = response.css('div.scrollbox img::attr(src)').getall()
        yield {'image_urls': img}