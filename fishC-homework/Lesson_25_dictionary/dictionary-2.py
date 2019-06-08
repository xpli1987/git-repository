#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
用字典保存员工工号，姓名和性别
'''
data = 'wx325409,黎小平,男'
Mydict = dict()
(Mydict['id'],Mydict['name'],Mydict['sex']) = data.split(',')

print('ID:  '+ Mydict['id'])
print('Name:  '+ Mydict['name'])
print('Sex:  '+ Mydict['sex']