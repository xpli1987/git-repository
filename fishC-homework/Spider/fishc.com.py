#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
#__DATE__:2019-07-04
'''
爬取并下载鱼C官网，然后打印前300个字节
'''
import urllib.request
import chardet

#鱼C工作室官网
url = r'https://ilovefishc.com/css/styles.css'

#urlopen()函数返回get请求
response = urllib.request.urlopen(url).read(300).decode('utf-8')

print(response)