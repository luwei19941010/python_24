#-*-coding:utf-8-*-
# Author:Lu Wei

# 1.计算文件夹的大小
# 基础：文件夹中只有文件
# 进阶：文件夹中还有文件夹，且文件夹的层数不确定
#
#
# import os,sys
# def File_big(path,size=0):
#     for paths,dir,files in os.walk(path):
#         for f in files:
#             size=size+os.path.getsize(os.path.join(paths,f))
#     return size
# # p=r'C:\Users\davidlu\PycharmProjects\luwei-Knightsplan\day24'
# p=r'C:\Users\davidlu\PycharmProjects\luwei-Knightsplan'
# print(File_big(p))
#
#
# #2.拼手气发红包
# 注意每个人抢到的钱数的概率都是均等的
# 注意抢到的金额精确到分


import random
# print(random.randint(1,100))
money=200.00
count=0
c=0
# while money!=0:
while count!=5:
    money = money-c
    if count==4:
        print(round(money,2))
        break
    a=random.uniform(0,money)
    c=round(a, 2)
    print(c)
    count+=1







'''
#4.根据代码研究super和mro的关系
class A:
    def func(self):
        print('in a')

class B(A):
    def func(self):
        print('in b')
        super().func()

class C(A):
    def func(self):
        print('in c')
        super().func()

class D(B,C):
    def func(self):
        print('in d')
        super().func()

d = D()
d.func()
#d,b,c,a
'''