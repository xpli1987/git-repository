#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
#__DATE__:2019-07-07
'''
通过百度下载图片。
需求：
1、用户可以自定义下载图片内容；
2、可以自定义下载图片尺寸
3、自定义下载图片数量
'''

from urllib import request, parse
import re
import easygui as eg
import os

#通过用户输入的关键字，尺寸大小来制作百度搜索的url
def makeUrl(keyword=None, width=None, height=None):
    parameter = {}
    print('正在制作URL')
    with open('parameter.txt', 'r') as pa:
        for each_line in pa:
            tmp = re.split('[:\n]',each_line)
            parameter[tmp[0]] = tmp[1]
    if keyword:
        parameter['word'] = parameter['oq'] = keyword
    if width:
        parameter['width'] = width
    if height:
        parameter['height'] = height
    url_data = parse.urlencode(parameter)
    url = 'https://image.baidu.com/search/index?' + url_data
    return url

def get_pic_url(url):
    print('正在生成图片下载链接！')
    response = request.urlopen(url).read().decode('utf-8')
    tmp = re.findall(r'("middleURL"):"(\S+jpg)"',response)
    pic_url = [each_item[1] for each_item in tmp]
    return pic_url

def download_pic(pic_url,filename):
    print('正在下载图片中！')
    num = 1
    for each_url in pic_url:
        res = request.urlopen(each_url).read()
        filepath = filename + os.sep + str(num) + '.jpg'
        with open(filepath, 'wb') as f:
            f.write(res)
        print('下载完成第%d张图片！！！'% num)
        num += 1


def main():
    msg = '''
          1:输入需要下载图片的关键字【*】
          2：输入图片的尺寸【*】  
          '''
    title = '搜索图片'
    fields = ['图片关键字:', '宽:', '高:']
    keyword, width, height = eg.multenterbox(msg, title, fields)
    filepath = eg.diropenbox('请选择图片保存的路径！', '选择路径', '*.jpg')
    print(filepath)
    url = makeUrl(keyword, width, height)
    pic_url = get_pic_url(url)
    download_pic(pic_url, filepath)

if __name__ == '__main__':
    main()
