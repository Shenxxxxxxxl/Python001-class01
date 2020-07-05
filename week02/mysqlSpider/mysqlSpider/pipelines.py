# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
db_info ={
    'host' :'127.0.0.1',
    'port' :3306,
    'user' :'root',
    'password' :'123456',
    'db':'python_learn'
}
class MysqlspiderPipeline:
    def __init__(self):
        self.conn = pymysql.connect(host=db_info['host'], port=db_info['port'], user=db_info['user'], password=db_info['password'], db=db_info['db'], charset='utf8')
        self.cursor = self.conn.cursor()
        self.sql='insert into maoyan(m_index,title,tag,time) values(%s,%s,%s,%s)'

    def process_item(self, item, spider):
        print('--------write----')
        try:
            effect_row=self.cursor.execute(self.sql,(item['index'],item['title'],item['tag'],item['time']))   # effect_row=1
            self.conn.commit()
        except Exception as e:
            print(type(e),e)
        return item
    
    def close_spider(self, spider):
        print('写入完成')
        self.cursor.close()
        self.conn.close()
