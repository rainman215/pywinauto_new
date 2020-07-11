#! /usr/bin/env python
#coding=GB18030
'''
@author: KLJS276
'''
from _ctypes import pointer
from ctypes import c_double
import ctypes
import os
import re
import unittest

import casebase.getReg as regInfo
import casebase.lxmlReaderModify as xmlManage
import casebase.case_wrapper as caseBase
import data
import readConfig


configList = readConfig.readIniConfig('QuikLab3.0')
regInfo = regInfo.getRegVal('applicationPath')
# os.chdir(regInfo)
lib = ctypes.cdll.LoadLibrary(r"QuiKLabAPI.dll")


class Test(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        lib.initQuiKLabPlatform()                 
        lib.loadProject(configList[4])            


    @classmethod
    def tearDownClass(self):
        lib.releaseQuiKLabPlatform()        

    @classmethod
    def testName_testTaskInfo(self):
        testTaskClassName = testTask = testCase = pstartDoubleName = "t"*1024
        sqlInfo = data.check()
        sqlTaskClass = sqlInfo.getTestTaskClassName(configList[4])    #�����ݿ��ȡ��������������
        taskClassNum = lib.getTestTaskClassCount()                    #�ӽӿڻ�ȡ��������������             
        caseBase.isNotEqual(len(sqlTaskClass), taskClassNum, '', '')
            
        if taskClassNum == len(sqlTaskClass):
            for i in range (0,taskClassNum):      
                lib.getTestTaskClassName(i,testTaskClassName,len(testTaskClassName))         #�ӽӿڻ�ȡ��������������
#                 print sqlTaskClass[i].decode('utf-8').encode('GB18030'),testTaskClassName.strip('\x00')
                sqlTaskClassName = sqlTaskClass[i].decode('utf-8').encode('GB18030')
                print sqlTaskClassName,testTaskClassName.strip('\00')
                caseBase.isNotEqual(sqlTaskClassName, testTaskClassName.strip('\x00'), '', '')     #�жϲ��������������Ƿ����
                if sqlTaskClassName != testTaskClassName.strip('\x00'):      
                    assert sqlTaskClassName == testTaskClassName.strip('\x00')                        
                    
                #�����������������������ж��������µĲ���������Ϣ    
                else:
                    sqlTaskNameList = sqlInfo.getTestTaskName(configList[4],sqlTaskClassName)     #���ݿ��ȡ�����������µĲ�����������
                    taskNum = lib.getTestTaskCount(sqlTaskClassName)                #�ӽӿڻ�ȡ������������
                    if len(sqlTaskNameList) != taskNum:                             #�ж����������Ƿ����
                        assert len(sqlTaskNameList) == taskNum
                        
                    else:
                        for j in range(0,taskNum):
                            lib.getTestTaskName(sqlTaskClassName,j,testTask,len(testTask))    #�ӽӿڻ�ȡ�ض����������������µĲ�����������
                            sqlTaskName = sqlTaskNameList[j].decode('utf-8').encode('GB18030')    #�����ݿ��л�ȡ�ض����������������µĲ�����������
                            print sqlTaskName
                            if sqlTaskName != testTask.strip('\x00'):     #�жϲ������������Ƿ����
                                assert sqlTaskName == testTask.strip('\x00')
                                
                            #�����������������ͬ���ж�������������Ϣ
                            else:
                                useTestTask = lib.useTestTask(sqlTaskClassName,sqlTaskName)     #����ʹ���еĲ�������
                                caseBase.isNotEqual(0, useTestTask, '', '')   #�ж����ò�������ӿ��Ƿ����óɹ�                      
                                testCaseNum = lib.getTestTaskTestCaseCount()      #�ӽӿڻ�ȡ������������
                                sqlTestCaseInfo = sqlInfo.getTestTaskTestCaseInfo(configList[4],sqlTaskClassName,sqlTaskName)   #�����ݿ��ȡ������Ϣ
                                dom = xmlManage.lxmlReaderModify(sqlTestCaseInfo)
                                sqlTestCaseList = dom.getTabNodeValue("//Item/@testCaseName")    #��ȡ���ݿ��е�testCaseName
                                if testCaseNum != len(sqlTestCaseList):
                                    assert testCaseNum == len(sqlTestCaseList)
                                else:
                                    for k in range(0,testCaseNum):
                                        lib.getTestTaskTestCaseName(k,testCase,len(testCase))        #�ӽӿڻ�ȡ������������
                                        sqlTestCaseName = sqlTestCaseList[k].decode('utf-8').encode('GB18030')    #�����ݿ��л�ȡ������������ 
                                        print sqlTestCaseName
                                        if sqlTestCaseName != testCase.strip('\x00'):
                                            assert sqlTestCaseName == testCase.strip('\x00')
                                            
                                        else:
                                            initValueNum = lib.getTestTaskTestCaseDoubleCount(k)     #�ӽӿڻ�ȡ��ʼֵ����
                                            sqlInitValues = dom.getTabNodeValue("//Item/@initialValues")[k]    #�����ݿ��ȡ  initialValues���Ե�ֵ
                                            sqlInitValueList = re.split('[=;]',sqlInitValues)      #�����ݿ��л�ȡ��ʼֵ�ı������Ͷ�Ӧ��ֵ
                                            if initValueNum != len(sqlInitValueList)/2:              #�жϳ�ʼֵ�����Ƿ����
                                                assert initValueNum == len(sqlInitValueList)/2
                                            else:
                                                for l in range(0,initValueNum):
                                                    initValue = c_double()
                                                    pstartValue = pointer(initValue)
                                                    lib.getTestTaskTestCaseDoubleNameValue(k,l,pstartDoubleName,len(pstartDoubleName),pstartValue)      #�ӽӿڻ�ȡ��ʼֵ�������Ͷ�Ӧ��ֵ
                                                    sqlInitParam = sqlInitValueList[l*2].decode('utf-8').encode('GB18030')   #�����ݿ��л�ȡ��ʼֵ�ı�����
                                                    sqlInitValue = sqlInitValueList[l*2 + 1].decode('utf-8').encode('GB18030')    #�����ݿ��л�ȡ��ʼֵ�ı�������Ӧ��ֵ
                                                    print sqlInitParam,sqlInitValue
                                                    if sqlInitParam != pstartDoubleName.strip('\x00') or float(sqlInitValue) != initValue.value:          #�жϴӽӿں����ݿ��л�ȡ�ı������ͳ�ʼֵ�Ƿ����
                                                        assert sqlInitParam == pstartDoubleName.strip('\x00') and float(sqlInitValue) == initValue.value                                                    

if __name__ == "__main__":
    unittest.main()