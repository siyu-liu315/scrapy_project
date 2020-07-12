import scrapy
from ..items import FreshdealItem

class FreshSpider(scrapy.Spider):
    name = 'fresh'
    start_urls = ['https://www.amazon.com/fmc/deals?almBrandId=QW1hem9uIEZyZXNo&ref=uf_dsk_sn_lnk_3_FD']

    def parse(self, response):
        item = FreshdealItem()

        dealname = response.css('.a-truncate-cut::text').extract()
        dealprice = response.css(".kepler-widget-price::text").extract()

        item["dealname"] = dealname
        item["dealprice"] = dealprice

        yield item


