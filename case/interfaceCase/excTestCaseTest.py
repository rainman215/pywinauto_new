#! /usr/bin/env python
#coding=GB18030
'''
Created on 2019年3月4日

@author: KLJS044
'''
import ctypes
import json
import os
import time
import unittest
# import compareVal
import casebase.getReg as regInfo
import data
import readConfig


a='\x00' #C语言中的空格
configList = readConfig.readIniConfig('QuikLab3.0')
regInfo = regInfo.getRegVal('applicationPath')
# os.chdir(regInfo)
lib = ctypes.cdll.LoadLibrary(r"QuiKLabAPI.dll")


class Test(unittest.TestCase):
    def setUp(self):
        assert lib.initQuiKLabPlatform() == 0,'初始化失败!\n'                 
        time.sleep(5)
        lib.loadProject(configList[4])


    def tearDown(self):
        assert lib.releaseQuiKLabPlatform() == 0,'工程释放失败！\n'


    def testName_runTestCase(self):
        proName = caseParaName = 't'*1024
        assert lib.useTargetIp(configList[0]) == 0,"设置使用中的下位机IP失败！\n"
        print "设置下位机IP:%s\n"%configList[0]
        assert lib.getPlatformState() == 0,'平台状态不正确！\n'
        print "平台状态:空闲\n"
        assert lib.getTargetState(configList[0]) == 0,'下位机状态不正确！\n'
        print "下位机状态:空闲\n"
        
        assert lib.getStatusIsPause() == 0,'用例状态错误！\n'
        print '用例处于暂停状态\n'
        assert lib.getStatusForTestCaseRunning() == 0,'用例运行状态错误！\n'
        print '用例不处于运行状态！\n'
#开始执行测试用例        
        exTestClass = configList[5]
        exTestCase = configList[6]
        assert lib.useTestCase(exTestClass,exTestCase) == 0,'选中测试用例失败！\n'
        print "设置使用中的测试用例:成功\n"
        time.sleep(1)
        print "为当前工程启动测试用(%s):\n"%exTestCase,lib.startTestCase(exTestCase)      
        time.sleep(5)
        lib.getCurrentProjectName(proName,1024)
        assert lib.setAutoRegWhenGetParamValue() == 0,'获取参数值时自动订阅参数失败！\n'
        print '获取参数值时自动订阅参数自动订阅成功\n'
        assert lib.regInputSignalParam('signal','P2') == 0,'订阅输入信号的参数失败！\n'
        print "订阅输入信号的参数:成功\n"
        assert lib.unRegInputSignalParam('signal','P2') == 0,'取消订阅失败！\n'
        print '取消订阅:成功\n'
        assert proName.strip(a) == 'uiTest',"获取当前工程名错误！\n"
        print '获取工程名:',proName.strip(a)
        assert lib.getPlatformState() == 1,'平台状态不正确！\n'
        print "平台状态:繁忙\n"
        assert lib.getTargetState(configList[0]),'下位机状态不正确！\n'
        print "下位机状态:繁忙\n"
#         print '用例状态',lib.getStatusIsPause()
        print lib.setStatusIsPause(1)
#         statusComp=compareVal.compare(lib.getStatusIsPause(),0,1)
#         statusComp.eq('用例暂停失败')
        count = 0
        while lib.getStatusIsPause() == 0:
            count += 1
            time.sleep(1)
            if count > 10:
                assert lib.getStatusIsPause() == 1,'用例暂停失败！\n'
        print '用例处于暂停状态！\n'
        print lib.setStatusIsPause(0)
        count = 0
        while lib.getStatusIsPause() == 1:          #查询用例是否处于暂停状态，连续查询10次，每隔1秒查询一次
            count += 1
            time.sleep(1)
            if count > 10:
                assert lib.getStatusIsPause() == 0,'用例执行失败！\n'
        print '用例处于非暂停状态！\n'
        
        assert lib.getStatusForTestCaseRunning() == 1,'用例运行状获取态错误！\n'
        print '用例处于运行状态！\n'
        
        lib.getInputSignalParamValue.restype=ctypes.c_float
        for i in range(5):                  #查询signal.P2值，查询5次，每隔1s查询一次
            print lib.getInputSignalParamValue("signal","P2")
            time.sleep(1)
        assert lib.resetInputSignal('signal') == 0,'重置输入信号参数值失败\n'
        assert lib.getInputSignalParamValue("signal","P2") == 0.0,'重置信号值失败！\n'
        print '重置输入信号值：成功\n'

        time.sleep(2)
        print lib.getInputSignalParamValue("signal","P1")
        print lib.getTestCaseRuntimeParamCount()
        lib.getTestCaseRuntimeParamValue.restype=ctypes.c_float
        for i in range(lib.getTestCaseRuntimeParamCount()):                 #遍历所有获得的参数数
            lib.getTestCaseRuntimeParamName(i,caseParaName,1024)            #按索引获得所有遍历到的参数名
            print "参数名",caseParaName.strip(a)                               #删除接口获得的多余空格
            print caseParaName.strip(a)+':',lib.getTestCaseRuntimeParamValue(caseParaName)
        assert lib.stopTestCase() == 0,'停止测试用例失败\n'
        print "停止工程测试用例:成功\n"
        assert lib.getPlatformState() == 0,'平台状态不正确\n'
        print "平台状态:空闲\n"
        time.sleep(5)
        assert lib.getTargetState(configList[0]) == 0,'下位机状态不正确\n'
        print "下位机状态:空闲\n"
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()