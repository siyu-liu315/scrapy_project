# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Indeedv2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    title = scrapy.Field()
    location = scrapy.Field()
    company = scrapy.Field()
    jd = scrapy.Field()
    url = scrapy.Field()


