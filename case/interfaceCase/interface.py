#! /usr/bin/env python
#coding=GB18030
import ctypes
import json
import logging
import os
import re
import sys
import time
import unittest

import data


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
os.chdir(r"D:\QuiKLab3.0")
lib = ctypes.cdll.LoadLibrary(r"D:\QuiKLab3.0\QuiKLabAPI.dll")
def judgeRes(input):
    assert input == 0
def checkPro():    
    print "获取当前平台的工程数量:\n",lib.getProjectCount()
    p_Num=lib.getProjectCount()
#SQL从数据库获取工程名列表_list 
    get_data=data.check()
    _list=get_data.getProName()
#比较接口获取工程数量同数据库工程数量
    if int(p_Num) == int(len(_list)):
        print('获取当前平台的总工程数量测试结果：Pass')
    else:
        print('获取当前平台的总工程数量测试结果：Fail')
        raise Exception,("Project num not match!")
    
    pN="s"*128
    p=[]
    flag=1
    for i in range(p_Num):      #查询所有工程名称
        lib.getProjectName(i,pN,len(pN))
        p.append(pN.split(a)[0])    #过去输出字符串中的a(空格)
        #将接口获取的工程名同数据库取出的工程列表_list进行匹配,flag=1为无匹配项
        for i in _list:
#             print i
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
        raise Exception,("Project not match!")
    time.sleep(5)

def runTestCase():
    print "加载工程:\n",lib.loadProject('uiTest')
    
    #测试用例
    print "获取当前工程的测试用例分类数量:\n",lib.getTestCaseClassCount()
     
    classN='s'*128
    lib.getTestCaseClassName(0, classN, len(classN))
    print "根据索引，获取分类下的测试用例类名称:\n",classN.strip(a)
     
    pn = "s"*128;
     
    cpn="s"*128
    lib.getCurrentProjectName(cpn,len(pn))
    print "当前工程的名称:\n",cpn.strip(a)
     
    print "获取测试用例集的测试用例数量:\n",lib.getTestCaseCount(classN)
     
    caseName='s'*128
    lib.getTestCaseName(classN,0,caseName,len(caseName))
    print "获取分类下的测试用例名称:\n",caseName.strip(a)
    # 
    lib.getInputSignalParamValue.restype=ctypes.c_float
    lib.getInputSignalParamValue("signal","P2")
    
    lib.getTargetCount()
    print"设置使用中的下位机IP:\n",lib.useTargetIp("192.168.1.212")
    print "设置使用中的测试用例:\n",lib.useTestCase(classN,caseName)
    
    time.sleep(1)
    print "为当前工程启动测试用(%s):\n"%caseName.split(a)[0],lib.startTestCase(caseName)
    
    time.sleep(5)
    print "下位机状态:",lib.getPlatformState()
#   

    print "获取测试用例运行时的参数数量:\n",lib.getTestCaseRuntimeParamCount()
    for i in range(10):
        lib.getInputSignalParamValue.restype=ctypes.c_float
        print("获取订阅的信号参数值:\n"),lib.getInputSignalParamValue("signal","P2")
        time.sleep(1)
    print "停止工程测试用例:\n",lib.stopTestCase()
    
def signalTest():
    print "加载工程:\n",judgeRes(lib.loadProject('1111111'))
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
#     print("获取订阅的信号参数值:\n"),lib.getInputSignalParamValue("signal","P3")
#     time.sleep(5)
#     print "停止工程测试用例:\n",lib.stopTestCase()
    print "下位机状态:",lib.getTargetState(0)
    
class Test(unittest.TestCase):


    @classmethod    
    def setUpClass(self):     
#         print "初始化QuiKLab平台类:\n",lib.initQuiKLabPlatform()
        while lib.initQuiKLabPlatform() != 0:
            pass
#         time.sleep(5)

    @classmethod
    def tearDownClass(self):
        print "释放平台类:\n" ,lib.releaseQuiKLabPlatform()


#     def test1(self):
#         checkPro()
    def test2(self):
        runTestCase()
#     def test3(self):
#         signalTest()
#         val=lib.loadProject('22222222222222222222')
#         print "加载工程:",val
if __name__ == "__main__":
    unittest.main()