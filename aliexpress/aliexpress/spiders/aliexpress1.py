import scrapy


class Aliexpress1Spider(scrapy.Spider):
    name = 'aliexpress1' # name of the spider 
    start_urls = ['https://www.bigw.com.au/baby/baby-clothes/c/6122/']

    def parse(self, response):
        print("processing:"+response.url)

        # create a dic to store the items 
        products = {}

        # extract the item name 
        name = response.css('h4.name a::text').getall()
        # extract item price 
        price = response.css('span.priceClass::text').getall()

        rawData = zip(name, price)
        # store the items in the dictionary
        for item in rawData:
            products[item[0].strip()] = item[1]
        yield products

        # generate a request to crawling next page 
        nextPage = response.css('li.next a::attr(href)').get()
        # check if the next page is not none
        if nextPage is not None: 
            nextPage = response.urljoin(nextPage)
            yield scrapy.Request(nextPage, callback = self.parse)

