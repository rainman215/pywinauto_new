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
        lib.initQuiKLabPlatform()          #初始化QuiKLab平台       
        lib.loadProject(configList[4])            #加载工程
        
        
    @classmethod
    def tearDownClass(self):
        lib.releaseQuiKLabPlatform()         #释放QuiKLab平台


    def test1InputSignalInfo(self):
        exceptInputSignal = []
        sqlInfo = data.check()
        signalInfo = sqlInfo.getSignalInfo(configList[4])         #从数据库中获取信号信息
        dom = xmlManage.lxmlReaderModify(signalInfo)
        signalName = dom.getTabNodeValue("//Routing/@name")    #获取数据库中的SignalName
        for signal in signalName: 
            recvFlag = dom.getTabNodeValue("//Routing[@name='%s']/@recvFlag"%signal)
            sendFlag = dom.getTabNodeValue("//Routing[@name='%s']/@sendFlag"%signal)
            if len(recvFlag[0]) != 0:                        #如果recvFlag不为空则为输入信号
                exceptInputSignal.append(signal)
        exceptInputSignalNum = len(exceptInputSignal)         #从数据库得到的输入信号的数量       
        acutalInputSignalNum = lib.getInputSignalCount()      #从接口获取信号数量
        case1.isNotEqual(exceptInputSignalNum,acutalInputSignalNum,'','')
            
        if exceptInputSignalNum == acutalInputSignalNum:
            for i in range (acutalInputSignalNum):
                inputSignalName = "getInputSignalName"
                lib.getInputSignalName(i,inputSignalName,len(inputSignalName))   #实际的输入信号名称
                acutalInputSignalName = inputSignalName.strip('\x00')
                for j in range (exceptInputSignalNum):
                    print "acutalInputSignalName",acutalInputSignalName
                    if acutalInputSignalName == exceptInputSignal[j]:
                        print "exceptInputSignal",exceptInputSignal[j]
                        packId = dom.getTabNodeValue("//Routing[@name='%s']/@packID"%exceptInputSignal[j])    #在信号信息中根据信号名称获取到PackID
                        exceptParamName = dom.getTabNodeValue("//Struct[@ID='%s']/Param/@name"%packId[0])           #在Struct信息中根据ID信息获取到参数名称
                        exceptParamNameNum = len(exceptParamName)      #数据库中存储的信号的参数个数
                        actualParamNameNum = lib.getSignalParamCount(acutalInputSignalName)   #接口获取的信号的参数个数
                        case1.isNotEqual(exceptParamNameNum,actualParamNameNum,'','')   #判断信号的参数个数是否相等
                        if  exceptParamNameNum == actualParamNameNum:
                            actualParaName = []   
                            for k in range(actualParamNameNum):                     #按获得的信号数量遍历
                                signalParamName = "getSignalParamName"              #获得信号名
                                lib.getSignalParamName(acutalInputSignalName,k,signalParamName,19)
                                actualParaName.append(signalParamName.strip('\x00'))     #获取接口信号参数的名称
                            case1.isNotEqual(exceptParamName,actualParaName,'','')
                        print exceptParamName,actualParaName
                        break
                    elif j == (len(exceptInputSignal)-1) and acutalInputSignalName != exceptInputSignal[j]:   #循环至列表结尾且输入信号名称的实际值与期望值不一致则失败
                        case1.isNotEqual(exceptInputSignal[j],acutalInputSignalName,'','') 
                            
                            
    def test2OutputSignalInfo(self):
        exceptOutputSignal = []
        sqlInfo = data.check()
        signalInfo = sqlInfo.getSignalInfo(configList[4])         #从数据库中获取信号信息
        dom = xmlManage.lxmlReaderModify(signalInfo)
        signalName = dom.getTabNodeValue("//Routing/@name")    #获取数据库中的SignalName
        for signal in signalName: 
            recvFlag = dom.getTabNodeValue("//Routing[@name='%s']/@recvFlag"%signal)
            sendFlag = dom.getTabNodeValue("//Routing[@name='%s']/@sendFlag"%signal)
            if len(recvFlag[0]) == 0 or recvFlag[0] == sendFlag[0]:                        #如果recvFlag为空或者输入信号等于输出信号则为输出信号
                exceptOutputSignal.append(signal)
        print exceptOutputSignal
        exceptOutputSignalNum = len(exceptOutputSignal)         #从数据库得到的输出信号的数量       
        acutalOutputSignalNum = lib.getOutputSignalCount()      #从接口获取输出信号数量
        case1.isNotEqual(exceptOutputSignalNum,acutalOutputSignalNum,'','')
            
        if exceptOutputSignalNum == acutalOutputSignalNum:
            for i in range (acutalOutputSignalNum):
                outputSignalName = "getoutputSignalName"
                lib.getOutputSignalName(i,outputSignalName,len(outputSignalName))   #实际的输出信号名称
                acutalOutputSignalName = outputSignalName.strip('\x00')
                for j in range (exceptOutputSignalNum):
                    print "acutalOutputSignalName",acutalOutputSignalName
                    if acutalOutputSignalName == exceptOutputSignal[j]:
                        print "exceptOutputSignal",exceptOutputSignal[j]
                        packId = dom.getTabNodeValue("//Routing[@name='%s']/@packID"%exceptOutputSignal[j])    #在信号信息中根据信号名称获取到PackID
                        exceptParamName = dom.getTabNodeValue("//Struct[@ID='%s']/Param/@name"%packId[0])           #在Struct信息中根据ID信息获取到参数名称
                        exceptParamNameNum = len(exceptParamName)      #数据库中存储的信号的参数个数
                        actualParamNameNum = lib.getSignalParamCount(acutalOutputSignalName)   #接口获取的信号的参数个数
                        case1.isNotEqual(exceptParamNameNum,actualParamNameNum,'','')    #判断信号的参数个数是否相等
                        if  exceptParamNameNum == actualParamNameNum:
                            actualParaName = []   
                            for k in range(actualParamNameNum):
                                signalParamName = "getSignalParamName"
                                lib.getSignalParamName(acutalOutputSignalName,k,signalParamName,19)
                                actualParaName.append(signalParamName.strip('\x00'))     #获取接口信号参数的名称
                            case1.isNotEqual(exceptParamName,actualParaName,'','')
                        print exceptParamName,actualParaName
                        break
                    elif j == (len(exceptOutputSignal)-1) and acutalOutputSignalName != exceptOutputSignal[j]:    #循环至列表结尾且输出信号名称的实际值与期望值不一致则失败
                        case1.isNotEqual(exceptOutputSignal[j],acutalOutputSignalName,'','')            
           
                    
if __name__ == "__main__":
    unittest.main()