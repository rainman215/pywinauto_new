#! /usr/bin/env python
#coding=GB18030
import getpass
import os
import socket
import time
import unittest

from casebase import getReg
import casebase.TCP_Component as tcp
import casebase.case_wrapper as case
from casebase.checkName import check
from casebase import sshProtocol

import casebase.init as init

configList = case.readIniConfig('QuikLab3.0')       #��ȡ�����ļ����ص����鴫��configList
ip=[]
host=socket.gethostname()                           #��ȡ������Ϣ
ip=socket.gethostbyname(host).split('.')   #��ñ���IP����������ip
print "Current ip is:",ip
window_name =configList[0]
getName=check()
proName=getName.getProName(configList[3])           #��ȡ��


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass
#         import casebase.QuikLab_Install as install                
#         install._checkInstall()                                #��װQuikLab��λ������
#         sshProtocol.insTar()                                    #��װQuikLab��λ����������
#         username = getpass.getuser()                            #��ȡ�����û���
#         despath='C:\\Users\\%s\\temp\\'%username                
#         init._init_rmLog()                                     #ɾ��report���ļ������log�ļ�
#         flag=despath+'tag.txt'
#         with open(flag,'r') as f:                                #����tag.txt�����ж�QuikLab��װ�Ƿ�ɹ�
#             for i in f:                                            
#                 if i == '0':
#                     exit()
#         softSetupDir = getReg.getRegVal('applicationPath')    #����ע�����Ϣ��ȡQuikLab��װĿ¼
#         appPath = softSetupDir + '\\MainApp.exe'                
#         case.confDataBase(softSetupDir,appPath,configList[4])    #ִ��QuikLab����������

    @classmethod
    def tearDownClass(self):
        pass
        os.system('taskkill /IM MainApp.exe /F')                #kill QuikLab����
    def test1_Login(self):
        softSetupDir = getReg.getRegVal('applicationPath')      #����ע�����Ϣ��ȡQuikLab��װĿ¼
        appPath = softSetupDir + '\\MainApp.exe'
        case.login(softSetupDir,appPath,configList[1],configList[2])    #����QuikLab�����е�¼����
   
    def test2_CreatPro(self):
        case.creat_pro(window_name,proName)                     #������Ŀ����
             
    def test3_LoadPro(self):
        case.unload_pro(window_name)                            #ж����Ŀ
        case.load_pro(window_name, proName)                     #������Ŀ
            
    def test4_ConfigEnviro(self):
        case.add_Bus(window_name)                               #�������
        case.add_dev(window_name)                               #����豸
        case.add_tar(window_name,ip)                            #���Ŀ���
        tcp.add_TCP_Client_Interface(window_name,ip)            #��ӿͻ���
        tcp.add_TCP_Service_Interface(window_name)              #��ӷ����
        tcp.add_TCP_Signal(window_name)                         #����ź�
        tcp.add_TCP_Case(window_name)                           #�������
    def test5_RunCase(self):
        case.run_case(window_name)                              #ִ������
        case.compareRes()                                       #�Ƚϲ��Խ��
    
if __name__ == "__main__":
    unittest.main()