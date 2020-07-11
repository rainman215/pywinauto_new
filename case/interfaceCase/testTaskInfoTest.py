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
        sqlTaskClass = sqlInfo.getTestTaskClassName(configList[4])    #从数据库获取测试任务类名称
        taskClassNum = lib.getTestTaskClassCount()                    #从接口获取测试任务类数量             
        caseBase.isNotEqual(len(sqlTaskClass), taskClassNum, '', '')
            
        if taskClassNum == len(sqlTaskClass):
            for i in range (0,taskClassNum):      
                lib.getTestTaskClassName(i,testTaskClassName,len(testTaskClassName))         #从接口获取测试任务类名称
#                 print sqlTaskClass[i].decode('utf-8').encode('GB18030'),testTaskClassName.strip('\x00')
                sqlTaskClassName = sqlTaskClass[i].decode('utf-8').encode('GB18030')
                print sqlTaskClassName,testTaskClassName.strip('\00')
                caseBase.isNotEqual(sqlTaskClassName, testTaskClassName.strip('\x00'), '', '')     #判断测试任务类名称是否相等
                if sqlTaskClassName != testTaskClassName.strip('\x00'):      
                    assert sqlTaskClassName == testTaskClassName.strip('\x00')                        
                    
                #如果测试任务类名称相等则判断任务类下的测试任务信息    
                else:
                    sqlTaskNameList = sqlInfo.getTestTaskName(configList[4],sqlTaskClassName)     #数据库获取测试任务类下的测试任务名称
                    taskNum = lib.getTestTaskCount(sqlTaskClassName)                #从接口获取测试任务数量
                    if len(sqlTaskNameList) != taskNum:                             #判断任务数量是否相等
                        assert len(sqlTaskNameList) == taskNum
                        
                    else:
                        for j in range(0,taskNum):
                            lib.getTestTaskName(sqlTaskClassName,j,testTask,len(testTask))    #从接口获取特定测试任务类名称下的测试任务名称
                            sqlTaskName = sqlTaskNameList[j].decode('utf-8').encode('GB18030')    #从数据库中获取特定测试任务类名称下的测试任务名称
                            print sqlTaskName
                            if sqlTaskName != testTask.strip('\x00'):     #判断测试任务名称是否相等
                                assert sqlTaskName == testTask.strip('\x00')
                                
                            #如果测试任务名称相同则判断任务下用例信息
                            else:
                                useTestTask = lib.useTestTask(sqlTaskClassName,sqlTaskName)     #设置使用中的测试任务
                                caseBase.isNotEqual(0, useTestTask, '', '')   #判断启用测试任务接口是否启用成功                      
                                testCaseNum = lib.getTestTaskTestCaseCount()      #从接口获取测试用例数量
                                sqlTestCaseInfo = sqlInfo.getTestTaskTestCaseInfo(configList[4],sqlTaskClassName,sqlTaskName)   #从数据库获取用例信息
                                dom = xmlManage.lxmlReaderModify(sqlTestCaseInfo)
                                sqlTestCaseList = dom.getTabNodeValue("//Item/@testCaseName")    #获取数据库中的testCaseName
                                if testCaseNum != len(sqlTestCaseList):
                                    assert testCaseNum == len(sqlTestCaseList)
                                else:
                                    for k in range(0,testCaseNum):
                                        lib.getTestTaskTestCaseName(k,testCase,len(testCase))        #从接口获取测试用例名称
                                        sqlTestCaseName = sqlTestCaseList[k].decode('utf-8').encode('GB18030')    #从数据库中获取测试用例名称 
                                        print sqlTestCaseName
                                        if sqlTestCaseName != testCase.strip('\x00'):
                                            assert sqlTestCaseName == testCase.strip('\x00')
                                            
                                        else:
                                            initValueNum = lib.getTestTaskTestCaseDoubleCount(k)     #从接口获取初始值数量
                                            sqlInitValues = dom.getTabNodeValue("//Item/@initialValues")[k]    #从数据库获取  initialValues属性的值
                                            sqlInitValueList = re.split('[=;]',sqlInitValues)      #从数据库中获取初始值的变量名和对应的值
                                            if initValueNum != len(sqlInitValueList)/2:              #判断初始值数量是否相等
                                                assert initValueNum == len(sqlInitValueList)/2
                                            else:
                                                for l in range(0,initValueNum):
                                                    initValue = c_double()
                                                    pstartValue = pointer(initValue)
                                                    lib.getTestTaskTestCaseDoubleNameValue(k,l,pstartDoubleName,len(pstartDoubleName),pstartValue)      #从接口获取初始值变量名和对应的值
                                                    sqlInitParam = sqlInitValueList[l*2].decode('utf-8').encode('GB18030')   #从数据库中获取初始值的变量名
                                                    sqlInitValue = sqlInitValueList[l*2 + 1].decode('utf-8').encode('GB18030')    #从数据库中获取初始值的变量名对应的值
                                                    print sqlInitParam,sqlInitValue
                                                    if sqlInitParam != pstartDoubleName.strip('\x00') or float(sqlInitValue) != initValue.value:          #判断从接口和数据库中获取的变量名和初始值是否相等
                                                        assert sqlInitParam == pstartDoubleName.strip('\x00') and float(sqlInitValue) == initValue.value                                                    

if __name__ == "__main__":
    unittest.main()