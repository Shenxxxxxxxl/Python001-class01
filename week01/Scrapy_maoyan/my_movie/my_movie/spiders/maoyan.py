import scrapy
from my_movie.items import MyMovieItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    #allowed_domains = ['https://maoyan.com/films']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        dataList = []
        infoList = response.xpath("//div[@class='movie-hover-info']")
        for i, info in enumerate(infoList):
            item = MyMovieItem()
            item['index'] = i
            item['title'] = info.xpath("./div[1]/span/text()").extract()[0].strip()
            item['tag'] = info.xpath("./div[2]/text()").extract()[1].strip()
            item['time'] = info.xpath("./div[4]/text()").extract()[1].strip()
            if i  == 10:
                break
            yield item
