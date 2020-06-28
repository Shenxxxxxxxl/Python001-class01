from scrapy import Selector
with open("D:\Shenxl\Workspace\Python\geekPython\maoyan_3.html", "r",encoding='utf-8') as f:
    body = f.read()
#使用scrapy自身的Selector解析文本
selector = Selector(text=body)

#这里获得所有a标签中的链接

infoList = selector.xpath('//div[@class="movie-hover-info"]')
dataList = []
for i, item in enumerate(infoList):
    print(item)
    index = i
    title = item.xpath("./div[1]/span/text()").extract()[0].strip()
    tag = item.xpath("./div[2]/text()").extract()[1].strip()
    time = item.xpath("./div[4]/text()").extract()[1].strip()
    data = [index,title,tag,time]
    dataList.append(data)
    if i  == 9:
        break

print(dataList)