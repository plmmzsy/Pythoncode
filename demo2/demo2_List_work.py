# -*- coding = utf-8 -*-
# Author:ZhouShuyu
# @Time : 2021/9/8 22:40
# @File : demo2_List_work.py

products = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]

print("----- 商品列表 -----")

index = len(products)
for index in range(0,index):
    product = products[index]
    print(index,product[0],product[1])

shopping_list= []  #定义一个空列表作为购物车

while 1: # 建立一个无限循环
    user = input("您想购买哪件商品，请输入编号(输入q停止添加并打印商品名单)：")
    if user.lower() == "q":
        print("您的购物车里现在有：",shopping_list)
        exit(0)
    else:
        name = products[int(user)][0]  #定义列表中的商品名称
        shopping_list.append(name)





