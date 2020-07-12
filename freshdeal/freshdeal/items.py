# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FreshdealItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    dealname = scrapy.Field()
    dealprice = scrapy.Field()
