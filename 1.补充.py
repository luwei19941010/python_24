#-*-coding:utf-8-*-
# Author:Lu Wei

#日志
    #用户：
    #程序员
        #统计用的
        #用来做故障排除的 debug
        #用来记录错误，完成代码的优化的
    #basiconfig
        #使用方便
        #不能实现编码问题，不能同时向文件和屏幕输出
        #logging.debug  logging.warning
    #logger对象
        #复杂
            #创建一个logger对象
            #创建一个文件操作符
            #创建一个屏幕操作符
            #创建日志格式


            #给logger对象绑定 文件操作符
            #给logger对象绑定 屏幕操作符
            #给文件操作符 设定格式
            #给屏幕操作符 设定格式

            #用logger对象操作

# import logging
#
# logger=logging.getLogger('loggername')
# logger1=logging.getLogger('loggername')
# fh=logging.FileHandler('a.log',mode='a',encoding='utf-8')
# sh=logging.StreamHandler()
# fh1=logging.FileHandler('a1.log',mode='a',encoding='utf-8')
# sh1=logging.StreamHandler()
# formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(module)s: %(message)s')
# logger.addHandler(fh)
# logger.addHandler(sh)
# logger1.addHandler(fh1)
# logger1.addHandler(sh1)
# sh.setFormatter(formatter)
# sh1.setFormatter(formatter)
# logger.error('asdasd')
# logger1.error('asdaasdasdsd')



# from collections import OrderedDict
# d=dict([('a',1),('b',2),('c',3)])
# print(d)
# odic=OrderedDict([('a',1),('b',2),('c',3)])
# for a,b in odic.items():
#     print(a,b)

# from collections import namedtuple #可命名元组
# Course=namedtuple('Course',['name','price','teacher'])#class 类
# python=Course('python','19800','alex')#对象
# print(python)
# print(python.name)
# print(python.price)
    #创建一个类，这个类没有方法，所以属性的值都不能修改

#什么是模块，什么是包
    #什么是模块
        #py文件，写好了的 对程序员直接提供某方面功能的文件
        #import
        #from..import
    #什么是包
        #文件夹 存储了多个py文件的文件夹
        #如果导入的是一个包，这个包里的模块默认是不能用的
        #导入一个包相当于执行__init__.py文件中的内容


#
# ab='123'
# import sys,os
# print(sys.modules)
# print(getattr(sys.modules[__name__],'ab'))
# os.path.getsize()


import os


def get_file_size(file_path, size=0):
    for root, dirs, files in os.walk(file_path):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
            # 加上下面一行打印所有文件
            #print(f)
    return size


def main(file_path, size=0):
    return get_file_size(file_path, size)


if __name__ == '__main__':
    # 打印当前目录大小
    print(main('.', 0))
    # 如需测试可以将下面的路径换成您机器中的路径
    path = r'C:\Users\davidlu\PycharmProjects\luwei-Knightsplan'
    print(main(path, 0))

a=r'C:\Users\davidlu\PycharmProjects\luwei-Knightsplan\day24'
b='a.log'
print(os.path.join(a,b))

import datetime
datetime.datetime.strftime()
datetime.datetime.timestamp()
datetime.datetime.fromtimestamp()

import shutil
shutil.make_archive()