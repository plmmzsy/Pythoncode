# -*- coding = utf-8 -*-
# Author:ZhouShuyu
# @Time : 2021/8/19 14:54
# @File : p6_for_loop.py

'''
for i in range(5):  #for循环的基本使用方式，可以打印 0 1 2 3 4
    print(i)
'''

'''
for i in range(0,10,3):   #表示从 0 开始到 10 ，步进值为 3 .打印结果 0 3 6 9 ，每次加 3 相当于 for(int i=0;i<10;i+=3)
    print(i)
'''

'''
for i in range(-10,-100,-30) : #结果 -10 -40 -70
    print(i)
'''

'''
name = "kunming"

for x in name :  #会依次打印kunming里的每个字母
    print(x,end="\t")
'''

a = ["aa","bb","cc","dd"]
for i in range(len(a)): #加入len() 可以获取数组元素个数
    print(i,a[i])



