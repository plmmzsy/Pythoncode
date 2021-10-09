# -*- coding = utf-8 -*-
# Author:ZhouShuyu
# @Time : 2021/8/18 17:23
# @File : game1.py

import random

a = int(input("请输入：剪刀（0），石头（1），布（2）\t" ))
print("你的输入为：%s" %a)

x=random.randint(0,2)
print("随机生成数字为：",x)

if a != 0 and a != 1 and a != 2 :
    print("输入错误，请重新输入！")
    exit()
elif a == x :
    print("平局")

elif a!=x :
    if a==0 :
        if x==1 :
            print("lose")
        else :
            print("win")
    if a==1 :
        if x==0 :
            print("win")
        else:
            print("lose")
    if a==2 :
        if x==0 :
            print("lose")
        else:
            print("win")
else :
    print("输入错误！")
    exit()