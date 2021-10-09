# -*- coding = utf-8 -*-
# Author:ZhouShuyu
# @Time : 2021/9/14 9:54
# @File : demo3_Dict.py

#字典的定义
'''
info = {"name":"吴彦祖","age":18}
'''

#字典的访问
'''
print(info["name"])
print(info["age"])
'''

#访问了不存在的键
#print(info["gender"]) #直接访问会报错

#print(info.get("gender")) #使用 get 方法，没有找到对应的键，默认返回：none

#print(info.get("age","20")) #能找到的时候默认值不会发挥作用
#print(info.get("gender","m")) #没有找到可以设定默认值

#增
'''
info = {"name":"吴彦祖","age":18}
newID=input("请输入新的学号：")
info["id"] = newID

print(info["id"])
'''

#删
#[del]
# info = {"name":"吴彦祖","age":18}
# print("删除前：%s"%info["name"])
#
# del info["name"]

#print("删除后：%s"%info["name"])

'''
info = {"name":"吴彦祖","age":18}
print("删除前：%s"%info["name"])

del info

#print("删除后：%s"%info) #删除字典后再访问报错

#[clear] 清空

info = {"name":"吴彦祖","age":18}
print("删除前：%s"%info["name"])

info.clear()

print("清空后：%s"%info)
'''

#改
'''
info = {"name":"吴彦祖","age":18}

info["age"]=20

print("修改后：%s"%info["age"])
'''

#查
'''
info = {"id":1,"name":"吴彦祖","age":18}

print(info.keys())   #得到所有的键（列表）

print(info.values())  #得到所有的值（列表）

print(info.items())  #得到所有的项（列表），每个键值对是一个元祖
'''

#遍历所有的键
'''
for key in info.keys():
    print(key)
'''

#遍历所有的值
'''
for value in info.values():
    print(value)
'''

'''
for key,value in info.items():
    print("key=%s,value=%s"%(key,value))
'''

#使用枚举函数同时拿到列表中的下标和元素内容
mylist=["a","b","c","d"]

for i,x in enumerate(mylist):
    print(i,x)


