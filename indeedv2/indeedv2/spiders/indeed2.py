import scrapy
from scrapy.http import Request
from ..items import Indeedv2Item
from datetime import date
from datetime import datetime


class Indeed2Spider(scrapy.Spider):
    name = 'indeed2'
    allowed_domains = ['indeed.com']
    start_urls = 'http://indeed.com/'

    def start_requests(self):
        start_urls = "https://www.indeed.com/jobs?q=data%20analyst&l=United%20States&explvl=entry_level&fromage=3&sort=date&start=%s"
        for x in range(0,5):
           next_page = start_urls + str(x*10)
           yield scrapy.Request(next_page,callback = self.parse)

    def parse(self, response):
        origin = 'http://indeed.com'
        urls = response.xpath("//h2/a/@href").extract()
        for url in urls:
            request  = Request(origin+url,callback= self.detail_parse)
            request.meta['url'] = origin+url
            yield request

    def detail_parse(self, response):
        item = Indeedv2Item()
        ### job title
        jobtitle = response.xpath("//h3[contains(@class, 'JobInfoHeader')]/text()").extract()[0]
        item["title"] = jobtitle

        ## company name and location
        companyline  = response.xpath("//div[contains(@class, 'InlineCompanyRating')]//text()").extract()
        company = companyline[0]
        item['company'] = company
        location = companyline[-1]
        item['location'] = location

        # job description
        jd = response.xpath("//div[contains(@id , 'jobDescriptionText')]//text()").extract()
        description = ' '.join(jd)
        item['jd'] = description.replace("\n", "").encode('utf-8')

        # get time
        day = datetime.now().strftime("%Y/%m/%d")
        item['date'] = day

        # #get url
        item['url'] = response.meta['url']
        yield item


