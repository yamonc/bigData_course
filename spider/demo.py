
#  下载网页
import requests
url = 'https://music.163.com/#/playlist?id=3193274452'
# 模拟浏览器发送http请求
response = requests.get(url)
# 编码方式
response.encoding = 'utf-8'
print(response.text)
