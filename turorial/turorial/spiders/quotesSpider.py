import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://dining.sharif.ir/login?return=%2Fadmin%2Ffood%2Ffood-reserve%2Freserve'
        ]
        for url in urls:
            yield scrapy.Request(url=url)
            #yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)