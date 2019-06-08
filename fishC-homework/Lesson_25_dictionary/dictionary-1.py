#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
尝试一下将数据（'F': 70, 'C': 67, 'h': 104, 'i': 105, 's': 115）创建为一个字典并访问键 'C' 对应的值？
'''

tuple1 = ('F:70', 'C: 67', 'h: 104', 'i: 105', 's: 115')
tmp = []

for each in tuple1:
    tmp.append(each.split(':'))

print (tmp)

dict1 = dict(tmp)
print (dict1)
print (dict1['C'])
