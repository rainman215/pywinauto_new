#! /usr/bin/env python
#coding=GB18030
import os
import sys
import time
import dirLocation
from PIL import ImageGrab

#装饰器
def _exception(func):
    def wrapper(*args):
        try:
            func(*args)                 #运行函数
        except:
            path=dirLocation.searchDir('report')            #获取report路径
            _file= path + '\log.txt'                        #获取log.txt路径
            with open(_file,'a') as f:                      #log.txt中写入fail
                f.write('fail')                             
                f.write('\n')
            now=time.strftime('%Y%m%d_%H%M%S',time.localtime((time.time())))   #获取当前时间
            im = ImageGrab.grab()                           #获取截图对象
            lists =[]
            fileNames = os.listdir(path)
            for fileName in fileNames:                      #获取report路径下所有目录名称
                if os.path.isdir(os.path.join(path,fileName)):
                    lists.append(fileName)
                     
            lists.sort(key=lambda fn:os.path.getmtime(path +r"/" + fn))     #将report路径下目录按名称排序
            file_new = os.path.join(path,lists[-1])                             #file_new为path+当前最新目录
            picFile= file_new + '/' + now+'.png'                            #获取图像名称
            print "screenshot:" + picFile,len("screenshot:" + picFile)    #用于测试报告中增加截图
            im.save(picFile)                                                #保存截图
            exit()

    return wrapper

if __name__=='__main__':
    pass