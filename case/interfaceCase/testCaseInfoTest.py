#! /usr/bin/env python
#coding=GB18030
'''
Created on 2019��2��19��

@author: KLJS044
'''
import ctypes
import json
import os
import time
import unittest

import casebase.getReg as regInfo
import data
from case.interfaceCase import readConfig


a='\x00' #C�����еĿո�
configList = readConfig.readIniConfig('QuikLab3.0')
regInfo = regInfo.getRegVal('applicationPath')
# os.chdir(regInfo)
lib = ctypes.cdll.LoadLibrary(r"QuiKLabAPI.dll")

class Test(unittest.TestCase):

    @classmethod
    def setUp(self):
        lib.initQuiKLabPlatform()                 
        lib.loadProject(configList[4]) 

    @classmethod
    def tearDown(self):
        lib.releaseQuiKLabPlatform()
    @classmethod
    def testName_testCaseInfo(self):
        testCaseClassName  = testCaseName = classN = "t"*1024
        sqlInfo = data.check()
        testCaseClassName=sqlInfo.getTestCaseClassName(configList[4])       #�����ݿ��ȡ��������������
        classCount = lib.getTestCaseClassCount()                            #�ӽӿڻ�ȡ��������������

        
        for i in range(classCount):
            flag = 1
            lib.getTestCaseClassName(i, classN, len(classN))                #"������������ȡ�����µĲ�������������"
            for sqlCaseClassName in testCaseClassName:
                i = sqlCaseClassName
#                 print "class=",i                           
                if classN.strip(a) == i.decode('utf-8').encode('GB18030'):  #�����ݿ��õ��������б����unicodeת��str                       #�ӽӿڻ�ȡ�����������������ݿ��ڻ�õ��������������в���
                    flag = 0
                    sqlCaseName = sqlInfo.getTestCaseName(configList[4],i)  #�����ݿ��ȡ������������
#                     print sqlCaseName 
                    caseCount = lib.getTestCaseCount(i.decode('utf-8').encode('GB18030')) #��ȡ�������������²�����������
                    for c in range(caseCount):                              #���ýӿڱ���������������
                        caseFlag = 1
                        lib.getTestCaseName(i.decode('utf-8').encode('GB18030'),c,testCaseName,1024)  #��������c��ȡ������������
                        for n in sqlCaseName:
                            if testCaseName.strip(a)==n:                    #���ݿ��õ��������ƺͺ����ڻ�õ��������ƽ��бȽϣ��ҵ�ƥ����caseFlag=0
                                caseFlag=0
                        if caseFlag == 1:                                   #���ݿ�ͺ�����õ����ݲ�ƥ��ֱ���˳�����
                            break

            if flag == 1:
                break
        assert flag == 0,"��ȡ������������ʧ�ܣ�"
        print "��ȡ������������ɹ���" 
        assert caseFlag == 0,"��ȡ������������ʧ�ܣ�"
        print "��ȡ�����������Ƴɹ���"                                           #��ȡ����ʧ��ʱ���ж���                                              #��ȡ��������ʱ���ж���

if __name__ == "__main__":
    unittest.main()