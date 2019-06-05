#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI

n = 11
x = 0
for i in range(1,n+1):
    if i < 5:
        print(' '*(n-i) +'*'+' '*(i-1),end='\n')
    else:
        x = i
        break

#print(x)
for y in range(1,(x+1)//2+1):
    if y == (x+1)//2:
        print(' '*(y-1)+"*"+' '*(y-1))
    else:
        print(' '*(y-1)+"*"+' '*(x-(y-1)*2-2)+'*'+" "*(y-1))