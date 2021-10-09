# -*- coding = utf-8 -*-
# Author:ZhouShuyu
# @Time : 2021/9/8 21:59
# @File : demo2_List3.py


list = ["a","b","c","a","b"]

'''
print(list.index("a",1,4))  #可以查找指定下标范围的元素并返回找到对应数据的下标

print(list.index("a",1,3)) #找不到会报错，说明范围区间左闭右开


print(list.count("c"))  #统计每个元素出现几次
'''

'''
#排序和反转
a = [1,4,2,3]
print(a)

a.reverse() #将列表所有元素反转
print(a)

a.sort() #排序，升序：从低到高
print(a)

a.sort(reverse=True) #降序排列
print(a)
'''


#schoolNames = [[],[],[]] #有三个元素的空列表，每个元素都是空列表

schoolName=[["北京大学","清华大学"],["南开大学","天津大学","天津师范大学"],["山东大学","中国海洋大学"]]

print(schoolName[0][0]) #第一个列表里的第一个元素

import random
offices = [[],[],[]]

names = ["A","B","c","D","E","F","G","H"]

i=1 #定义办公室编号从1开始
for name in names:
    index = random.randint(0,2)  #定义一个变量来随机分配办公室
    offices[index].append(name)  #把老师通过index变量随机分配到办公室中，append追加
for office in offices:
    print("办公室%d 的人数：%d"%(i,len(office)))
    i+=1
    for name in office:
        print("%s"%name,end="\t") #\t是空格
    print("\n")  #每打印一次换一次行
    print("-"*20) #分割线
