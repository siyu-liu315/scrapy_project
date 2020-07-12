import scrapy
from..items import IpoFeedbackItem
from urllib.parse import urlparse
from scrapy.http import Request
import urllib.request

class IpoSpider(scrapy.Spider):

    name = 'ipo'
    start_urls = ["http://www.csrc.gov.cn/pub/newsite/fxjgb/scgkfxfkyj/index.html"]

    def parse(self, response):
        start_url  = "http://www.csrc.gov.cn/pub/newsite/fxjgb/scgkfxfkyj"
        pages = response.css("ul li a")
        # page = 1
        for stock in pages:
            link = stock.xpath("@href").extract_first()
            add = link.split("/")[1]
            title = stock.xpath("./text()").extract()[0]
            url = start_url+link[1:]
            yield scrapy.Request(url,callback=self.parse_download,meta={"title" : title, "add" : add})

        while page <= 10:
            next_page = start_url + "/index_"+ str(page) + ".html"
            page += 1
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_download(self,response):
        start_url = "http://www.csrc.gov.cn/pub/newsite/fxjgb/scgkfxfkyj/"
        item = IpoFeedbackItem()
        href = response.xpath("//script").re(r'<a href="(\./P\d+?\.docx?)">|<a href="(\./P\d+?\.doc?)">|<a href="(\./P\d+?\.pdf)">')[0]
        url = start_url+response.meta["add"] + href[1:]
        title = response.meta["title"]
        item['url'] = url
        item['title'] = title

        filetype = href.split(".")[-1]
        try:
            file = urllib.request.urlopen(url).read()
            ### 需要修改文件下载的路径
            with open(f"C:\\Users\\Siyu\\Desktop\\test\\{title}.{filetype}", 'wb') as f:
                f.write(file)
        except urllib.request.HTTPError:
            item["status"] = "wrong:HTTPERROR"
        yield item







