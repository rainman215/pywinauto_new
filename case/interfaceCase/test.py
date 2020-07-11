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
a='\x00' #C语言中的空格
configList=readConfig.readIniConfig('QuikLab3.0')
dir=getReg.getRegVal('applicationPath')
os.chdir(dir)
lib = ctypes.cdll.LoadLibrary("QuiKLabAPI.dll")
val=lib.initQuiKLabPlatform()
if val==0:
    print "初始化QuiKLab平台类成功\n"    
time.sleep(5)
print("获取下位机数量:\n"),lib.getTargetCount()
print("根据索引获取下位机IP:")
IP="iP"*64
lib.getTargetIP(0,IP,len(IP))
print IP.strip(a)
    
print"根据索引获取下位机状态:\n",lib.getTargetState(0)
    
print"设置使用中的下位机IP:\n",lib.useTargetIp("192.168.1.5") 

def checkPro():    
    print "获取当前平台的工程数量:\n",lib.getProjectCount()
    p_Num=lib.getProjectCount()
    get_data=data.check()
    _list=get_data.getProName()
    print(_list)
    for i in _list:
        print i.encode('GB18030')

    if int(p_Num) == int(len(_list)):
        print('获取当前平台的总工程数量测试结果：Pass')
    else:
        print('获取当前平台的总工程数量测试结果：Fail')
    
    
    pN="s"*128
    p=[]
    flag=1
    for i in range(p_Num):      #查询所有工程名称
        lib.getProjectName(i,pN,len(pN))
        p.append(pN.split(a)[0])    #过去输出字符串中的a(空格)
        #将接口获取的工程名同数据库取出的工程列表_list进行匹配,flag=1为无匹配项
        for i in _list:
            if pN.strip(a)==i:
                flag=0
            else:
                pass
        if flag==1:
            print pN.strip(a)
            break
    if flag==0:
        print('工程名称获取测试结果:Pass')
    else:
        print('工程名称获取测试结果:Fail')
    time.sleep(5)
def runTestCase():
    print "加载工程:\n",lib.loadProject(configList[4])
    
    #测试用例
    print "获取当前工程的测试用例分类数量:\n",lib.getTestCaseClassCount()
     
    classN='s'*128
    lib.getTestCaseClassName(0, classN, len(classN))
    print "根据索引，获取分类下的测试用例类名称:\n",classN.strip(a)
     
    pn = "s"*128;
    # lib.getProjectName(1,pn,len(pn))
    # print "索引为'1'的工程名称:\n", pn.strip(a)
     
    cpn="s"*128
    lib.getCurrentProjectName(cpn,len(pn))
    print "当前工程的名称:\n",cpn.strip(a)
     
    print "获取测试用例集的测试用例数量:\n",lib.getTestCaseCount(classN)
     
    caseName='s'*128
    lib.getTestCaseName(classN,0,caseName,len(caseName))
    print "获取分类下的测试用例名称:\n",caseName.strip(a)
    # 
#     lib.getInputSignalParamValue.restype=ctypes.c_float
#     lib.getInputSignalParamValue("signal","P2")
    
    lib.getTargetCount()
    print"设置使用中的下位机IP:\n",lib.useTargetIp(configList[0])
    
    print "设置使用中的测试用例:\n",lib.useTestCase(configList[5],configList[6])
    print "为当前工程启动测试用例",lib.startTestCase(configList[7])
#     print "订阅输入信号的参数:\n",lib.regInputSignalParam("signal","P2")
    # print("设置发送信号的参数值:\n"),lib.setOutputSignalParamValue("signal","P3",55)
    # print("获取订阅的信号参数值:\n"),lib.getInputSignalParamValue("signal","P2") 
    time.sleep(5)
    print "下位机状态:",lib.getPlatformState()
    print "获取测试用例运行时的参数数量:\n",lib.getTestCaseRuntimeParamCount()
#     print("设置发送信号的参数值:\n"),lib.setOutputSignalParamValue("signal","P2",44)
#     print "获取参数值时自动订阅参数:\n",lib.setAutoRegWhenGetParamValue()
    for i in range(19):
        lib.getInputSignalParamValue.restype=ctypes.c_float
        print("获取订阅的信号参数值:\n"),lib.getInputSignalParamValue("signal","P1")
        time.sleep(1)
# print "获取测试用例运行时的参数数量:",lib.getTestCaseRuntimeParamCount()
    print "停止工程测试用例:\n",lib.stopTestCase()
# # 
def signalTest():
    print "加载工程:\n",lib.loadProject(configList[4])
    print("获取工程输入信号的数量:")
    num=lib.getInputSignalCount()
    print(num)
      
    print("获取输入信号的名称:")
    sN="insingnalName"
    print "*"*20
    for i in range(num):
        lib.getInputSignalName(i,sN,13)
        print sN
    print "*"*20
    print("获取工程输出信号的数量:")
    num=lib.getOutputSignalCount()
    print(num)
      
    print "*"*20
    for i in range(num):
        print "获取输出信号的名称:"
        sN="outsignalName"
        lib.getOutputSignalName(i,sN,13)
        print sN
        spNum=lib.getSignalParamCount(sN)
        print("获取信号的参数数量:"),spNum
        print("获取信号参数名称:")
        for i in range(spNum):
            spN="SignalParamName"
            lib.getSignalParamName(sN,i,spN,15)
            print spN
    #         time.sleep(1)
        print "*"*20
     
    # print(lib.setAutoWhenGetParamValue(true))
     
    # print("取消订阅:\n"),lib.unRegInputSignalParam("signal","P3")
     
    # print("设置发送信号的参数值:\n"),lib.setOutputSignalParamValue("signal","P3",55)
    print("获取订阅的信号参数值:\n"),lib.getInputSignalParamValue("signal","P3")
    time.sleep(5)
    print "停止工程测试用例:\n",lib.stopTestCase()
     
    print "下位机状态:",lib.getTargetState(0)

