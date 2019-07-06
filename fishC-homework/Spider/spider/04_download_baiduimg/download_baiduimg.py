#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
#__DATE__:2019-07-05
'''
到百度网站上搜索对应图片进行下载
'''
import urllib.request
import re
import os
import easygui as eg
from urllib import parse


def downloadpic(response,path):
    p = re.compile(r'("middleURL"):"(\S+jpg)"')
    url_list = [each_item[1] for each_item in p.findall(response)]
    num = 1
    for each_url in url_list:
        res = urllib.request.urlopen(each_url).read()
        filename = path + os.sep + str(num) +'.jpg'
        with open(filename, 'wb') as pic:
            pic.write(res)
        num += 1

def main():
    msg = '请输入需要下载的图片关键字！'
    title = '下载图片'
    keyword = eg.enterbox(msg, title, default='性感美女')
    url_data = parse.urlencode({'wd': keyword})[3:]
    url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word=' + url_data
    print(url)
    response = urllib.request.urlopen(url).read().decode('utf-8')
    filepath = r'C:\Users\460002000439\PycharmProjects\learning\fishC-homework' \
               r'\Spider\spider\04_download_baiduimg'
    downloadpic(response, filepath)

if __name__ == '__main__':
    main()