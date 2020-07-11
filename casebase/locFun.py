#! /usr/bin/env python
#coding=GB18030
import os
import sys
import time
import dirLocation

#-------------获取当前执行函数名称并判断执行是否正常-------------
def _getName(func):
    def wrapper(*args,**kwargs):
        path = dirLocation.searchDir('report') #获取report路径
        _file=path+'/log.txt'
        print _file
        with open(_file,'a') as f:  #打开log.txt写入
            t=time.strftime('%Y%m%d_%H%M%S',time.localtime((time.time())))   #获取当前时间
            f.write('%s '%t)    #写入当前时间
            f.write(func.__name__)  #写入模块名称
            f.write(' ')
            print func.__name__
        func(*args,**kwargs)
        with open(_file,'a') as f:
            f.write('pass')             #写入测试结果
            f.write('\n')
    return wrapper

if __name__=='__main__':
    pass