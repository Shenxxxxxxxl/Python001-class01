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

class ShoppingPipeline:
    def __init__(self):
        self.conn = pymysql.connect(host=db_info['host'], port=db_info['port'], user=db_info['user'], password=db_info['password'], db=db_info['db'], charset='utf8')
        self.cursor = self.conn.cursor()
        self.product_sql='insert into product(id, pagetitle, tab, mall, channel, position, link, release_time) VALUES(%s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE position = %s';
        self.comment_sql='insert into product_comment(id, product_id, usmzdmid, comment_time, content, support, oppose) VALUES(%s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE support = %s, oppose = %s';

    def process_item(self, item, spider):
        print('--------write----')
        try:
            if item['comments']:
                for comment in item['comments']:
                    self.cursor.execute(self.comment_sql,(comment['id'],comment['product_id'],comment['usmzdmid'],comment['comment_time'],comment['content'],comment['support'],comment['oppose'],comment['support'],comment['oppose'])) 
            effect_row=self.cursor.execute(self.product_sql,(item['id'],item['pagetitle'],item['tab'],item['mall'],item['channel'],item['position'],item['link'],item['release_time'],item['position']))   # effect_row=1
            self.conn.commit()
        except Exception as e:
            print(type(e),e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        print('写入完成')
        self.cursor.close()
        self.conn.close()
