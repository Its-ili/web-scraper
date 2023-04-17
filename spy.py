import scrapy

class MySpider(scrapy.Spider):
    name = 'spy'
    start_urls = ['http://example.com']

    def parse(self, response):
        # Extract data from the webpage using XPath or CSS selectors
        data = {}
        data['title'] = response.css('h1::text').get()
        data['content'] = response.css('p::text').getall()
        yield data
