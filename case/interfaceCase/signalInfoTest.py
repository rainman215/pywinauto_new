#! /usr/bin/env python
#coding=GB18030

'''

@author: KLJS276
'''
import ctypes
import os
import unittest
import readConfig
import casebase.lxmlReaderModify as xmlManage
import casebase.getReg as regInfo
import data
import casebase.case_wrapper as case1


configList = readConfig.readIniConfig('QuikLab3.0')
regInfo = regInfo.getRegVal('applicationPath')
# os.chdir(regInfo)
lib = ctypes.cdll.LoadLibrary(r"QuiKLabAPI.dll")


class TestSignalInfo(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        lib.initQuiKLabPlatform()          #��ʼ��QuiKLabƽ̨       
        lib.loadProject(configList[4])            #���ع���
        
        
    @classmethod
    def tearDownClass(self):
        lib.releaseQuiKLabPlatform()         #�ͷ�QuiKLabƽ̨


    def test1InputSignalInfo(self):
        exceptInputSignal = []
        sqlInfo = data.check()
        signalInfo = sqlInfo.getSignalInfo(configList[4])         #�����ݿ��л�ȡ�ź���Ϣ
        dom = xmlManage.lxmlReaderModify(signalInfo)
        signalName = dom.getTabNodeValue("//Routing/@name")    #��ȡ���ݿ��е�SignalName
        for signal in signalName: 
            recvFlag = dom.getTabNodeValue("//Routing[@name='%s']/@recvFlag"%signal)
            sendFlag = dom.getTabNodeValue("//Routing[@name='%s']/@sendFlag"%signal)
            if len(recvFlag[0]) != 0:                        #���recvFlag��Ϊ����Ϊ�����ź�
                exceptInputSignal.append(signal)
        exceptInputSignalNum = len(exceptInputSignal)         #�����ݿ�õ��������źŵ�����       
        acutalInputSignalNum = lib.getInputSignalCount()      #�ӽӿڻ�ȡ�ź�����
        case1.isNotEqual(exceptInputSignalNum,acutalInputSignalNum,'','')
            
        if exceptInputSignalNum == acutalInputSignalNum:
            for i in range (acutalInputSignalNum):
                inputSignalName = "getInputSignalName"
                lib.getInputSignalName(i,inputSignalName,len(inputSignalName))   #ʵ�ʵ������ź�����
                acutalInputSignalName = inputSignalName.strip('\x00')
                for j in range (exceptInputSignalNum):
                    print "acutalInputSignalName",acutalInputSignalName
                    if acutalInputSignalName == exceptInputSignal[j]:
                        print "exceptInputSignal",exceptInputSignal[j]
                        packId = dom.getTabNodeValue("//Routing[@name='%s']/@packID"%exceptInputSignal[j])    #���ź���Ϣ�и����ź����ƻ�ȡ��PackID
                        exceptParamName = dom.getTabNodeValue("//Struct[@ID='%s']/Param/@name"%packId[0])           #��Struct��Ϣ�и���ID��Ϣ��ȡ����������
                        exceptParamNameNum = len(exceptParamName)      #���ݿ��д洢���źŵĲ�������
                        actualParamNameNum = lib.getSignalParamCount(acutalInputSignalName)   #�ӿڻ�ȡ���źŵĲ�������
                        case1.isNotEqual(exceptParamNameNum,actualParamNameNum,'','')   #�ж��źŵĲ��������Ƿ����
                        if  exceptParamNameNum == actualParamNameNum:
                            actualParaName = []   
                            for k in range(actualParamNameNum):                     #����õ��ź���������
                                signalParamName = "getSignalParamName"              #����ź���
                                lib.getSignalParamName(acutalInputSignalName,k,signalParamName,19)
                                actualParaName.append(signalParamName.strip('\x00'))     #��ȡ�ӿ��źŲ���������
                            case1.isNotEqual(exceptParamName,actualParaName,'','')
                        print exceptParamName,actualParaName
                        break
                    elif j == (len(exceptInputSignal)-1) and acutalInputSignalName != exceptInputSignal[j]:   #ѭ�����б��β�������ź����Ƶ�ʵ��ֵ������ֵ��һ����ʧ��
                        case1.isNotEqual(exceptInputSignal[j],acutalInputSignalName,'','') 
                            
                            
    def test2OutputSignalInfo(self):
        exceptOutputSignal = []
        sqlInfo = data.check()
        signalInfo = sqlInfo.getSignalInfo(configList[4])         #�����ݿ��л�ȡ�ź���Ϣ
        dom = xmlManage.lxmlReaderModify(signalInfo)
        signalName = dom.getTabNodeValue("//Routing/@name")    #��ȡ���ݿ��е�SignalName
        for signal in signalName: 
            recvFlag = dom.getTabNodeValue("//Routing[@name='%s']/@recvFlag"%signal)
            sendFlag = dom.getTabNodeValue("//Routing[@name='%s']/@sendFlag"%signal)
            if len(recvFlag[0]) == 0 or recvFlag[0] == sendFlag[0]:                        #���recvFlagΪ�ջ��������źŵ�������ź���Ϊ����ź�
                exceptOutputSignal.append(signal)
        print exceptOutputSignal
        exceptOutputSignalNum = len(exceptOutputSignal)         #�����ݿ�õ�������źŵ�����       
        acutalOutputSignalNum = lib.getOutputSignalCount()      #�ӽӿڻ�ȡ����ź�����
        case1.isNotEqual(exceptOutputSignalNum,acutalOutputSignalNum,'','')
            
        if exceptOutputSignalNum == acutalOutputSignalNum:
            for i in range (acutalOutputSignalNum):
                outputSignalName = "getoutputSignalName"
                lib.getOutputSignalName(i,outputSignalName,len(outputSignalName))   #ʵ�ʵ�����ź�����
                acutalOutputSignalName = outputSignalName.strip('\x00')
                for j in range (exceptOutputSignalNum):
                    print "acutalOutputSignalName",acutalOutputSignalName
                    if acutalOutputSignalName == exceptOutputSignal[j]:
                        print "exceptOutputSignal",exceptOutputSignal[j]
                        packId = dom.getTabNodeValue("//Routing[@name='%s']/@packID"%exceptOutputSignal[j])    #���ź���Ϣ�и����ź����ƻ�ȡ��PackID
                        exceptParamName = dom.getTabNodeValue("//Struct[@ID='%s']/Param/@name"%packId[0])           #��Struct��Ϣ�и���ID��Ϣ��ȡ����������
                        exceptParamNameNum = len(exceptParamName)      #���ݿ��д洢���źŵĲ�������
                        actualParamNameNum = lib.getSignalParamCount(acutalOutputSignalName)   #�ӿڻ�ȡ���źŵĲ�������
                        case1.isNotEqual(exceptParamNameNum,actualParamNameNum,'','')    #�ж��źŵĲ��������Ƿ����
                        if  exceptParamNameNum == actualParamNameNum:
                            actualParaName = []   
                            for k in range(actualParamNameNum):
                                signalParamName = "getSignalParamName"
                                lib.getSignalParamName(acutalOutputSignalName,k,signalParamName,19)
                                actualParaName.append(signalParamName.strip('\x00'))     #��ȡ�ӿ��źŲ���������
                            case1.isNotEqual(exceptParamName,actualParaName,'','')
                        print exceptParamName,actualParaName
                        break
                    elif j == (len(exceptOutputSignal)-1) and acutalOutputSignalName != exceptOutputSignal[j]:    #ѭ�����б��β������ź����Ƶ�ʵ��ֵ������ֵ��һ����ʧ��
                        case1.isNotEqual(exceptOutputSignal[j],acutalOutputSignalName,'','')            
           
                    
if __name__ == "__main__":
    unittest.main()