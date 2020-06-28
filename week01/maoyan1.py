import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'Content-Type': 'text/plain; charset=UTF-8',
    'Origin': 'https://maoyan.com',
    'Referer': 'https://maoyan.com/films?showType=3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Cookie': 'uuid_n_v=v1; uuid=1D84C250B84711EAACB6BBD781D8993834EE4332C14F43078A9812351CF1B4D3; mojo-uuid=5626779d6b188ad9cb357370abebe4a6; _lxsdk_cuid=172f4a90b2ac8-08c40deb6c77f7-f7d123e-144000-172f4a90b2ac8; _lxsdk=1D84C250B84711EAACB6BBD781D8993834EE4332C14F43078A9812351CF1B4D3; _csrf=ab509b8b2c599bd493ff3148994b5fe53475d33ee77fe3f17b87c1afeefe020f; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593272389,1593273208,1593349783,1593357316; mojo-session-id={"id":"5e6578f5db976cb88c466fef17be80c4","time":1593364184436}; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593364184; __mta=208974381.1593242618761.1593361279698.1593364184809.20; mojo-trace-id=3; _lxsdk_s=172fbe7fda7-8ec-d16-e9%7C%7C3'
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
  #with open("maoyan_1.html", "r",encoding='utf-8') as f:
  #  res = f.read()
  dataList = filter_text(res)
  with open('maoyan_1.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer  = csv.writer(csvfile)
    writer.writerow(["序号","电影名称","电影类型","上映时间"])
    for row in dataList:
        writer.writerow(row)