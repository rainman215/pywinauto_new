#! /usr/bin/env python
#coding=GB18030
import ctypes
import json
import os
import re
import sys
import time
import logging
import data
from _ctypes import byref, pointer
from ctypes import c_double
from casebase import getReg
import readConfig
# reload(sys)
# sys.setdefaultencoding('GB18030')

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(Levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='test.log',
                    filemode='w'
                    )
class Logger(object):
    def __init__(self,fileN='Default.log'):
        self.terminal=sys.stdout
        self.log=open(fileN,'w')
    def write(self,message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        pass
sys.stdout=Logger('1.txt')
a='\x00' #C�����еĿո�
configList=readConfig.readIniConfig('QuikLab3.0')
dir=getReg.getRegVal('applicationPath')
os.chdir(dir)
lib = ctypes.cdll.LoadLibrary("QuiKLabAPI.dll")
val=lib.initQuiKLabPlatform()
if val==0:
    print "��ʼ��QuiKLabƽ̨��ɹ�\n"    
time.sleep(5)
print("��ȡ��λ������:\n"),lib.getTargetCount()
print("����������ȡ��λ��IP:")
IP="iP"*64
lib.getTargetIP(0,IP,len(IP))
print IP.strip(a)
    
print"����������ȡ��λ��״̬:\n",lib.getTargetState(0)
    
print"����ʹ���е���λ��IP:\n",lib.useTargetIp("192.168.1.5") 

def checkPro():    
    print "��ȡ��ǰƽ̨�Ĺ�������:\n",lib.getProjectCount()
    p_Num=lib.getProjectCount()
    get_data=data.check()
    _list=get_data.getProName()
    print(_list)
    for i in _list:
        print i.encode('GB18030')

    if int(p_Num) == int(len(_list)):
        print('��ȡ��ǰƽ̨���ܹ����������Խ����Pass')
    else:
        print('��ȡ��ǰƽ̨���ܹ����������Խ����Fail')
    
    
    pN="s"*128
    p=[]
    flag=1
    for i in range(p_Num):      #��ѯ���й�������
        lib.getProjectName(i,pN,len(pN))
        p.append(pN.split(a)[0])    #��ȥ����ַ����е�a(�ո�)
        #���ӿڻ�ȡ�Ĺ�����ͬ���ݿ�ȡ���Ĺ����б�_list����ƥ��,flag=1Ϊ��ƥ����
        for i in _list:
            if pN.strip(a)==i:
                flag=0
            else:
                pass
        if flag==1:
            print pN.strip(a)
            break
    if flag==0:
        print('�������ƻ�ȡ���Խ��:Pass')
    else:
        print('�������ƻ�ȡ���Խ��:Fail')
    time.sleep(5)
def runTestCase():
    print "���ع���:\n",lib.loadProject(configList[4])
    
    #��������
    print "��ȡ��ǰ���̵Ĳ���������������:\n",lib.getTestCaseClassCount()
     
    classN='s'*128
    lib.getTestCaseClassName(0, classN, len(classN))
    print "������������ȡ�����µĲ�������������:\n",classN.strip(a)
     
    pn = "s"*128;
    # lib.getProjectName(1,pn,len(pn))
    # print "����Ϊ'1'�Ĺ�������:\n", pn.strip(a)
     
    cpn="s"*128
    lib.getCurrentProjectName(cpn,len(pn))
    print "��ǰ���̵�����:\n",cpn.strip(a)
     
    print "��ȡ�����������Ĳ�����������:\n",lib.getTestCaseCount(classN)
     
    caseName='s'*128
    lib.getTestCaseName(classN,0,caseName,len(caseName))
    print "��ȡ�����µĲ�����������:\n",caseName.strip(a)
    # 
#     lib.getInputSignalParamValue.restype=ctypes.c_float
#     lib.getInputSignalParamValue("signal","P2")
    
    lib.getTargetCount()
    print"����ʹ���е���λ��IP:\n",lib.useTargetIp(configList[0])
    
    print "����ʹ���еĲ�������:\n",lib.useTestCase(configList[5],configList[6])
    print "Ϊ��ǰ����������������",lib.startTestCase(configList[7])
#     print "���������źŵĲ���:\n",lib.regInputSignalParam("signal","P2")
    # print("���÷����źŵĲ���ֵ:\n"),lib.setOutputSignalParamValue("signal","P3",55)
    # print("��ȡ���ĵ��źŲ���ֵ:\n"),lib.getInputSignalParamValue("signal","P2") 
    time.sleep(5)
    print "��λ��״̬:",lib.getPlatformState()
    print "��ȡ������������ʱ�Ĳ�������:\n",lib.getTestCaseRuntimeParamCount()
#     print("���÷����źŵĲ���ֵ:\n"),lib.setOutputSignalParamValue("signal","P2",44)
#     print "��ȡ����ֵʱ�Զ����Ĳ���:\n",lib.setAutoRegWhenGetParamValue()
    for i in range(19):
        lib.getInputSignalParamValue.restype=ctypes.c_float
        print("��ȡ���ĵ��źŲ���ֵ:\n"),lib.getInputSignalParamValue("signal","P1")
        time.sleep(1)
# print "��ȡ������������ʱ�Ĳ�������:",lib.getTestCaseRuntimeParamCount()
    print "ֹͣ���̲�������:\n",lib.stopTestCase()
# # 
def signalTest():
    print "���ع���:\n",lib.loadProject(configList[4])
    print("��ȡ���������źŵ�����:")
    num=lib.getInputSignalCount()
    print(num)
      
    print("��ȡ�����źŵ�����:")
    sN="insingnalName"
    print "*"*20
    for i in range(num):
        lib.getInputSignalName(i,sN,13)
        print sN
    print "*"*20
    print("��ȡ��������źŵ�����:")
    num=lib.getOutputSignalCount()
    print(num)
      
    print "*"*20
    for i in range(num):
        print "��ȡ����źŵ�����:"
        sN="outsignalName"
        lib.getOutputSignalName(i,sN,13)
        print sN
        spNum=lib.getSignalParamCount(sN)
        print("��ȡ�źŵĲ�������:"),spNum
        print("��ȡ�źŲ�������:")
        for i in range(spNum):
            spN="SignalParamName"
            lib.getSignalParamName(sN,i,spN,15)
            print spN
    #         time.sleep(1)
        print "*"*20
     
    # print(lib.setAutoWhenGetParamValue(true))
     
    # print("ȡ������:\n"),lib.unRegInputSignalParam("signal","P3")
     
    # print("���÷����źŵĲ���ֵ:\n"),lib.setOutputSignalParamValue("signal","P3",55)
    print("��ȡ���ĵ��źŲ���ֵ:\n"),lib.getInputSignalParamValue("signal","P3")
    time.sleep(5)
    print "ֹͣ���̲�������:\n",lib.stopTestCase()
     
    print "��λ��״̬:",lib.getTargetState(0)

def testTask():
    print "���ع���:\n",lib.loadProject(configList[4])
    print "��ȡ��ǰ���̵Ĳ��������������:\n",lib.getTestTaskClassCount()
 
    testTaskClassName = "testTaskClassName"
    lib.getTestTaskClassName(1,testTaskClassName,17)
    print "������������ȡ��ǰ���̵Ĳ��������������:\n",testTaskClassName
    
    print "��ȡ�������񼯵Ĳ�����������:\n",lib.getTestTaskCount(testTaskClassName)
     
    testTaskName = "testTaskName"
    lib.getTestTaskName(testTaskClassName,0,testTaskName,13)
    print "���������������������������ȡ������������:\n",testTaskName
     
    print "����ʹ���е�Ŀ���IP",lib.useTargetIp(configList[0])
    print "����ʹ���еĲ�������:\n",lib.useTestTask(configList[8],configList[9])
    print "������������:\n",lib.startTestTask(configList[10])
    print "*"*20 
    time.sleep(10)
#     print "�����Ƿ��ڻ�ȡ����ֵʱ�Զ����Ĳ�����Ĭ��Ϊtrue����ȡ����ֵʱ�Զ����Ĳ���:\n",lib.setAutoRegWhenGetParamValue(False)
#     print "���������źŵĲ���:\n",lib.regInputSignalParam("signal","P2")
#     print "ȡ������:\n",lib.unRegInputSignalParam("signal","P2")
    testTaskTestCaseName = "TestTaskTestCaseName"
    lib.getTestTaskTestCaseName(0,testTaskTestCaseName,21)
    print "����������������ȡ�����µĲ�����������:\n",testTaskTestCaseName
    for i in range(19):
        lib.getInputSignalParamValue.restype=ctypes.c_float
        print("��ȡ���ĵ��źŲ���ֵ:\n"),lib.getInputSignalParamValue("signal","P1") 
        time.sleep(1)
    testTaskTestCaseName1 = "TestTaskTestCaseName"
    lib.getStatusTestCaseName('22',0,testTaskTestCaseName1,22)
    print "����������ȡִ���еĲ�������������:\n",testTaskTestCaseName1
     
    print "����������������ȡ��ʼֵ������:\n",lib.getTestTaskTestCaseDoubleCount(0)
    pstartDoubleName = "pDoubleName"
    # pstartValue = byref(c_double(1.0))
    value = c_double()
    pstartValue = pointer(value)
    lib.getTestTaskTestCaseDoubleNameValue(0,0,pstartDoubleName,11,pstartValue)
    print "�������������ͳ�ʼֵ��������ȡ��ʼֵ������ֵ:\n",pstartDoubleName,"\n",value
    print "�������������ͳ�ʼֵ���������ö�Ӧ��ʼֵ��ֵ:\n",lib.setTestTaskTestCaseDoubleValue(0,0,c_double(15))
     
    value = c_double()
    pstartValue = pointer(value)
    lib.getTestTaskTestCaseDoubleNameValue(0,0,pstartDoubleName,11,pstartValue)
    print "�������������ͳ�ʼֵ��������ȡ��ʼֵ������ֵ:\n",pstartDoubleName,"\n",value
    print "��������ִ��ʱ��ȡƽ̨����״̬:\n",lib.getPlatformState()
    print "��������ִ��ʱ�����Ƿ�����ͣ״̬:\n",lib.getStatusIsPause()
    print "��������ִ��ʱ���������Ƿ�������״̬:\n",lib.getStatusForTestCaseRunning()
     
    print "��ȡִ���еĲ�����������:\n",lib.getStatusExcTestCaseCount(configList[9])
    print "��ȡ������������ʱ�Ĳ�������",lib.getTestCaseRuntimeParamCount() 
    print "������ͣ״̬",lib.setStatusIsPause(1)
    time.sleep(2)
    print "����������ͣʱ��ȡƽ̨����״̬:\n",lib.getPlatformState()
    print "����������ͣʱ�����Ƿ�����ͣ״̬:\n",lib.getStatusIsPause()
    print "����������ͣʱ���������Ƿ�������״̬:\n",lib.getStatusForTestCaseRunning()
     
    print "*"*20
    print "ֹͣ��������:\n",lib.stopTestTask()
    print "��������ֹͣʱ��ȡƽ̨����״̬:\n",lib.getPlatformState()
    time.sleep(5)
#     print "������������:\n",lib.startTestTaskSet(configList[10])
    
    url = r"E:\testtaskset.xml"
#     print "���ò������񼯹�ѡ״̬��·��:\n",lib.updateTestTaskSetTablePath(url)
    time.sleep(5)
    print "ֹͣ��������:\n",lib.stopTestTaskSet()
    
def fileTest():
    print "���ع���:\n",lib.loadProject('cl_test1')
    dir = "/"
    count=lib.getFileCount(dir)
    print "��ȡ��ӦĿ¼�ϵ��ļ�����:\n",count
    get_data=data.check()
    SqlList=get_data.getFileResources('cl_test1')
    if count == len(SqlList):
        pass
    else:
        print "Wrong"
        exit()
    fileName = "fileName"*12
    flag=1
    for i in range(count):
        lib.getFileName(dir,i,fileName,len(fileName))
        print "����Ŀ¼���ļ������������ļ�����:\n",fileName
        for c in SqlList:
            if fileName.strip(a).strip('/') == c:
                flag=0
            else:
                pass
        if flag==1:
            print fileName+"**********"
            break
    time.sleep(5)
    fileContent = "fileContent"*300
    print lib.getFileContent(fileName,fileContent,len(fileContent))
    print "�޸�֮ǰ�����ļ����������ļ�����:\n",fileContent
    
    setFileContent = '''<?xml version="1.0"?>
<Layout>
    <Config mdiarea="0"/>
</Layout>'''
    print "�����ļ����������ļ�����",lib.setFileContent(fileName,setFileContent)
    
    fileContent = "fileContent"*300
    lib.getFileContent(fileName,fileContent,len(fileContent))
    print "�޸�֮������ļ����������ļ�����:\n",fileContent
    
    
runTestCase()
# print "�ͷ�ƽ̨��:\n" ,lib.releaseQuiKLabPlatform()
# print testTask()
# fileTest()
# testTask()


