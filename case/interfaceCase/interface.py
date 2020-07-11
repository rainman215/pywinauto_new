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
a='\x00' #C�����еĿո�
os.chdir(r"D:\QuiKLab3.0")
lib = ctypes.cdll.LoadLibrary(r"D:\QuiKLab3.0\QuiKLabAPI.dll")
def judgeRes(input):
    assert input == 0
def checkPro():    
    print "��ȡ��ǰƽ̨�Ĺ�������:\n",lib.getProjectCount()
    p_Num=lib.getProjectCount()
#SQL�����ݿ��ȡ�������б�_list 
    get_data=data.check()
    _list=get_data.getProName()
#�ȽϽӿڻ�ȡ��������ͬ���ݿ⹤������
    if int(p_Num) == int(len(_list)):
        print('��ȡ��ǰƽ̨���ܹ����������Խ����Pass')
    else:
        print('��ȡ��ǰƽ̨���ܹ����������Խ����Fail')
        raise Exception,("Project num not match!")
    
    pN="s"*128
    p=[]
    flag=1
    for i in range(p_Num):      #��ѯ���й�������
        lib.getProjectName(i,pN,len(pN))
        p.append(pN.split(a)[0])    #��ȥ����ַ����е�a(�ո�)
        #���ӿڻ�ȡ�Ĺ�����ͬ���ݿ�ȡ���Ĺ����б�_list����ƥ��,flag=1Ϊ��ƥ����
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
        print('�������ƻ�ȡ���Խ��:Pass')
    else:
        print('�������ƻ�ȡ���Խ��:Fail')
        raise Exception,("Project not match!")
    time.sleep(5)

def runTestCase():
    print "���ع���:\n",lib.loadProject('uiTest')
    
    #��������
    print "��ȡ��ǰ���̵Ĳ���������������:\n",lib.getTestCaseClassCount()
     
    classN='s'*128
    lib.getTestCaseClassName(0, classN, len(classN))
    print "������������ȡ�����µĲ�������������:\n",classN.strip(a)
     
    pn = "s"*128;
     
    cpn="s"*128
    lib.getCurrentProjectName(cpn,len(pn))
    print "��ǰ���̵�����:\n",cpn.strip(a)
     
    print "��ȡ�����������Ĳ�����������:\n",lib.getTestCaseCount(classN)
     
    caseName='s'*128
    lib.getTestCaseName(classN,0,caseName,len(caseName))
    print "��ȡ�����µĲ�����������:\n",caseName.strip(a)
    # 
    lib.getInputSignalParamValue.restype=ctypes.c_float
    lib.getInputSignalParamValue("signal","P2")
    
    lib.getTargetCount()
    print"����ʹ���е���λ��IP:\n",lib.useTargetIp("192.168.1.212")
    print "����ʹ���еĲ�������:\n",lib.useTestCase(classN,caseName)
    
    time.sleep(1)
    print "Ϊ��ǰ��������������(%s):\n"%caseName.split(a)[0],lib.startTestCase(caseName)
    
    time.sleep(5)
    print "��λ��״̬:",lib.getPlatformState()
#   

    print "��ȡ������������ʱ�Ĳ�������:\n",lib.getTestCaseRuntimeParamCount()
    for i in range(10):
        lib.getInputSignalParamValue.restype=ctypes.c_float
        print("��ȡ���ĵ��źŲ���ֵ:\n"),lib.getInputSignalParamValue("signal","P2")
        time.sleep(1)
    print "ֹͣ���̲�������:\n",lib.stopTestCase()
    
def signalTest():
    print "���ع���:\n",judgeRes(lib.loadProject('1111111'))
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
#     print("��ȡ���ĵ��źŲ���ֵ:\n"),lib.getInputSignalParamValue("signal","P3")
#     time.sleep(5)
#     print "ֹͣ���̲�������:\n",lib.stopTestCase()
    print "��λ��״̬:",lib.getTargetState(0)
    
class Test(unittest.TestCase):


    @classmethod    
    def setUpClass(self):     
#         print "��ʼ��QuiKLabƽ̨��:\n",lib.initQuiKLabPlatform()
        while lib.initQuiKLabPlatform() != 0:
            pass
#         time.sleep(5)

    @classmethod
    def tearDownClass(self):
        print "�ͷ�ƽ̨��:\n" ,lib.releaseQuiKLabPlatform()


#     def test1(self):
#         checkPro()
    def test2(self):
        runTestCase()
#     def test3(self):
#         signalTest()
#         val=lib.loadProject('22222222222222222222')
#         print "���ع���:",val
if __name__ == "__main__":
    unittest.main()