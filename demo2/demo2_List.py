# -*- coding = utf-8 -*-
# Author:ZhouShuyu
# @Time : 2021/9/7 16:08
# @File : demo2_List.py

'''
namelist=[] #定义一个空列表

namelist = ["zhang","wang","li"]

print(namelist[0]) #打印第一个元素

testlist = [1,"测试"]    #列表中可以存储混合类型
print(type(testlist[0]))
print(type(testlist[1]))

'''

namelist = ["zhang","wang","li"]
for name in namelist:   #遍历
    print(name)

print(len(namelist))  #获取列表长度

length = len(namelist)
i = 0
while i<length:
    print(namelist[i])
    i+=1