def testTask():
    print "加载工程:\n",lib.loadProject(configList[4])
    print "获取当前工程的测试任务分类数量:\n",lib.getTestTaskClassCount()
 
    testTaskClassName = "testTaskClassName"
    lib.getTestTaskClassName(1,testTaskClassName,17)
    print "根据索引，获取当前工程的测试任务分类名称:\n",testTaskClassName
    
    print "获取测试任务集的测试任务数量:\n",lib.getTestTaskCount(testTaskClassName)
     
    testTaskName = "testTaskName"
    lib.getTestTaskName(testTaskClassName,0,testTaskName,13)
    print "根据任务分类名和任务索引，获取测试任务名称:\n",testTaskName
     
    print "设置使用中的目标机IP",lib.useTargetIp(configList[0])
    print "设置使用中的测试任务:\n",lib.useTestTask(configList[8],configList[9])
    print "启动测试任务:\n",lib.startTestTask(configList[10])
    print "*"*20 
    time.sleep(10)
#     print "设置是否在获取参数值时自动订阅参数，默认为true即获取参数值时自动订阅参数:\n",lib.setAutoRegWhenGetParamValue(False)
#     print "订阅输入信号的参数:\n",lib.regInputSignalParam("signal","P2")
#     print "取消订阅:\n",lib.unRegInputSignalParam("signal","P2")
    testTaskTestCaseName = "TestTaskTestCaseName"
    lib.getTestTaskTestCaseName(0,testTaskTestCaseName,21)
    print "根据用例索引，获取任务下的测试用例名称:\n",testTaskTestCaseName
    for i in range(19):
        lib.getInputSignalParamValue.restype=ctypes.c_float
        print("获取订阅的信号参数值:\n"),lib.getInputSignalParamValue("signal","P1") 
        time.sleep(1)
    testTaskTestCaseName1 = "TestTaskTestCaseName"
    lib.getStatusTestCaseName('22',0,testTaskTestCaseName1,22)
    print "根据索引获取执行中的测试用例的名称:\n",testTaskTestCaseName1
     
    print "根据用例索引，获取初始值的数量:\n",lib.getTestTaskTestCaseDoubleCount(0)
    pstartDoubleName = "pDoubleName"
    # pstartValue = byref(c_double(1.0))
    value = c_double()
    pstartValue = pointer(value)
    lib.getTestTaskTestCaseDoubleNameValue(0,0,pstartDoubleName,11,pstartValue)
    print "根据用例索引和初始值索引，获取初始值的名和值:\n",pstartDoubleName,"\n",value
    print "根据用例索引和初始值索引，设置对应初始值的值:\n",lib.setTestTaskTestCaseDoubleValue(0,0,c_double(15))
     
    value = c_double()
    pstartValue = pointer(value)
    lib.getTestTaskTestCaseDoubleNameValue(0,0,pstartDoubleName,11,pstartValue)
    print "根据用例索引和初始值索引，获取初始值的名和值:\n",pstartDoubleName,"\n",value
    print "测试任务执行时获取平台运行状态:\n",lib.getPlatformState()
    print "测试任务执行时用例是否处于暂停状态:\n",lib.getStatusIsPause()
    print "测试任务执行时测试用例是否处于运行状态:\n",lib.getStatusForTestCaseRunning()
     
    print "获取执行中的测试用例个数:\n",lib.getStatusExcTestCaseCount(configList[9])
    print "获取测试用例运行时的参数数量",lib.getTestCaseRuntimeParamCount() 
    print "设置暂停状态",lib.setStatusIsPause(1)
    time.sleep(2)
    print "测试任务暂停时获取平台运行状态:\n",lib.getPlatformState()
    print "测试任务暂停时用例是否处于暂停状态:\n",lib.getStatusIsPause()
    print "测试任务暂停时测试用例是否处于运行状态:\n",lib.getStatusForTestCaseRunning()
     
    print "*"*20
    print "停止测试任务:\n",lib.stopTestTask()
    print "测试任务停止时获取平台运行状态:\n",lib.getPlatformState()
    time.sleep(5)
#     print "启动测试任务集:\n",lib.startTestTaskSet(configList[10])
    
    url = r"E:\testtaskset.xml"
#     print "设置测试任务集勾选状态表路径:\n",lib.updateTestTaskSetTablePath(url)
    time.sleep(5)
    print "停止测试任务集:\n",lib.stopTestTaskSet()
    
def fileTest():
    print "加载工程:\n",lib.loadProject('cl_test1')
    dir = "/"
    count=lib.getFileCount(dir)
    print "获取对应目录上的文件个数:\n",count
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
        print "根据目录与文件索引，返回文件名称:\n",fileName
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
    print "修改之前根据文件名，返回文件内容:\n",fileContent
    
    setFileContent = '''<?xml version="1.0"?>
<Layout>
    <Config mdiarea="0"/>
</Layout>'''
    print "根据文件名，设置文件内容",lib.setFileContent(fileName,setFileContent)
    
    fileContent = "fileContent"*300
    lib.getFileContent(fileName,fileContent,len(fileContent))
    print "修改之后根据文件名，返回文件内容:\n",fileContent
    
    
runTestCase()
# print "释放平台类:\n" ,lib.releaseQuiKLabPlatform()
# print testTask()
# fileTest()
# testTask()


