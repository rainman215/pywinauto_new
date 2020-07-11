#! /usr/bin/env python
#coding=GB18030
'''
Created on 2019��3��4��

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


a='\x00' #C�����еĿո�
configList = readConfig.readIniConfig('QuikLab3.0')
regInfo = regInfo.getRegVal('applicationPath')
# os.chdir(regInfo)
lib = ctypes.cdll.LoadLibrary(r"QuiKLabAPI.dll")


class Test(unittest.TestCase):
    def setUp(self):
        assert lib.initQuiKLabPlatform() == 0,'��ʼ��ʧ��!\n'                 
        time.sleep(5)
        lib.loadProject(configList[4])


    def tearDown(self):
        assert lib.releaseQuiKLabPlatform() == 0,'�����ͷ�ʧ�ܣ�\n'


    def testName_runTestCase(self):
        proName = caseParaName = 't'*1024
        assert lib.useTargetIp(configList[0]) == 0,"����ʹ���е���λ��IPʧ�ܣ�\n"
        print "������λ��IP:%s\n"%configList[0]
        assert lib.getPlatformState() == 0,'ƽ̨״̬����ȷ��\n'
        print "ƽ̨״̬:����\n"
        assert lib.getTargetState(configList[0]) == 0,'��λ��״̬����ȷ��\n'
        print "��λ��״̬:����\n"
        
        assert lib.getStatusIsPause() == 0,'����״̬����\n'
        print '����������ͣ״̬\n'
        assert lib.getStatusForTestCaseRunning() == 0,'��������״̬����\n'
        print '��������������״̬��\n'
#��ʼִ�в�������        
        exTestClass = configList[5]
        exTestCase = configList[6]
        assert lib.useTestCase(exTestClass,exTestCase) == 0,'ѡ�в�������ʧ�ܣ�\n'
        print "����ʹ���еĲ�������:�ɹ�\n"
        time.sleep(1)
        print "Ϊ��ǰ��������������(%s):\n"%exTestCase,lib.startTestCase(exTestCase)      
        time.sleep(5)
        lib.getCurrentProjectName(proName,1024)
        assert lib.setAutoRegWhenGetParamValue() == 0,'��ȡ����ֵʱ�Զ����Ĳ���ʧ�ܣ�\n'
        print '��ȡ����ֵʱ�Զ����Ĳ����Զ����ĳɹ�\n'
        assert lib.regInputSignalParam('signal','P2') == 0,'���������źŵĲ���ʧ�ܣ�\n'
        print "���������źŵĲ���:�ɹ�\n"
        assert lib.unRegInputSignalParam('signal','P2') == 0,'ȡ������ʧ�ܣ�\n'
        print 'ȡ������:�ɹ�\n'
        assert proName.strip(a) == 'uiTest',"��ȡ��ǰ����������\n"
        print '��ȡ������:',proName.strip(a)
        assert lib.getPlatformState() == 1,'ƽ̨״̬����ȷ��\n'
        print "ƽ̨״̬:��æ\n"
        assert lib.getTargetState(configList[0]),'��λ��״̬����ȷ��\n'
        print "��λ��״̬:��æ\n"
#         print '����״̬',lib.getStatusIsPause()
        print lib.setStatusIsPause(1)
#         statusComp=compareVal.compare(lib.getStatusIsPause(),0,1)
#         statusComp.eq('������ͣʧ��')
        count = 0
        while lib.getStatusIsPause() == 0:
            count += 1
            time.sleep(1)
            if count > 10:
                assert lib.getStatusIsPause() == 1,'������ͣʧ�ܣ�\n'
        print '����������ͣ״̬��\n'
        print lib.setStatusIsPause(0)
        count = 0
        while lib.getStatusIsPause() == 1:          #��ѯ�����Ƿ�����ͣ״̬��������ѯ10�Σ�ÿ��1���ѯһ��
            count += 1
            time.sleep(1)
            if count > 10:
                assert lib.getStatusIsPause() == 0,'����ִ��ʧ�ܣ�\n'
        print '�������ڷ���ͣ״̬��\n'
        
        assert lib.getStatusForTestCaseRunning() == 1,'��������״��ȡ̬����\n'
        print '������������״̬��\n'
        
        lib.getInputSignalParamValue.restype=ctypes.c_float
        for i in range(5):                  #��ѯsignal.P2ֵ����ѯ5�Σ�ÿ��1s��ѯһ��
            print lib.getInputSignalParamValue("signal","P2")
            time.sleep(1)
        assert lib.resetInputSignal('signal') == 0,'���������źŲ���ֵʧ��\n'
        assert lib.getInputSignalParamValue("signal","P2") == 0.0,'�����ź�ֵʧ�ܣ�\n'
        print '���������ź�ֵ���ɹ�\n'

        time.sleep(2)
        print lib.getInputSignalParamValue("signal","P1")
        print lib.getTestCaseRuntimeParamCount()
        lib.getTestCaseRuntimeParamValue.restype=ctypes.c_float
        for i in range(lib.getTestCaseRuntimeParamCount()):                 #�������л�õĲ�����
            lib.getTestCaseRuntimeParamName(i,caseParaName,1024)            #������������б������Ĳ�����
            print "������",caseParaName.strip(a)                               #ɾ���ӿڻ�õĶ���ո�
            print caseParaName.strip(a)+':',lib.getTestCaseRuntimeParamValue(caseParaName)
        assert lib.stopTestCase() == 0,'ֹͣ��������ʧ��\n'
        print "ֹͣ���̲�������:�ɹ�\n"
        assert lib.getPlatformState() == 0,'ƽ̨״̬����ȷ\n'
        print "ƽ̨״̬:����\n"
        time.sleep(5)
        assert lib.getTargetState(configList[0]) == 0,'��λ��״̬����ȷ\n'
        print "��λ��״̬:����\n"
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()