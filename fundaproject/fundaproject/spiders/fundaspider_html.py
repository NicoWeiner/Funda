import scrapy


class FundaSpider(scrapy.Spider):
    name = "fundaspider"

    def start_requests(self):
        urls = [
            'https://www.funda.nl/en/koop/heel-nederland/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = FundaItem ()
        postcode = response.css (class="search-result-subtitle")
        asking_price = response.css (class="search-result-price")
        living_area_m2 = response.css (title="Living area")
        living_area_m2 = response.css ('span.title="Living area"::text')

        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)