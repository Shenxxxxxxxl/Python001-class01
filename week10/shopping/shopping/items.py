# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShoppingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id  = scrapy.Field() #商品id
    pagetitle  = scrapy.Field() #商品名称
    tab = scrapy.Field()
    mall = scrapy.Field() #商城
    channel = scrapy.Field() #频道
    position =  scrapy.Field() #排名
    link = scrapy.Field() #详情连接，获取评价
    release_time = scrapy.Field() # 发布时间
    comments = scrapy.Field() #评价
