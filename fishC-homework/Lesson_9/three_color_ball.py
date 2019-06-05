#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
三色球问题：
有红、黄、蓝三种颜色的球，其中红球 3 个，黄球 3 个，绿球 6 个。
先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出球的各种颜色搭配。
'''
print('red\tblue\tgreen')
for red in range(0,4):
    for blue in range(0,4):
        for green in range(2,7):
            if red + blue + green == 8:
                print(red,'\t' ,blue,'\t',green,'\t')