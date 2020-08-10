import json
import urllib.request
from bs4 import BeautifulSoup
import time
import socket
from Picture import Picture
import functools
import demjson
import pymysql
import os
import requests


def ask_request(page):
    """
    发出请求,目前最多34页
    :param page: 请求的页数
    :return: 返回json数据
    """
    url = 'https://picsum.photos/v2/list?page=' + page
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4040.5 Safari/537.36',
        'Referer': 'https://picsum.photos/images',
        'Connection': 'keep-alive'
    }
    request = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(request)  # 取得响应
    html = response.read()
    return html


def save2Db(list):
    conn = pymysql.connect(host='rm-2ze08bh0zi3p3z246oo.mysql.rds.aliyuncs.com', user='root', password='CYM1437qi',
                           db='blog_pro', port=3306)
    sql = 'insert into pic (id,author,width,height,url,download_url) values (%s,%s,%s,%s,%s,%s)'
    for i in plist:
        try:
            with conn.cursor() as cursor:
                conn.ping(reconnect=True)
                cursor.execute(sql,
                               (
                                   int(i.id), str(i.author), int(i.width), int(i.height), str(i.url),
                                   str(i.download_url)
                               )
                               )
                conn.commit()
        finally:
            conn.close()
        print(i)


def save2Local(list):
    root = "G:\\temp\image"
    for i in plist:
        path = root + '\\' + i.id + '.png'
        try:
            # 判断根目录是否存在
            if not os.path.exists(root):
                os.mkdir(root)
            # 判断文件是否存在
            if not os.path.exists(path):
                print("开始请求url，准备下载第%d号文件", i.id)
                r = requests.get(i.download_url)
                print("开始下载...")
                with open(path, 'wb') as f:
                    f.write(r.content)
                    f.close()
                    print('文件保存成功')
            else:
                print('文件路径：%s', i.download_url)
                print('文件已经存在')
        except:
            print('失败')
    print('一批保存完成...')


def save2Text(filename, content):
    f = open(filename, 'w', encoding='utf-8')
    f.write(content)
    f.close()



if __name__ == '__main__':

    for i in range(35):
        print('第%d批数据开始处理' %i)
        content = ask_request(str(i))
        # 写入文件
        save2Text('json.txt',str(content))
        # 读取文件
        with open('json.txt', 'r', encoding='utf-8') as f:
            temp = f.read()
        # 截取成json字符串
        pic_json = temp[2:-3]
        print(pic_json)
        # 映射成为类
        list = demjson.decode(pic_json, Picture)
        plist = []
        for i in range(0, len(list)):
            plist.append(Picture(list[i]))
        save2Db(plist)
        # save2Local(plist)
