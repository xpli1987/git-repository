#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__;ThunderRuss_XPLI
'''
水仙花数：number of daffodils
如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
输出100-999之间所有的number of daffodils
'''

for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            if c*100 + b*10 + a == c**3 + b**3 + a**3:
                print(c*100 + b*10 + a)
