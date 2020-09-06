import scrapy, ast, re, datetime
from shopping.items import ShoppingItem


class SmzdmSpider(scrapy.Spider):
    name = 'smzdm'
    allowed_domains = ['smzdm.com']
    start_urls = ['http://smzdm.com/']

    def start_requests(self):
        url = f'https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        infoList = response.xpath("//div[@class='z-feed-content ']")
        time_now = datetime.datetime.now()
        for info in infoList[:10]:
            print('=================i=================')
            a_content = info.xpath(".//h5/a")
            item = ShoppingItem()
            item['link'] = a_content.xpath(".//@href").extract()[0]
            item['id'] = item['link'].split("/")[-2] #获取商品id
            content = a_content.xpath(".//@onclick").extract()[0]
            print("爬出的id为%s" %item['id'] )
            dataLayer = ast.literal_eval(content[15: -1])
            item['pagetitle'] = dataLayer['pagetitle']
            item['tab'] = dataLayer['tab']
            item['mall'] = dataLayer['商城']
            item['channel'] = dataLayer['频道']
            item['position'] = dataLayer['position']
            release_time = info.xpath(".//div[@class='z-feed-foot']/div[@class='z-feed-foot-r']/span[@class='feed-block-extras']/text()").extract()[0].strip()
            if '前' == release_time[-1]:
                interval_str= release_time[-3:-1]
                time_minus = int(re.sub("\D", "", release_time))
                if '分钟' == interval_str:
                    item['release_time'] = time_now-datetime.timedelta(minutes=time_minus);
                elif '小时' == interval_str:
                    item['release_time'] = time_now-datetime.timedelta(hours=time_minus);
            else:
                item['release_time'] = str(time_now.year)+'-'+release_time
            #发布时间
            item['comments'] = []
            yield scrapy.Request(url=item['link'], meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        print("正在爬取详情" )
        item = response.meta['item']
        infoList = response.xpath("//div[@id='commentTabBlockNew']/ul/li[@class='comment_list']")
        next_ul = response.xpath("//*[@id='commentTabBlockNew']/ul[2]")
        comments = item['comments']
        for info in infoList:
            comment = {}
            comment['product_id'] = item['id']
            comment['id'] = info.xpath(".//@id").extract()[0][11:]
            comment_info = info.xpath(".//div[@class='comment_conBox']")
            comment['usmzdmid'] = comment_info.xpath(".//div[1]/a/@usmzdmid").extract()[0]
            comment['comment_time'] = comment_info.xpath(".//div[1]/div[1]/meta/@content").extract()[0]
            comment_list = comment_info.xpath(f".//p[@class='p_content_{comment['id']}']/span/text()").extract()
            comment['content'] = ''
            for c in comment_list:
                if c.strip():
                    comment['content'] = comment['content'] + c
            comment['support'] = comment_info.xpath(f".//a[@id='cdc_support_{comment['id']}']/span/text()").extract()[0][1:-1]
            comment['oppose'] =  comment_info.xpath(f".//a[@id='cdc_oppose_{comment['id']}']/span/text()").extract()[0][1:-1]
            comments.append(comment)
        if next_ul:
            print("翻页")
            max_li = int(next_ul.xpath(".//li[last()-3]/a/text()").extract()[0]) +1
            #重复调用获取评价
            for comment_idx in range(2,max_li+1):
                url = f"https://www.smzdm.com/p/{item['id']}/p{comment_idx}/#comments"
                yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse2)
        else:
            print("不翻页")
            yield item

