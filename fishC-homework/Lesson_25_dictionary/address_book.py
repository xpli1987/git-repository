#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#__author__:ThunderRuss_XPLI
'''
使用字典编写一个通讯录程序
1、可以查询联系人资料
2、可以新建联系人
3、可以删除联系人
4、退出通讯录程序
'''
print(\
    '''
    |--- 欢迎进入通讯录程序 ---|
    |--- 1：查询联系人资料  ---|
    |--- 2：播放新的联系人  ---|
    |--- 3：删除已有联系人  ---|
    |--- 4：退出通讯录程序  ---|
    '''\
    )

#新建一个字典用来存储通讯录
add_book = dict()

#查询联系人资料
def search_info(name):
    if not add_book.get(name):     #确认是否存在此联系人
        print('没有此联系人资料',end='\n\n')
    else:
        print('%s：%s'%(name,add_book[name]),end='\n\n')  #如果存在此联系人则返回联系人的资料

#插入联系人
def new_linkman(name):
    if add_book.get(name):
        print('您输入的姓名在通讯录中已存在 --->>','%s：%s' %(name,add_book.get(name)))
        choice = input('是否修改用户资料(YES/NO):').upper()
        if choice == 'YES':
            new_phone_num = input('请输入用户联系电话：')
            add_book[name] = new_phone_num
            print('联系人资料修改成功！',end='\n\n')
    else:
        phone_num = input('请输入用户联系电话：')
        add_book[name] = phone_num
        print('联系人资料添加成功！',end='\n\n')

#删除联系人
def del_linkman(name):
    if add_book.get(name):
        add_book.pop(name)
        print('联系人资料删除成功！', end='\n\n')
    else:
        print('通讯录无此联系人资料可删除！',end='\n\n')

def main():
    while True:
        # 用户输入指令，识别需要进行的操作
        user_order = input('请输入相关的指令代码：')
        if user_order == '1':
            name = input('请输入联系人姓名：')
            search_info(name)
            continue
        elif user_order == '2':
            name = input('请输入联系人姓名：')
            new_linkman(name)
            continue
        elif user_order == '3':
            name = input('请输入联系人姓名：')
            del_linkman(name)
            continue
        elif user_order == '4':
            print(\
                '''
                |--- 感谢使用通讯录程序  ---|
                '''\
                )
            break
        else:
            print('输入指令错误！')
            continue

if __name__ == '__main__':
    main()