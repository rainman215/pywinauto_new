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

username = getpass.getuser()    #获取本机用户名
despath='C:\\Users\\%s\\temp\\'%username    
if not os.path.exists(despath):             #建立临时安装文件夹
    os.mkdir(despath)     
appPath = " " 

print despath
time.sleep(1)

#-------------从服务器下载最新测试版本到c:\\user\\%user\\temp-------------
def cpFile(_type):
    srcFile=getLatestRev.getRev(_type)  #根据文件类型获取最新版本地址
    t=srcFile.split('\\')[-1]           #获取文件名称
    if t in os.listdir(despath):        #临时安装文件夹目录下查找是否已下载最新版本
        print "%s file has exist!"%t
        return srcFile
    else:
        os.system('copy %s %s'%(srcFile,despath))   #将最新版本安装文件拷贝到临时安装文件夹
        with open('temp','w') as f:                     #拷贝完毕后将标记写入1
            f.write('1')                                #拷贝完成后生成标记文件temp，内容为"1"
        print "copy done"
        return srcFile  

#-------------静默安装-------------
def _install():
    global fileName
    fileName=cpFile('exe').split('\\')[-1]           #执行copy，并将安装程序名称写入appFile.txt
    appFile=despath+'appFile.txt'   
    with open(appFile,'w') as f:
        f.write(fileName)
    filePath=despath+'\\'+fileName          #获取安装文件路径

    os.system('%s /silent'%filePath)        #静默安装
    global appPath
    appPath = getReg.getRegVal("applicationPath") #从注册表获取安装路径


#-------------静默卸载-------------
def _uninstall():
    os.system('%s\unins000.exe /silent'%appPath)            #静默卸载
    path = appPath + "\\MainApp.exe"
#     path='D:\QuiKLab3.0\MainApp.exe'
    if os.path.exists(path):
        print "unInstall fail!!!"           #安装文件存在则卸载失败
        exit()
    else:
        print "unInstall successful！！！"
        
#-------------检查安装是否成功-------------
def _check(window_name):
    app=application.Application()
    i=1
    while i<20:                             #当存在拷贝完成则删除标记文件temp跳出循环
        if os.path.isfile('temp'):
            os.remove('temp')
            break
        time.sleep(1)
        i+=1
    time.sleep(5)
    try:
        app.connect(title = window_name)        #获取安装窗口连接
    except:
        print "connect failed!"
        exit()
    app[window_name].wait('exists', 10, 2)      #判断安装窗口是否存在

    flag=despath+'tag.txt'          
    with open(flag,'w') as f:                   #将安装是否成功标志写入tag.txt,默认写入1
        f.write('1')   
    try:
        app[window_name].wait_not('exists', 60, 2)   #判断是否安装完成
        _path = appPath + "\\MainApp.exe"
        print _path
        if os.path.exists(_path):                    #安装的执行文件是否存在
            print 'Install Successfully!'
        else:
            print 'Install fail'
            with open(flag,'w') as f:           #安装失败则将0写入tag.txt
                f.write('0')   
            exit()
    except:
        print "Install Fail"
        with open(flag,'w') as f:
            f.write('0') 
        killName=fileName.replace('exe','tmp')      
        print "kill process:",killName
        os.system('taskkill /IM %s /F'%killName)        #安装失败关闭安装进程
        exit()

        
@location._getName 
def _checkInstall():
    threads=[]                              #多线程检测
    t1 = threading.Thread(target=_install)   #第一个线程为install
    threads.append(t1)
    t2 = threading.Thread(target=_check,args=(u'安装 - QuiKLab',)) #第二个线程为_check
    threads.append(t2)
    for t in threads:
        t.setDaemon(True)
        t.start()                           #启动多线程
#     print threading.enumerate()
    for i in threads:
        i.join() 
        
if __name__=='__main__':
    _checkInstall()
#     pass
#     _uninstall()
