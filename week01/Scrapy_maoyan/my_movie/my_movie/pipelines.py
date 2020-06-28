# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class MyMoviePipeline:
    def __init__(self):
        self.file = open("maoyan2.csv",'w',encoding='utf-8')
        self.writer = csv.writer(self.file)
        self.writer.writerow(["序号","电影名称","电影类型","上映时间"])

    def process_item(self, item, spider):
        print('--------write----')
        self.writer.writerow([item['index'],item['title'],item['tag'],item['time']])
        return item
    
    def close_spider(self, spider):
        print('写入完成')
        self.file.close()
