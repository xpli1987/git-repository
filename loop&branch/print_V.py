#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
通过打印*的符号来组成字母“V”
'''


n = 5
for x in range(1,(n+1)//2+1):
    if x == (n+1)//2:
        print(' '*(x-1)+"*"+' '*(x-1))
    else:
        print(' '*(x-1)+"*"+' '*(n-(x-1)*2-2)+'*'+" "*(x-1)+'Hello')
