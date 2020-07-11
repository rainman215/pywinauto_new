#! /usr/bin/env python
#coding=GB18030
import ConfigParser
import logging
import os
import sys
import time
import xml.dom.minidom

from pywinauto import mouse as ms

import auto_lib as pywin 
from casebase import getReg
import exception as exp
import locFun as location
import dirLocation

app=pywin.Pywin()

#��½����
@location._getName
def login(tl_dir,tl_name,uName,key):                                     
    app.start(tl_dir,tl_name)                                               #�������
    window_name =u'��¼--QuiKLab'                 
    app._wait_child(window_name, u'�� ½', 'exists', 10, 2)                   #�жϵ�¼���Ƿ����
    app.connect(window_name)                                                #��������
#�����û���������
    app.input(window_name, 'Combox', uName)                                 #�����û���
    app.click(window_name, 'Edit1')                                         #������������
    app.input(window_name,'Edit1', key)                                     #��������
    app.click(window_name, u'�� ½')                                          #�����¼��ť
#�ж�QuikLab3.0�Ƿ񵯳�    
    window_name =u'QuiKLab'
    app._wait(window_name,'active',10, 2)
    app.connect(window_name)
#     else:
#         print "try again!"
#         app.connect(window_name)

#�½���Ŀ
@location._getName 
def creat_pro(window_name,pro_name):                                  
    app.click(window_name,u'�½���Ŀ')                                  #����½���Ŀ��ť
    app._wait_child(window_name, u'����', 'active', 10, 2)            #�ж��Ƿ񵯳��Ի���
    app.click(window_name, 'Edit2')                                     #�����Ŀ�����
    app.input(window_name, 'Edit2', '^a')                               #ȫѡ
    app.input(window_name,'Edit2',pro_name)                         #������Ŀ����
    app.click(window_name,u'ȷ��') #ȷ��                                                                                                #���ȷ��
    app.click(window_name,u'��')                                     #�����
    

#������Ŀ
@location._getName 
def load_pro(window_name,pro_name):                                     #���ع��̲���
    app.click(window_name,u'������Ŀ')                                      #���������Ŀ
    app.click(window_name, 'Edit1')                                     #���������Ŀ���� 
    app.input(window_name,'Edit1',pro_name)                             #������Ŀ����
    app.click(window_name, u'��������')                                     #�����������
    app.click(window_name,u'ȷ��')                                        #���ȷ��
    app._wait_not_child(window_name, u'��Ŀѡ��', 'ready', 10, 2)           #�ж���Ŀѡ��Ի������Ƿ񵯳�
    time.sleep(2)
    
#�ж���Ŀ�Ƿ���سɹ�
    if u'��' + pro_name + u'��' in app.texts(window_name, 'statics2'):   
        pass
    else:
        print "pro failed to load!!!"
        exit()
        
#--------------------ɾ����Ŀ�����ڲ�ʹ�ò���Ϊ�����--------------------------
def delete_pro(window_name,pro_name):                                    
    app.click(window_name,u'������Ŀ')
    app.click(window_name, 'Edit1')
    app.input(window_name,'Edit1',pro_name)
    ownerInfo = app.texts(window_name, "DataItem3")
    if ownerInfo != '':
        app.right_click(window_name, u'��������')
        app.Sendk("UP", 1)
        app.Sendk("ENTER", 1)
        app.click(window_name, u"ȷ��")
    app.right_click(window_name, u'��������')
    app.Sendk("DOWN", 2)
    app.Sendk("ENTER", 1)
    app.click(window_name, u"ȷ��")
    app.click(window_name, u"ȷ��")

#ж����Ŀ
@location._getName         
def unload_pro(window_name):                                           
    app.click(window_name,u'ж����Ŀ')                      #���ж����Ŀ
    time.sleep(1)
    app.click(window_name,u'��')
    if u'' in app.texts(window_name, 'statics2'):
        pass
    else:
        print "unload failed!!!"
        exit()

#�������
@location._getName
def add_Bus(window_name):                                          
    app.click(window_name,u'��������') #���뻷������ 
    ms.right_click(coords=(1577, 492))                      
    app.Sendk('DOWN',1)                                 #ѡ���������
    app.Sendk('ENTER',1)                                #�������
