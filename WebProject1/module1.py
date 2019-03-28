import urllib;
import urllib.request;
import re;
#import asq;
import timeit;


print("fdsfsfs");

# 根据url获取网页html内容
def getHtmlContent(url):
  #  urllib.request.ur("")
    req=urllib.request.Request('http://www.pretend_server.com')
    page=  urllib.request.urlopen(req)

     #  print(e.reason)
    return req.data

# 从html中解析出所有jpg图片的url
# 百度贴吧html中jpg图片的url格式为：<img ... src="XXX.jpg" width=...>
def GetJpeg(html):
  # 解析jpg图片url的正则
    jpgReg = re.compile(r'<img.+?src="(.+?\.jpg)" width')  # 注：这里最后加一个'width'是为了提高匹配精确度
    # 解析出jpg的url列表
    jpgs = re.findall(jpgReg, html)
    return jpgs
def main():
    url="http://www.sohu.com"
    print( timeit( getHtmlContent(url)));

if __name__ == '__main__':
    main()