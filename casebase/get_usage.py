#! /usr/bin/env python
#coding=GB18030
import getpass
import os, sys
import shutil
import threading
import time

import psutil
from pywinauto import application
import win32com.client

from casebase import getProcessID, getReg
import pandas as pd
import casebase.case_wrapper as case
configList = case.readIniConfig('QuikLab3.0')


#-----------------判断进程是否存在-------------------------
def check_exist(pro_name):
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_process where Name="%s"'%pro_name)   #获取进程号
    if len(processCodeCov) > 0:     #进程号长度大于0，进程存在返回1
#         print "exist"
        return 1
    else:                                           
        print "%s is not exist"%pro_name
        return 0
    
#-----------------获得进程ID-------------------------
def get_PID():
    _list=getProcessID.process_get_modules()            #获取所有进程名和ID
    for i in range(len(_list)):                                     
        if "MainApp" in _list[i][1]:                    #根据进程名查找ID
            PID=_list[i][0]
            return PID
        
#----------------获得report路径----------------------
def get_path():
    path = sys.path[0] + r"\report"
    if not os.path.exists(path):
        path = os.path.abspath("..") + r"\report"
        print path

    if not os.path.exists(path):
        path = os.path.abspath("..\..") + r"\report"
        print path
    return(path)

#-----------------获得CPU和MEM占用率-----------------------
def get_usage():
    app=application.Application(backend='uia')
    flag=0
    window_name=configList[0]
    
#-------------判断QuikLab3.0是否弹出，并且执行case的线程是否在执行------------------
    while flag == 0:
        mark=0
        try:
            for i in threading.enumerate():                         #获取所有当前运行的线程名称
#                 print str(i)
                if 'runTestCase' in str(i):                         #如果'runTestCase'是否在运行
#                 if 'Thread-1' in str(i):
                    mark=1                                          #mark标记为1
            if mark == 0:                                           #mark=0则'runTestCase'没有运行
                print "Quiklab exception!"
                username = getpass.getuser()                        #获取本机用户名
                despath='C:\\Users\\%s\\temp\\'%username    
#                 despath = getReg.getRegVal("workSpace")
#                 despath = despath+"\\temp\\"
                if os.path.exists(despath):                             #该路径存在则删除
                    shutil.rmtree(despath)
                os._exit(0)  #若tcpSmoke异常退出，则cpu线程退出并删除临时安装文件
            app.connect(title = window_name) 
            flag=1  #QuikLab弹出主界面后，flag设为1，开始获取cpu usage
        except:
            time.sleep(2)
            flag=0
    _path=get_path()+'\Usage.txt'       #设定生成usage.txt的路径
    if os.path.exists(_path):           #删除之前测试的Usage.txt文件
        os.remove(_path)
    PID=get_PID()
#     if PID is None:
#         print "QuikLab didn't start!"
#         exit()
    c=[]
    m=[]
    t=[]
    try:
        def get_cpu_info():
            i = 0
            print "getting Usage... "
            while True:
                if check_exist('MainApp.exe')==0:
                    break
                i = i + 1
                text = open(_path, 'a')
                cpucount = psutil.cpu_count(logical=True)   #CPU核的个数
                process = psutil.Process(int(PID))  #根据PID监视进程
                cpupercent = process.cpu_percent(interval=1)    #设定获取CPU的间隔时间为1s
                cpu = int(cpupercent / cpucount)                #获取CPU的值
                mem = process.memory_percent()                  #获取mem的值
                now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  #获取当前时间
                c.append(cpu)               #每次获取的cpu值存入数组c
                m.append(mem)               #每次获取的mem值存入数组m
                t.append(now)               #每次获取的时间存入数组t
                if cpu <= 50:                   #cpu占用率输入到text中
                    print >> text, now+'         ' +str(cpu) + '                    ' + str(mem)  
                    text.close()
                else:
                    print >> text, now+'         ' +str(cpu) + '                    ' + str(mem)
                    text.close()
                    #cpu占用率超过50时，获取当前执行的模块名称，写入overusage.txt
                    Log_file=get_path()+'log.txt'
                    with open(Log_file,'r') as tf:
                        lines=tf.readlines()
                        fun_name=lines[-1].split(' ')[1]                 #获取log.txt最后一行并取出当前执行模块名称(第二个字符串)
                    over_file=get_path()+'\overusage.txt'                   
                    over=open(over_file,'a')    
                    over.write(fun_name)        #获取当前执行的模块名称，写入overusage.txt
                    over.write('\n')
                    over.close()
        print '进程%s的' % PID + 'CPU监控已经运行，结果将在result.txt生成'
        print "-------------------------------------------------"
        text = open(_path, 'a')
        print >> text,'测试时间'+'                                                       '+'CPU使用率(%)'+ '                 '+'MEM占用率(%)'+'                                                       '+'测试时间'
        text.close()
        get_cpu_info()
    except:
        pass
    finally:
#         if max(c) > 50:
#             with open(_path,'a') as f:
#                 print "CPU占用过高，Performance Test Fail"
#                 f.write("CPU占用过高，Performance Test Fail")
#         else:
#             with open(_path,'a') as f:
#                 print "Performance Test Pass"
#                 f.write('Performance Test Pass')
#         username = getpass.getuser()
#         despath='C:\\Users\\%s\\temp\\'%username
#         shutil.rmtree(despath)   #删除临时安装文件
        print  u'进程%s' % PID + u'已经结束'
        info={u'记录时间':t,
              u'CPU使用率':c,
              u'MEM使用率':m}
        df=pd.DataFrame(info)   #通过pd将信息转为excel结构
        ex=get_path()+'\usage.xls' #命名excel
        df.to_excel(ex)     #将获取的数据转为excel文件
        
if __name__=='__main__':
    get_usage()