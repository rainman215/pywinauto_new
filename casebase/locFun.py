#! /usr/bin/env python
#coding=GB18030
import os
import sys
import time
import dirLocation

#-------------��ȡ��ǰִ�к������Ʋ��ж�ִ���Ƿ�����-------------
def _getName(func):
    def wrapper(*args,**kwargs):
        path = dirLocation.searchDir('report') #��ȡreport·��
        _file=path+'/log.txt'
        print _file
        with open(_file,'a') as f:  #��log.txtд��
            t=time.strftime('%Y%m%d_%H%M%S',time.localtime((time.time())))   #��ȡ��ǰʱ��
            f.write('%s '%t)    #д�뵱ǰʱ��
            f.write(func.__name__)  #д��ģ������
            f.write(' ')
            print func.__name__
        func(*args,**kwargs)
        with open(_file,'a') as f:
            f.write('pass')             #д����Խ��
            f.write('\n')
    return wrapper

if __name__=='__main__':
    pass