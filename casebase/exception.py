#! /usr/bin/env python
#coding=GB18030
import os
import sys
import time
import dirLocation
from PIL import ImageGrab

#װ����
def _exception(func):
    def wrapper(*args):
        try:
            func(*args)                 #���к���
        except:
            path=dirLocation.searchDir('report')            #��ȡreport·��
            _file= path + '\log.txt'                        #��ȡlog.txt·��
            with open(_file,'a') as f:                      #log.txt��д��fail
                f.write('fail')                             
                f.write('\n')
            now=time.strftime('%Y%m%d_%H%M%S',time.localtime((time.time())))   #��ȡ��ǰʱ��
            im = ImageGrab.grab()                           #��ȡ��ͼ����
            lists =[]
            fileNames = os.listdir(path)
            for fileName in fileNames:                      #��ȡreport·��������Ŀ¼����
                if os.path.isdir(os.path.join(path,fileName)):
                    lists.append(fileName)
                     
            lists.sort(key=lambda fn:os.path.getmtime(path +r"/" + fn))     #��report·����Ŀ¼����������
            file_new = os.path.join(path,lists[-1])                             #file_newΪpath+��ǰ����Ŀ¼
            picFile= file_new + '/' + now+'.png'                            #��ȡͼ������
            print "screenshot:" + picFile,len("screenshot:" + picFile)    #���ڲ��Ա��������ӽ�ͼ
            im.save(picFile)                                                #�����ͼ
            exit()

    return wrapper

if __name__=='__main__':
    pass