#�жϵ���"�������"���� 
    app._wait_child(window_name, u'�������', 'ready', 10, 2)
    app.click(window_name, 'ComboBox1')
    app.input(window_name, 'ComboBox1', 'tcp')#��� TCP/IPЭ��
    app.Sendk('ENTER',1)                        #ȷ��
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
def add_tar(window_name,ip):                                            
    app.click(window_name, 'ComboBox1')                 #��������˵�
    time.sleep(1)
    app.Sendk('UP', 1)              #ѡ���豸����
    app.Sendk('ENTER', 1)

#���IP
    app.click(window_name, 'Edit2')
    app.input(window_name, 'Edit2', '^a')           #Edit2ȫѡ
    app.input(window_name, 'Edit2', '19')
    app.Sendk('2', 1)
    app.click(window_name,'Edit3')
    app.input(window_name, 'Edit3', '^a')
    app.input(window_name, 'Edit3', '16')
    app.Sendk('8', 1)
    app.click(window_name,'Edit4')
    app.input(window_name, 'Edit4', '^a')
    app.input(window_name, 'Edit4', '1')
#     app.Sendk('.', 1)
    app.click(window_name,'Edit5')
    app.input(window_name, 'Edit5', '^a')
    app.input(window_name, 'Edit5', ip[3])
    app.click(window_name, u'ȷ��')#ȷ��
    
#------------------��������--------------------------
@location._getName
def run_case(window_name):
    app.click(window_name,u'��������')                  #�����������
    app._wait_child(window_name, u'��ʼ�²���', 'ready', 10, 2)  #��⿪ʼ���ԶԻ����Ƿ񵯳�
    app.click(window_name, 'ComboBox3')
    app.Sendk('DOWN', 1)
    app.Sendk('UP', 2)
    app.Sendk('ENTER', 1)
    app.click(window_name, 'TabItem1')
    app.click(window_name, 'content2*')                     #ѡ�в�������
    app.click(window_name, 'ComboBox4')                     #��������˵�
    time.sleep(1)
    app.Sendk('UP', 2)                              #ѡ���ݲ�ִ������
    app.Sendk('ENTER', 1)    
    app.click(window_name, u'��ʼ')                   #ȷ��
    try:                                                #����"��"��ť�ж϶Ի����Ƿ񵯳�
        app._wait_child_nor(window_name,u'��','ready',10,2)   
        app.click(window_name, u"��")
    except:
        pass
    time.sleep(10)
    app._wait_not_child(window_name, u'����', 'ready', 10, 2)    #�жϼ�����ť�Ƿ񵯳�
    time.sleep(2)
    app.click(window_name,u'����')                            #�������
    time.sleep(2)
    app.click(window_name, u'��������')                         #���
#     times=-2
    while True:                                     #"��һ��"�ɵ����˵������������δִ����
        try:
            app._wait_child_nor(window_name, u'��һ��', 'enabled', 10, 0.5)  #�ж���һ���Ƿ�ɵ��
            app.click(window_name, u'��һ��')
        except:
            break
#         time.sleep(0.5)

#------------------�ȶԵ��Խ��--------------------------
@location._getName
def compareRes():
    workSpace=getReg.getRegVal("workSpace")                 #��ע����ȡworkspace��ַ
    filePath='%s\\runtime\\'%workSpace
    print filePath
    fileName=time.strftime('%Y_%m_%d',time.localtime((time.time()))) +'.log'    #��־����Ϊ"��ǰʱ��"+".log"
    logFile=filePath+fileName
    print logFile
#     case.isNotIn('δͨ��',logFile, True,'���Գɹ�')
#     case.isNotIn('ʧ��',logFile,'���Գɹ�')

    despath=dirLocation.searchDir('report')

#     os.chdir(despath)
#     despath=os.getcwd()

    print despath,"..."
    os.system('copy %s %s'%(logFile,despath))         #�����Խ��������reportĿ¼��
    isNotIn('δͨ��',logFile,'���Գɹ�')                   #���Խ����ƥ�䲻��"δͨ��"�����������ͨ��


@location._getName
def close(window_name,contorl):
    app.click(window_name,contorl)
    app.click(window_name,u"ȷ��")
    
def closeLogin(window_name,contorl):
    app.click(window_name,contorl)
    
