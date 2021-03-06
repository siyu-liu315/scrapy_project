import scrapy
from..items import IndeedItem
from urllib.parse import urlparse
from scrapy.http import Request
import urllib.request

class IndeedSpider(scrapy.Spider):

    name = 'indeed'

    def start_requests(self):
        start_urls = "https://www.indeed.com/jobs?q=data%20analyst&l=United%20States&explvl=entry_level&fromage=3&sort=date&start=%s"
    # page &start = page*10 e.g https://www.indeed.com/jobs?q=data%20analyst&start=10
        for x in range(0,6):
           next_page = start_urls + str(x*10) + "#"
           yield scrapy.Request(next_page,callback = self.parse)

    def parse(self, response):
        url = "https://www.indeed.com/viewjob?jk=%s"
        print(url)
        JKs = response.xpath('//div[contains(@class,"jobsearch-SerpJobCard")]/@data-jk').extract()
        for JK in JKs:
            request = scrapy.Request(url=url % JK, callback=self.parse_indeed_results)
            request.meta['url'] = url%JK
            request.meta['dont_redirect'] = True
            yield request

#meta = {'dont_redirect': True, 'handle_httpstatus_list': [302]}
    def parse_indeed_results(self, response):
        # LIMIT
        """
        self.item_count += 1
        if self.item_count > 10:
            raise CloseSpider('item_exceeded')
        """
        item = IndeedItem()

        # # Date
        # date = response.css("jobsearch-JobMetadataFooter::text").extract()[0]
        # item['date'] = date

        # TITLE
        title = response.xpath('//h3[contains(@class,"JobInfoHeader")]/text()').extract_first()
        item['title'] = title.strip()

        # COMPANY
        company_data = response.xpath('//div[contains(@class,"InlineCompanyRating")]//text()').extract()
        item['company'] = company_data[0].strip()
        item['address'] = company_data[-1].strip()

    # DESCRIPTION
        description = response.xpath('//div[contains(@id,"jobDescriptionText")]//text()').extract()
        description = ' '.join(description)
        item['description'] = description.replace("\n", "").encode('utf-8')

    #URL
        item['url'] = response.meta['url']
        yield item


