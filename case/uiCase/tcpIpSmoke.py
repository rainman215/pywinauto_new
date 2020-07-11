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

configList = case.readIniConfig('QuikLab3.0')       #读取配置文件返回的数组传给configList
ip=[]
host=socket.gethostname()                           #获取本机信息
ip=socket.gethostbyname(host).split('.')   #获得本机IP并存入数组ip
print "Current ip is:",ip
window_name =configList[0]
getName=check()
proName=getName.getProName(configList[3])           #获取并


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass
#         import casebase.QuikLab_Install as install                
#         install._checkInstall()                                #安装QuikLab上位机程序
#         sshProtocol.insTar()                                    #安装QuikLab下位机程序并启动
#         username = getpass.getuser()                            #获取本地用户名
#         despath='C:\\Users\\%s\\temp\\'%username                
#         init._init_rmLog()                                     #删除report下文件夹外的log文件
#         flag=despath+'tag.txt'
#         with open(flag,'r') as f:                                #根据tag.txt内容判断QuikLab安装是否成功
#             for i in f:                                            
#                 if i == '0':
#                     exit()
#         softSetupDir = getReg.getRegVal('applicationPath')    #根据注册表信息获取QuikLab安装目录
#         appPath = softSetupDir + '\\MainApp.exe'                
#         case.confDataBase(softSetupDir,appPath,configList[4])    #执行QuikLab配置项设置

    @classmethod
    def tearDownClass(self):
        pass
        os.system('taskkill /IM MainApp.exe /F')                #kill QuikLab进程
    def test1_Login(self):
        softSetupDir = getReg.getRegVal('applicationPath')      #根据注册表信息获取QuikLab安装目录
        appPath = softSetupDir + '\\MainApp.exe'
        case.login(softSetupDir,appPath,configList[1],configList[2])    #启动QuikLab并进行登录测试
   
    def test2_CreatPro(self):
        case.creat_pro(window_name,proName)                     #创建项目测试
             
    def test3_LoadPro(self):
        case.unload_pro(window_name)                            #卸载项目
        case.load_pro(window_name, proName)                     #加载项目
            
    def test4_ConfigEnviro(self):
        case.add_Bus(window_name)                               #添加总线
        case.add_dev(window_name)                               #添加设备
        case.add_tar(window_name,ip)                            #添加目标机
        tcp.add_TCP_Client_Interface(window_name,ip)            #添加客户端
        tcp.add_TCP_Service_Interface(window_name)              #添加服务端
        tcp.add_TCP_Signal(window_name)                         #添加信号
        tcp.add_TCP_Case(window_name)                           #添加用例
    def test5_RunCase(self):
        case.run_case(window_name)                              #执行用例
        case.compareRes()                                       #比较测试结果
    
if __name__ == "__main__":
    unittest.main()