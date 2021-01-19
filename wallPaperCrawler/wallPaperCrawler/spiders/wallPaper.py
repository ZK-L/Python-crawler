import scrapy
import time


class WallpaperSpider(scrapy.Spider):
    name = 'wallPaper'
    # allowed_domains = ['https://wallhaven.cc']
    start_urls = ['https://wallhaven.cc/search?categories=111&purity=110&ratios=16x9&sorting=favorites&order=desc&page=3']

    def parse(self, response):
        wallPaperLInks = response.css('a.preview::attr(href)').getall()
        for wallPaper in wallPaperLInks:
            yield scrapy.Request(wallPaper, callback =self.parseItem)
            time.sleep(0.5)
        

    def parseItem(self, response):
        img = response.css('div.scrollbox img::attr(src)').getall()
        yield {'image_urls': img}