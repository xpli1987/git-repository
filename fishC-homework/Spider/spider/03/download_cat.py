#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
#__DATE__:2019-07-05
'''
在http://placekitten.com网站上下载一只猫的图片。该网站支持http://placekitten.com/宽/高
来查看一张猫的图片，图片大小为url中的宽和高
需求：
1、让用命输入尺寸，默认尺寸为400*600；
2、让用户指定图片保存位置
'''
import urllib.request
import easygui as eg
import os

def main():
    msg = '请填写猫的尺寸'
    title = '下载一只猫的图片'
    cat_size = width, height = 400, 600
    field_name = ['宽:', '高:']
    field_value = eg.multenterbox(msg,title,field_name,cat_size)
    while 1:
        if field_value == None: #如果用户没有填写尺寸则break
            break
        errmsg = ''

        try:
            width = int(field_value[0].strip())
        except:
            errmsg = '宽必须为整数！'

        try:
            height = int(field_value[1].strip())
        except:
            errmsg = '高必须为整数！'

        if errmsg == '':
            break
        field_value = eg.multenterbox(errmsg,title,field_name,cat_size)

    url = r'http://placekitten.com/%d/%d'%(width, height)
    response = urllib.request.urlopen(url).read()

    file_path = eg.diropenbox('请选择保存图片位置')

    if file_path:
        file_name = file_path + os.sep + 'cat_%d_%d.jpg' %(width, height)
    else:
        file_name = 'cat_%d_%d.jpg' %(width, height)

    with open(file_name, 'wb') as f:
        f.write(response)

if __name__ == '__main__':
    main()