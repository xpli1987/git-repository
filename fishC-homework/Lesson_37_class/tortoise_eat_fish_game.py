#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
乌龟吃鱼游戏：
假设游戏场景为范围（x, y）为0<=x<=10，0<=y<=10
游戏生成1只乌龟和10条鱼
它们的移动方向均随机
乌龟的最大移动能力是2（Ta可以随机选择1还是2移动），鱼儿的最大移动能力是1
当移动到场景边缘，自动向反方向移动
乌龟初始化体力为100（上限）
乌龟每移动一次，体力消耗1
当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20
鱼暂不计算体力
当乌龟体力值为0（挂掉）或者鱼儿的数量为0游戏结束
解题思路：
1、创建一个乌龟类：
1）移动：随机移动1或者2，碰墙后向反方向移动
2）体力消耗：初始体力为100，移动1次消耗1
3）吃鱼：乌龟吃掉鱼后体力加20
4）死亡：当乌龟的体力为0时死亡
5）初始化乌龟属性及位置
2、创建一个鱼类：
1）移动：最大移动能力为1，碰墙后向反方向移动
2）死亡：当鱼被乌龟吃掉时死亡
3）初始化鱼的位置
'''
import random,time

#定义乌龟类
class Tortoise:
    #初始化乌龟位置和饥饿度
    def __init__(self):
        self.hunger = 100
        self.position = (random.randint(0,10),random.randint(0,10))
        print(self.position)

    #定义乌龟的移动方法
    def move(self):
        self.x = random.randint(-2,2) #X轴移动位置
        self.y = random.randint(-2,2) #Y轴移动位置
        #如果乌龟下一次移动位置超过游戏场景，则向反方向移动
        if self.position[0] + self.x < 0 or self.position[0] + self.x > 10:
            self.x = -self.x
        if self.position[1] + self.y < 0 or self.position[1] + self.y > 10:
            self.y = -self.y
        #乌龟移动后的位置：
        self.position = (self.position[0] + self.x, self.position[1] + self.y)
        print('乌龟当前位置为：',self.position)
        #乌龟移动后的饥饿度：
        self.hunger -= 1
        print('乌龟当前饥饿度为：',self.hunger)
        return self.position,self.hunger

    #定义乌龟吃鱼的方法
    def eat(self):
        self.hunger += 20
        if self.hunger >= 100:
            self.hunger = 100
        print('乌龟吃到了一条鱼，当前饥饿度为：',self.hunger)
        return self.hunger

    #定义乌龟死亡的方法
    def death(self):
        print('乌龟体力消耗完了也没有吃到鱼，饿死了....')

#定义鱼的类
class Fish:
    #初始化鱼的位置
    def __init__(self):
        self.position = (random.randint(0,10),random.randint(0,10))
        print(self.position)

    def move(self):
        self.x = random.randint(-1, 1)  # X轴移动位置
        self.y = random.randint(-1, 1)  # Y轴移动位置
        # 如果鱼下一次移动位置超过游戏场景，则向反方向移动
        if self.position[0] + self.x < 0 or self.position[0] + self.x > 10:
            self.x = -self.x
        if self.position[1] + self.y < 0 or self.position[1] + self.y > 10:
            self.y = -self.y
        # 鱼移动后的位置：
        self.position = (self.position[0] + self.x, self.position[1] + self.y)
        print(self.position)
        return self.position

    def death(self,name):
        self.name = name
        print('%s被乌龟吃掉了！'% self.name)

def main():
    #生成一只乌龟
    t = Tortoise()
    #生成十条鱼
    fish_dict = dict()
    for num in range(10):
        for fish_name in ['青鱼','喜头鱼','鲤鱼','鲫鱼','金枪鱼','孔雀鱼','红剑鱼','神仙鱼','金鱼','六间鱼']:
            print('生成了一条',fish_name)
            fish = Fish()
            fish_dict[fish_name] = fish
    # print(fish_dict)
    # fish_dict.pop('金枪鱼')
    #存放被吃掉的鱼
    dead_fish = []
    while True:
        #判断游戏结束
        if t.hunger == 0:
            t.death()
            print('游戏结束！！！')
            break
        if len(fish_dict) == 0:
            print('游戏结束！！！')
            break
        #判断乌龟是否抓到了鱼
        for each_fish in fish_dict.keys():
            if t.position == fish_dict[each_fish].position:
                fish_dict[each_fish].death(each_fish)
                dead_fish.append(each_fish)
                t.eat()
        if dead_fish != 0:
            for each_fish in dead_fish:
                # print(each_fish)
                # print(fish_dict[each_fish])
                fish_dict.pop(each_fish)
            dead_fish = []
        time.sleep(1)
        t.move()
        for each_fish in fish_dict.keys():
            fish_dict[each_fish].move()

if __name__ == '__main__':
    main()