#�����������ݿ������Ϣ
@location._getName
def confDataBase(tl_dir,tl_name,connectMode):
    app.start(tl_dir,tl_name)
    time.sleep(3)
    window_name =u'��¼--QuiKLab'
    app.connect(window_name)
    app.click(window_name, u"����")     #������ð�ť
    app.click(window_name, u"���ݿ�")    #������ݿ�

    app.click(window_name, "ComboBox0")
    time.sleep(2)
    app.sendKey('^{HOME}', 1) 
    time.sleep(2)
    if (connectMode == "Զ���ļ�"):                 #�����ļ�����ģʽ�Ƿ�Ϊ"Զ���ļ�"
        app.Sendk('DOWN', 2)
        app.sendKey('{ENTER}', 1)
        app.click(window_name, 'Edit2')        #ѡ��IP��ַ�����ĵ�һλ����
        app.input(window_name, 'Edit2', '^a')  #ȫѡ�����ĵ�һλ����
        app.input(window_name, 'Edit2', '19')  #����IP��ַ�еĵ�һλ����
        app.Sendk('2', 1)
        app.click(window_name, 'Edit3')
        app.input(window_name, 'Edit3', '^a')
        app.input(window_name, 'Edit3', '16')
        app.Sendk('8', 1)
        app.click(window_name, 'Edit4')
        app.input(window_name, 'Edit4', '^a')
        app.input(window_name, 'Edit4', '1')
        app.click(window_name, 'Edit5')
        app.input(window_name, 'Edit5', '^a')
        app.input(window_name, 'Edit5', 22)     #�������ݿ��ַ226
        app.Sendk('6', 1)
    elif (connectMode == "���ݿ�"):
        app.sendKey('{DOWN}', 1)
        app.sendKey('{ENTER}', 1)
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
        app.input(window_name, 'Edit6', 22)   #�������ݿ��ַ226
        app.Sendk('6', 1)
    else:
        app.sendKey('{ENTER}', 1)
#������λ����ַ
    app.click(window_name, u'���Է�����')    #���"���Է�����"
    app.click(window_name, 'Edit1')
    app.input(window_name, 'Edit1', '^a')
#     app.Sendk('192',1)
    app.input(window_name, 'Edit1', '19')
    app.Sendk('2',1)                                    #����192
    
    app.click(window_name, 'Edit3')
    app.input(window_name, 'Edit3', '^a')
    app.input(window_name, 'Edit3', '16')
    app.Sendk('8', 1)                                   #����168
    
    app.click(window_name, 'Edit4')
    app.input(window_name, 'Edit4', '^a')
    app.input(window_name, 'Edit4', '1')                #����1
    
    app.click(window_name, 'Edit5')
    app.input(window_name, 'Edit5', '^a')
    app.input(window_name, 'Edit5', 22)
    app.Sendk('2', 1)                                   #���� 222
    
    app.click(window_name, u"Ӧ��")    #���Ӧ�ð�ť
    app.click(window_name, u"ȷ��")    #���ȷ����ť
    try:
        app._wait_child_nor(window_name,u'ȷ��','ready',10,2) 
        app.click(window_name, u"ȷ��")
    except:
        pass
#     app.click(window_name, u"ȷ��")
    app.click(window_name, u'�˳�')    #����˳�
    
#ѡ��ListBox�б��е�Item
def selectListBoxItem(window_name,listBoxName,selectItem):
    i = 0
    value = app.texts(window_name,listBoxName)       #��ȡ��ListBox�е�Item
    app.click(window_name,value[1][0])               #ѡ��չʾ�ڽ�����ListBox�еĵ�һ��Item
    app.sendKey('^{HOME}', 1)                          #���������ö�
    while True:
        value = app.texts(window_name,listBoxName)
        for i in range(0,len(value)):
            value[i] = "".join(value[i])             #���б��е�ÿ��Ԫ��ת��Ϊ�ַ���
        if selectItem in value:                      #�����Ҫѡ���Item���б���������ѡ��
            app.click(window_name, selectItem)
            break
        else:                                        #�����Ҫѡ���Item�����б����������������һҳ
            if i == 0: 
                app.sendKey('{PGDN}', 2)
                i = i + 1
            else:
                app.sendKey('{PGDN}', 1)
    
#----------------------------------------���Թ�������---------------------------------------------------
# �ж�Ԥ�ڽ����ʵ�ʽ���Ƿ����
@exp._exception 
def isNotEqual(expectResult,acutalResult,pyfilename,message):
    if expectResult != acutalResult:
        assert expectResult == acutalResult

# �ж�Ԥ�ڽ���Ƿ������ʵ�ʽ����
# @exp._exception 
def isNotIN(expectResult,acutalResult,pyfilename,message):
    if expectResult not in  acutalResult:
        logWriter(pyfilename,message);
        assert expectResult in acutalResult
        
