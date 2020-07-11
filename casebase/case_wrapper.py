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
    window_name =u'��¼--�����Զ����Թ���ϵͳ'
    app.connect(window_name)
    app.input(window_name, 'Combox', uName)
#    controller="Edit1"
    #  app.pr(window_name)
    app.Sendk('TAB', 1)
#     time.sleep(2)
    app.input(window_name,'Edit1', key)
    app.click(window_name, u'�� ½')
#�ж�QuikLab3.0�Ƿ񵯳�    
    window_name =u'QuiKLab V3.0'
    app._wait(window_name,'active',10, 2)
    app.connect(window_name)
#     os.chdir(_dir)
    
#�½�����
@location._getName
def creat_pro(window_name,pro_name):
    app.click(window_name,u'�½���Ŀ')
#     app.click(window_name, 'Edit1')
    app.Sendk('TAB', 3)
    app.input(window_name,'Edit1',pro_name)
    app.click(window_name,u'ȷ��') #ȷ��
#     SendKeys.SendKeys('{1}')

@location._getName
def load_pro(window_name,pro_name):
    app.click(window_name,u'������Ŀ')
#     time.sleep(1)
    app.click(window_name, 'Edit1')
    app.input(window_name,'Edit1',pro_name)
    app.click(window_name, u'��������')
#     app.Sendk('TAB', 2)
    app.click(window_name,u'ȷ��')
    time.sleep(2)
#�жϹ����Ƿ���سɹ�
    if 'name' in app.texts(window_name, 'statics2'):
        pass
    else:
        print "pro failed to load!!!"
        exit()

#ж�ع���
@location._getName        
def unload_pro(window_name):
    app.click(window_name,u'ж����Ŀ')
    time.sleep(1)
    app.click(window_name,u'��')
    if len(app.texts(window_name, 'statics2')) != 0:
        print 'unload failed!!!'
        exit()

#�������
@location._getName
def add_Bus(window_name):
    app.click(window_name,u'��������') #���뻷������ 
    ms.right_click(coords=(1577, 492))
    app.Sendk('DOWN', 1)
    app.Sendk('ENTER',1)
#�жϵ���"�������"���� 
    app._wait_child(window_name, u'�������', 'ready', 10, 2)
    app.click(window_name, 'ComboBox1')
    app.input(window_name, 'ComboBox1', 'tcp')#��� TCP/IPЭ��
    app.Sendk('ENTER',1)
    app.click(window_name, u'ȷ��') #ȷ��

#����豸  
@location._getName
def add_dev(window_name):
    app.right_click(window_name,'Pane2')
    app.Sendk('DOWN', 3)
    app.Sendk('ENTER',1) #ѡ������豸
    app._wait_child(window_name, u'����豸', 'ready', 10, 2)

#���Ŀ���
@location._getName
def add_tar(window_name):
    app.click(window_name, 'ComboBox1')
    app.Sendk('UP', 1)
    app.Sendk('ENTER', 1)

#���IP
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
    app.click(window_name, u'ȷ��')#ȷ��
    

@location._getName
def close(window_name,contorl):
    app.click(window_name,contorl)
    app.click(window_name,u"ȷ��")
    
def closeLogin(window_name,contorl):
    app.click(window_name,contorl)
    
#�����������ݿ������Ϣ  
def confDataBase(tl_dir,tl_name):
    app.start(tl_dir,tl_name)
    window_name =u'��¼--�����Զ����Թ���ϵͳ'
    app.connect(window_name)
    app.click(window_name, u"����")     #������ð�ť
    app.click(window_name, u"���ݿ�")    #������ݿ�
    time.sleep(2)
    app.click(window_name, 'Edit3')        #ѡ��IP��ַ�����ĵ�һλ����
    app.input(window_name, 'Edit3', '^a')  #ȫѡ�����ĵ�һλ����
    app.input(window_name, 'Edit3', '19')  #����IP��ַ�еĵ�һλ����
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
    app.click(window_name, u"Ӧ��")    #���Ӧ�ð�ť
    app.click(window_name, u"ȷ��")    #���ȷ����ť
    app.click(window_name, u"ȷ��")
    app.click(window_name, u'�˳�')    #����˳�
    
#----------------------------------------�ļ�/���ݿ����-------------------------------------------------
#��ȡ�����ļ�
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
#         print "ProName had exist������"
#         exit()
    readIniConfig('QuikLab3.0')