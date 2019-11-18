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
        address = response.css ('h2.search-result-title::text').extract()
        postcode = response.css ('small.search-result-subtitle::text').extract()
        asking_price = response.css ('span.search-result-price::text').extract()
        living_area = response.css ('span.Living area::text').extract()
        property_area = response.css (title="Plot size")
        contruction_year = response.css (???)
        garden = response.css (???)
        type_house = response.css (???)
        description = response.css (???)
        energylabel = response.css (???)
        number_rooms = response.css (??? attribute is not given)
        number_bathrooms = response.css (???)
        items['address'] = address
        items['postcode'] = postcode
        items['asking_price'] = asking_price
        items['living_area'] = living_area
        items['property_area'] = property_area
        items['contruction_year'] = contruction_year
        items['garden'] = garden
        items['type_house'] = type_house
        items['description'] = description
        items['energylabel'] = energylabel
        items['number_rooms'] = number_rooms
        items['number_bathrooms'] = number_bathrooms
        yield items