#-------------ʵ�ʽ����Ԥ�ڽ���Ƚϣ�flagΪTrue��Ԥ��Ϊͨ������֮��Ԥ�ڲ�ͨ��-------------
#Example: isNotIn('��',logFile, True,'���Գɹ�') logFile����'��'��True����Ϊ�棬���Գɹ�
@exp._exception        
def isNotIn(expectResult,logFile,Msg):
    with open(logFile,'r') as f:
        actualResult=f.read()
#     print actualResult
    if expectResult in actualResult:
        assert expectResult not in actualResult
#             if flag is True:
#         print 'pass'
#     else:
#         print '����ʧ��'

    
#----------------------------------------�ļ�/���ݿ����-------------------------------------------------
#��ȡ�����ļ�
def readIniConfig(softName):
#     print softName
    readini = ConfigParser.ConfigParser()
    _file = sys.path[0] + r"\data\mainConfig.ini"
    if not os.path.exists(_file):
        _file = os.path.abspath("..") + r"\data\mainConfig.ini"
    
    if not os.path.exists(_file):
        _file = os.path.abspath("..\..") + r"\data\mainConfig.ini"      #ȷ�������ļ�·�� 
    readini.read(_file)                         #��ȡ�����ļ���Ϣ
    section = readini.sections()                        
#     print section
    _list=[]
    for sectionInfo in section:
        if sectionInfo in softName:                                 #ѡ��sectionΪsoftName������Ϊ������Ϣ
            for key in readini.options(sectionInfo):                #��ȡ�����ļ��ڵĵ�һ��
                if readini.get(sectionInfo,key):                    #��ȡ��һ�ж�Ӧ��ֵ����������׷�ӵ�_list
                    _list.append(readini.get(sectionInfo,key))
                else:                                               #��һ�ж�Ӧֵ�������������ļ�û����ȷ����
                    print "Configure file wrong!Please check it."
                    exit()
    if len(_list) == 15:                                        #��ǰ��������Ŀ��
#         print _list
        return _list
    else:
        print "Configure file wrong!Please check it."
        exit()

#����xml�ļ�
def readXml(xmlFileUrl,elementName):
    elementData = []
    dom = xml.dom.minidom.parse(xmlFileUrl)  #��xml�ĵ�
    root = dom.documentElement   #��ȡ���нڵ����
    print root
    itemlist = root.getElementsByTagName(elementName)   #�ڼ����л�ȡ�ڵ�����ΪelementName�Ľڵ����
    for item in itemlist:
        un = item.firstChild.data
        elementData.append(un)    #��ȡ�Ա�ǩ֮�������
    return elementData

#��¼log�ļ�
def logWriter(pyfilename,message):
    LOG_FORMAT = "%(asctime)s " + str(pyfilename) + " %(message)s"         #����log�ļ����ݸ�ʽ���쳣������ʱ��/py�ļ�/��Ϣ��
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"                                      #�쳣����ʱ��ĸ�ʽ
    fileUrl = os.getcwd() + r'\report\test.log'                             
    if not os.path.exists(fileUrl):
        os.chdir('../')
        fileUrl=os.getcwd() + r'\report\test.log'
    logging.basicConfig(format = LOG_FORMAT,datefmt= DATE_FORMAT,filename=fileUrl,level = logging.DEBUG)  #ָ��Ҫ��¼��־�ļ�����־��ʽ�����ڸ�ʽ�����λ��
    logging.debug(message)
    logging.shutdown()             #�������Ϣ 
if __name__=='__main__':
#     pass
    app=pywin.Pywin()
    tl_dir = r'C:\QuiKLab3.0'
    tl_name = r'C:\QuiKLab3.0\MainApp.exe'  
#     confDataBase(tl_dir,tl_name,"���ݿ�")
    login(tl_dir,tl_name,'default','1')
# #     time.sleep(5)
#     window_name =u'QuiKLab'
#     time.sleep(1)
#     app.connect(window_name)
#     app.connect(window_name)
#     time.sleep(2)
#     creat_pro(window_name,'test_name120')
#     unload_pro(window_name)
#     load_pro(window_name, 'test_name120')
#     add_Bus(window_name)
#     add_dev(window_name)
#     add_tar(window_name,'192.168.1.103')
#     result=ckname.checkName('cl123')
#     print result
#     if result == 0:
#         print "ProName had exist������"
#         exit()
#     readIniConfig('QuikLab3.0')
#     logWriter()
#     logFile='2018_11_23.log'
#     isNotIn('ʧ��',logFile,'���Գɹ�')
#     run_case(window_name)
#     compareRes()
