#! /usr/bin/env python
#coding=GB18030
import ConfigParser
import os
import time
from pywinauto import mouse as ms
import auto_lib as pywin 
import locFun as location


app=pywin.Pywin()

@location._getName
def login(tl_dir,tl_name,uName,key):
#     _dir = os.getcwd()
    app.start(tl_dir,tl_name)
    window_name =u'登录--试验自动测试管理系统'
    app.connect(window_name)
    app.input(window_name, 'Combox', uName)
#    controller="Edit1"
    #  app.pr(window_name)
    app.Sendk('TAB', 1)
#     time.sleep(2)
    app.input(window_name,'Edit1', key)
    app.click(window_name, u'登 陆')
#判断QuikLab3.0是否弹出    
    window_name =u'QuiKLab V3.0'
    app._wait(window_name,'active',10, 2)
    app.connect(window_name)
#     os.chdir(_dir)
    
#新建工程
@location._getName
def creat_pro(window_name,pro_name):
    app.click(window_name,u'新建项目')
#     app.click(window_name, 'Edit1')
    app.Sendk('TAB', 3)
    app.input(window_name,'Edit1',pro_name)
    app.click(window_name,u'确定') #确定
#     SendKeys.SendKeys('{1}')

@location._getName
def load_pro(window_name,pro_name):
    app.click(window_name,u'加载项目')
#     time.sleep(1)
    app.click(window_name, 'Edit1')
    app.input(window_name,'Edit1',pro_name)
    app.click(window_name, u'单机测试')
#     app.Sendk('TAB', 2)
    app.click(window_name,u'确定')
    time.sleep(2)
#判断工程是否加载成功
    if 'name' in app.texts(window_name, 'statics2'):
        pass
    else:
        print "pro failed to load!!!"
        exit()

#卸载工程
@location._getName        
def unload_pro(window_name):
    app.click(window_name,u'卸载项目')
    time.sleep(1)
    app.click(window_name,u'是')
    if len(app.texts(window_name, 'statics2')) != 0:
        print 'unload failed!!!'
        exit()

#添加总线
@location._getName
def add_Bus(window_name):
    app.click(window_name,u'环境配置') #进入环境配置 
    ms.right_click(coords=(1577, 492))
    app.Sendk('DOWN', 1)
    app.Sendk('ENTER',1)
#判断弹出"添加总线"窗口 
    app._wait_child(window_name, u'添加总线', 'ready', 10, 2)
    app.click(window_name, 'ComboBox1')
    app.input(window_name, 'ComboBox1', 'tcp')#添加 TCP/IP协议
    app.Sendk('ENTER',1)
    app.click(window_name, u'确定') #确定

#添加设备  
@location._getName
def add_dev(window_name):
    app.right_click(window_name,'Pane2')
    app.Sendk('DOWN', 3)
    app.Sendk('ENTER',1) #选择添加设备
    app._wait_child(window_name, u'添加设备', 'ready', 10, 2)

#添加目标机
@location._getName
def add_tar(window_name):
    app.click(window_name, 'ComboBox1')
    app.Sendk('UP', 1)
    app.Sendk('ENTER', 1)

#添加IP
    app.click(window_name, 'Edit2')
    app.Sendk('RIGHT', 1)
    time.sleep(1)
    app.input(window_name, 'Edit2', '19')
    app.Sendk('2', 1)
    app.input(window_name, 'Edit3', '16')
    app.Sendk('8', 1)
    app.input(window_name, 'Edit4', '1')
    app.Sendk('.', 1)
    app.input(window_name, 'Edit5', '5')
    app.click(window_name, u'确定')#确定
    

@location._getName
def close(window_name,contorl):
    app.click(window_name,contorl)
    app.click(window_name,u"确定")
    
def closeLogin(window_name,contorl):
    app.click(window_name,contorl)
    
#界面配置数据库相关信息  
def confDataBase(tl_dir,tl_name):
    app.start(tl_dir,tl_name)
    window_name =u'登录--试验自动测试管理系统'
    app.connect(window_name)
    app.click(window_name, u"配置")     #点击配置按钮
    app.click(window_name, u"数据库")    #点击数据库
    time.sleep(2)
    app.click(window_name, 'Edit3')        #选择IP地址输入框的第一位数字
    app.input(window_name, 'Edit3', '^a')  #全选输入框的第一位数字
    app.input(window_name, 'Edit3', '19')  #输入IP地址中的第一位数字
    app.Sendk('2', 1)
    app.click(window_name, 'Edit4')
    app.input(window_name, 'Edit4', '^a')
    app.input(window_name, 'Edit4', '16')
    app.Sendk('8', 1)
    app.click(window_name, 'Edit5')
    app.input(window_name, 'Edit5', '^a')
    app.input(window_name, 'Edit5', '1')
    app.click(window_name, 'Edit6')
    app.input(window_name, 'Edit6', '^a')
    app.input(window_name, 'Edit6', '22')
    app.Sendk('6', 1)
    app.click(window_name, u"应用")    #点击应用按钮
    app.click(window_name, u"确定")    #点击确定按钮
    app.click(window_name, u"确定")
    app.click(window_name, u'退出')    #点击退出
    
#----------------------------------------文件/数据库操作-------------------------------------------------
#读取配置文件
def readIniConfig(softName):
#     print softName
    readini = ConfigParser.ConfigParser()
    _file = '../data/mainConfig.ini'
    if os.path.exists(_file):
        pass
    else:
        os.chdir('data')     
    readini.read(_file)
    section = readini.sections()
#     print section
    for sectionInfo in section:
        if sectionInfo in softName:
            softWindowName = readini.get(sectionInfo,"softWindowName")
            softSetupdir = readini.get(sectionInfo,"softSetupDir")
            softLabname = readini.get(sectionInfo,"softLabName")
            softUserName = readini.get(sectionInfo,"softUserName")
            softPwd = readini.get(sectionInfo,"softPwd")
            softProjectName = readini.get(sectionInfo,"softProjectName")
        _list=[softWindowName,softSetupdir,softLabname,softUserName,softPwd,softProjectName]
    return _list

if __name__=='__main__':
    pass
#     app=pywin.Pywin()
#     tl_dir = r'D:\QuiKLab3.0'
#     tl_name = r'D:\QuiKLab3.0\MainApp.exe'   
#     login(tl_dir,tl_name,'cx','1')
#     time.sleep(5)
#     window_name =u'QuiKLab V3.0'
#     app.connect(window_name)
#     time.sleep(5)
#     creat_pro(window_name,'test_name120')
#     unload_pro(window_name)
#     load_pro(window_name, 'test_name120')
#     add_Bus(window_name)
#     add_dev(window_name)
#     add_tar(window_name)
#     result=ckname.checkName('cl123')
#     print result
#     if result == 0:
#         print "ProName had exist！！！"
#         exit()
    readIniConfig('QuikLab3.0')