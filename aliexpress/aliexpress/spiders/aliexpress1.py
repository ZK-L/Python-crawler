import scrapy


class Aliexpress1Spider(scrapy.Spider):
    name = 'aliexpress1' # name of the spider 
    allowed_domains = ['aliexpress.com']
    start_urls = ['https://www.aliexpress.com/af/category/100004960.html?categoryBrowse=y&origin=n&CatId=100004960&catName=drinkwar']

    def parse(self, response):
        print("processing:"+response.url)

        product = {}
        product['name'] = response.css('.product::text').extract()
        product['range'] = response.css('.value::text').extract()

        # Extract data using xpath
        product['orders'] = response.xpath("//em[title-'Total Orders']/text()").extract()
        procut['companyName'] = response.xpath("//a[class='store $p4pLog'/text()").extract()

        yield product
