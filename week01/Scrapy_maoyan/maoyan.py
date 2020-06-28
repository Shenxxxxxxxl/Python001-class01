import scrapy
from geekPython.Scrapy_maoyan.my_movie.my_movie.items import MyMovieItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['https://maoyan.com/films?showType=3']
    start_urls = ['http://https://maoyan.com/films?showType=3/']

    def parse(self, response):
        infoList = response.css("//div[@class='movie-hover-info']")
        for i, item in enumerate(infoList):
            print(item)
            index = i
            title = item.css("/div[1]/span/text()")
            tag = item.css("/div[2]")
            time = item.css("/div[4]")
            data = [index,title,tag,time]
            if i  == 9:
                break
            yield item
