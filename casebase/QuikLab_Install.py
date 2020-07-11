#! /usr/bin/env python
#coding=GB18030
import getpass
import os,sys
import re
import threading
import time
from pywinauto import application 
import locFun as location
import getReg
from casebase import getLatestRev

reload(sys)
sys.setdefaultencoding('GB18030')

username = getpass.getuser()    #��ȡ�����û���
despath='C:\\Users\\%s\\temp\\'%username    
if not os.path.exists(despath):             #������ʱ��װ�ļ���
    os.mkdir(despath)     
appPath = " " 

print despath
time.sleep(1)

#-------------�ӷ������������²��԰汾��c:\\user\\%user\\temp-------------
def cpFile(_type):
    srcFile=getLatestRev.getRev(_type)  #�����ļ����ͻ�ȡ���°汾��ַ
    t=srcFile.split('\\')[-1]           #��ȡ�ļ�����
    if t in os.listdir(despath):        #��ʱ��װ�ļ���Ŀ¼�²����Ƿ����������°汾
        print "%s file has exist!"%t
        return srcFile
    else:
        os.system('copy %s %s'%(srcFile,despath))   #�����°汾��װ�ļ���������ʱ��װ�ļ���
        with open('temp','w') as f:                     #������Ϻ󽫱��д��1
            f.write('1')                                #������ɺ����ɱ���ļ�temp������Ϊ"1"
        print "copy done"
        return srcFile  

#-------------��Ĭ��װ-------------
def _install():
    global fileName
    fileName=cpFile('exe').split('\\')[-1]           #ִ��copy��������װ��������д��appFile.txt
    appFile=despath+'appFile.txt'   
    with open(appFile,'w') as f:
        f.write(fileName)
    filePath=despath+'\\'+fileName          #��ȡ��װ�ļ�·��

    os.system('%s /silent'%filePath)        #��Ĭ��װ
    global appPath
    appPath = getReg.getRegVal("applicationPath") #��ע����ȡ��װ·��


#-------------��Ĭж��-------------
def _uninstall():
    os.system('%s\unins000.exe /silent'%appPath)            #��Ĭж��
    path = appPath + "\\MainApp.exe"
#     path='D:\QuiKLab3.0\MainApp.exe'
    if os.path.exists(path):
        print "unInstall fail!!!"           #��װ�ļ�������ж��ʧ��
        exit()
    else:
        print "unInstall successful������"
        
#-------------��鰲װ�Ƿ�ɹ�-------------
def _check(window_name):
    app=application.Application()
    i=1
    while i<20:                             #�����ڿ��������ɾ������ļ�temp����ѭ��
        if os.path.isfile('temp'):
            os.remove('temp')
            break
        time.sleep(1)
        i+=1
    time.sleep(5)
    try:
        app.connect(title = window_name)        #��ȡ��װ��������
    except:
        print "connect failed!"
        exit()
    app[window_name].wait('exists', 10, 2)      #�жϰ�װ�����Ƿ����

    flag=despath+'tag.txt'          
    with open(flag,'w') as f:                   #����װ�Ƿ�ɹ���־д��tag.txt,Ĭ��д��1
        f.write('1')   
    try:
        app[window_name].wait_not('exists', 60, 2)   #�ж��Ƿ�װ���
        _path = appPath + "\\MainApp.exe"
        print _path
        if os.path.exists(_path):                    #��װ��ִ���ļ��Ƿ����
            print 'Install Successfully!'
        else:
            print 'Install fail'
            with open(flag,'w') as f:           #��װʧ����0д��tag.txt
                f.write('0')   
            exit()
    except:
        print "Install Fail"
        with open(flag,'w') as f:
            f.write('0') 
        killName=fileName.replace('exe','tmp')      
        print "kill process:",killName
        os.system('taskkill /IM %s /F'%killName)        #��װʧ�ܹرհ�װ����
        exit()

        
@location._getName 
def _checkInstall():
    threads=[]                              #���̼߳��
    t1 = threading.Thread(target=_install)   #��һ���߳�Ϊinstall
    threads.append(t1)
    t2 = threading.Thread(target=_check,args=(u'��װ - QuiKLab',)) #�ڶ����߳�Ϊ_check
    threads.append(t2)
    for t in threads:
        t.setDaemon(True)
        t.start()                           #�������߳�
#     print threading.enumerate()
    for i in threads:
        i.join() 
        
if __name__=='__main__':
    _checkInstall()
#     pass
#     _uninstall()
