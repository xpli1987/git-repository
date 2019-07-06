#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
#__DATE__:2019-07-04
'''
写一个程序，依次访问文件中指定的站点，并将每个站点返回的内容依次存放到不同的文件中
'''
import urllib.request
import chardet
import re

'''
读取urls.txt文件中的url并保存到url_list列表中
'''
urls_list = list()
with open(r'spider/02/urls.txt','r') as f:
    urls_list = [each_url for each_url in f]
print(urls_list)

'''
读取url内容
'''
def getSome(url):
    response = urllib.request.urlopen(url).read()
    encodings = chardet.detect(response)['encoding']
    if encodings == 'GB2312' or encodings == 'gb2312':
        encodings = 'GBK'
    return response.decode(encodings)

'''
使用urlopen()方法把站点返回的内容存在到不同的文件中
'''
length = len(urls_list)
for index in range(length):
    if index < length -1:
        url = urls_list[index][:-1]
    else:
        url = urls_list[index]
    p_start = re.compile('\\bwww\.\\b')
    p_end = re.compile('\\b\.com\\b')
    index_start = p_start.search(url).end()
    index_end = p_end.search(url).start()
    file_name = url[index_start: index_end] + '.txt'
    with open(r'spider/02/'+file_name,'w',errors='ignore') as f:
        text = getSome(url)
        print(url)
        f.write(text)

