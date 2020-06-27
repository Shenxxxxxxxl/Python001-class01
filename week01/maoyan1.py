import requests
from bs4 import BeautifulSoup
import csv

#如果无法获取到对应的html，需要输入Cookie
headers = {
    'Content-Type': 'text/plain; charset=UTF-8',
    'Origin': 'https://maoyan.com',
    'Referer': 'https://maoyan.com/films?showType=3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Cookie': ''
}
#前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
def get_url(url):
  try:
    response = requests.get(url, headers=headers)
    print('response=%s'%response)
    if response.status_code ==200:
      return response.text
    else:return None
  except:return None

def filter_text(text):
  try:
    soup = BeautifulSoup(text,features="lxml")
    infoList = soup.find_all('div',class_='movie-item-hover')
    dataList = []
    for i, item in enumerate(infoList):
      print(item)
      index = i
      info = item.find("a").find_all("div")
      title = info[1].span.string
      tag = info[2].contents[2].strip()
      time = info[4].contents[2].strip()
      #df = pd.DataFrame(data,index=[index],columns=['title','tag','time'])\
      data = [index,title,tag,time]
      #print(data)
      dataList.append(data)
      if i  == 9:
        break
    
    print(dataList)
    return dataList

  except Exception as e:
    print(type(e),e)
    return None
  return None
if __name__ == '__main__':
  url = 'https://maoyan.com/films?showType=3'
  dataList = []
  res =''
  res = get_url(url)
  # 可以使用本地保存下来的html做测试
  #with open("D:\maoyan_3.html", "r",encoding='utf-8') as f:
  #  res = f.read()
  dataList = filter_text(res)
  with open('D:\maoyan_3.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer  = csv.writer(csvfile)
    writer.writerow(["序号","电影名称","电影类型","上映时间"])
    for row in dataList:
        writer.writerow(row)
