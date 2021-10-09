# -*- coding = utf-8 -*-
# Author:ZhouShuyu
# @Time : 2021/9/14 9:36
# @File : demo3_tuple.py

'''
tup1=() #创建空元祖
print(type(tup1))

tup2=(50,) #只有一个数值的时候要加逗号隔开才能被判定为元组
print(type(tup2))
'''

tup1 = ("abc","def",2000,2020)

print(tup1[0])
print(tup1[-1]) #访问末尾元素
print(tup1[1:5]) #即使长度不到 5 也不会报错，左闭右开（第五个不访问）

'''
#增（和另外的元组做一个连接,相当于新建了元组）
tup1 = (12,34,56)
tup2 = ("abc","xyz")

tup = tup1 + tup2
print(tup)
'''

#删
tup1 = (12,34,56)
print(tup1)
del tup1 #删除了整个元组变量


#改
#tup1 = (12,34,56)
#tup1[0]=100 #报错，不允许修改


