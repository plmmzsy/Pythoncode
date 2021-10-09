# -*- coding = utf-8 -*-
# Author:ZhouShuyu
# @Time : 2021/9/7 16:15
# @File : demo2_List2.py

'''
#增： append
namelist = ["zhang","wang","li"]
print("-------增加前·名单列表的数据--------")

for name in namelist :
    print(name)

print("-------增加后·名单列表的数据--------")
nametemp = input ("请输入增加的内容：")
namelist.append(nametemp)   #在末尾追加一个元素


for name in namelist :
    print(name)
'''
'''
a=[1,2]
b=[3,4]
a.append(b)  #将列表b当做一个元素追加到a中
print(a)

a.extend(b)   #将b列表中的每一个元素逐一追加到a列表中
print(a)
'''


#增：  insert

a = [0,1,2]
a.insert(1,3)  #第一个元素表示下标，第二个表示元素（把 3 作为数值插入 a 中位置为 1 的地方）
print(a)       #insert：指定下标位置插入元素

'''
#删
movieName = ["加勒比海盗","骇客帝国","指环王","速度与激情"]

print("-------增加前·电影列表的数据--------")

for name in movieName :
    print(name)

#del movieName[2]  #在指定位置删除一个元素
#movieName.pop()  #弹出末尾最后一个元素

movieName.remove("指环王") #删除指定内容的元素,如果有重复就删除第一个


print("-------删除后·电影列表的数据--------")
for name in movieName:
    print(name)
'''

'''
#改：
namelist = ["zhang","wang","li"]

print("-------修改前·名单列表的数据--------")
for name in namelist :
    print(name)

namelist[1] = "小红"

print("-------修改后·名单列表的数据--------")
for name in namelist :
    print(name)
'''



#查： in /not in
namelist = ["zhang","wang","li"]
findName = input("请输入你要查找的学生姓名：")

if findName in namelist:
    print("在学员名单中找到了相同的名字")
else:
    print("没有找到")




