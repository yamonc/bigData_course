import sys
from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error
import xlwt


def askURL(url):
    """
    得到页面的全部内容
    :param url: 访问的url
    :return: 页面全部内容
    """
    # 设置反扒机制
    herders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.36 (KHTML,like GeCKO) Chrome/45.0.2454.85 Safari/537.36 115Broswer/6.0.3',
        'Referer': 'https://movie.douban.com/',
        'Connection': 'keep-alive'}
    request = urllib.request.Request(url, headers= herders)  # 发送请求
    try:
        response = urllib.request.urlopen(request)  # 取得响应
        html = response.read()  # 获取网页内容
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def getData(baseurl):
    # 找到影片详情的连接
    findLink = re.compile(r'<a href="(.*?)">')
    # 找到影片图片
    findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
    # 找到片名
    findTitle = re.compile(r'<span class="title">(.*)</span>')
    # 找到评分
    findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
    # 找到评价的人数
    findJudge = re.compile(r'<span>(\d*)人评价</span>')
    # 找到概况
    findInq = re.compile(r'<span class="inq">(.*)</span>')
    # 找到影片相关内容：导演、主演、年份、地区、类别
    findBd = re.compile(r'<p class="">(.*?)</p>', re.S)
    # 去掉无关内容
    remove = re.compile(r'                            |\n|</br>|\.*')
    # 列表存数据
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askURL(url)
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_='item'):
            # 找到每一个影片项
            data = []
            # 转换成字符串
            item = str(item)
            # 影片详情连接
            link = re.findall(findLink, item)[0]
            # 添加详情连接
            data.append(link)
            imgSrc = re.findall(findImgSrc, item)[0]
            # 添加图片链接
            data.append(imgSrc)
            titles = re.findall(findTitle, item)
            # 片名可能只有一个中文名，没有外国名
            if len(titles) == 2:
                ctitle = titles[0]
                # 添加中文片名
                data.append(ctitle)
                # 去掉无关符号
                otitle = titles[1].replace('/', '')
                # 添加外国片名
                data.append(otitle)
            else:
                # 添加中文名
                data.append(titles[0])
                # 留空
                data.append(' ')

            # 添加评分
            rating = re.findall(findRating, item)[0]
            data.append(rating)
            # 添加评论人数
            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)
            # 添加概况
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                # 有概况 去掉句号
                inq = inq[0].replace('。', '')
                # 添加概况
                data.append(inq)
            else:
                # 存储空
                data.append(' ')
            bd = re.findall(findBd, item)[0]
            bd = re.sub(remove, '', bd)
            # 去掉<br>
            bd = re.sub('<br(\s+)?\/?>(\s+)?', " ", bd)
            # 替换/
            bd = re.sub('/', '', bd)
            data.append(bd.strip())
            datalist.append(data)
    return datalist


def saveData(datalist, savepath):
    """
    保存数据到excel
    :param datalist: 要保存的数据
    :param savepath:  保存的路径
    :return:
    """
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('豆瓣电影TOP250', cell_overwrite_ok=True)
    col = ('电影详情链接', ' 图片链接', '影片中文名', '影片外国名', '评分', '评价数', '概况', '相关信息')
    for i in range(0, 8):
        # 列名
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        data = datalist[i]
        for j in range(0, 8):
            # 数据
            sheet.write(i + 1, j, data[j])
    # 保存
    book.save(savepath)


if __name__ == '__main__':
    print('开始爬取...')
    baseurl = 'https://movie.douban.com/top250?start='
    datalist = getData(baseurl)
    savapath = '豆瓣电影250.xls'
    saveData(datalist, savapath)