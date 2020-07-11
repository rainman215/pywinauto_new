#! /usr/bin/env python
#coding=GB18030
import getpass
import os
import sys
import time

import SendKeys
from pywinauto import mouse as ms

import auto_lib as pywin 
import casebase.case_wrapper as case
import casebase.findkey as key
import casebase.getReg as getReg
import locFun as location
import pyautogui as py
import getLatestRev

app=pywin.Pywin()

#添加客户端接口
def get_pos(pos,x_dis,y_dis):
    window_name=r'QuiKLab V3.0'
    app.click(window_name,pos)  
#     print py.position()
    x1=py.position()[0]          #获得pos控件的x坐标
    y1=py.position()[1]          #获得pos控件的y坐标
    checkbox_x=x1+x_dis          #根据偏移量设置x值
    checkbox_y=y1+y_dis          #根据偏移量设置y值
#     py.moveTo(checkbox_x, checkbox_y)
    py.click(checkbox_x,checkbox_y)

#添加总线
@location._getName
def add_Bus(window_name):                              
    app.click(window_name,u'环境配置') #进入环境配置 
#     app._wait_child(window_name,u'总线索引','ready',10,2) 
    ms.right_click(coords=(1577, 492))
    app.Sendk('DOWN',1)
    app.Sendk('ENTER',1)
#判断弹出"添加总线"窗口 
    app._wait_child(window_name, u'添加总线', 'ready', 10, 2)
    app.click(window_name, 'ComboBox1')
    app.input(window_name, 'ComboBox1', 'tcp')#添加 TCP/IP协议
    app.Sendk('ENTER',1)
    app.click(window_name, u'确定') #确定

#添加TCP客户端接口
@location._getName
def add_TCP_Client_Interface(window_name,ip):                       
    app.connect(window_name)
    app._wait_child(window_name, u'添加接口', 'ready', 10, 2)
    app.click(window_name, 'ComboBox1')
    time.sleep(1)
    app.Sendk('DOWN', 1)
    app.Sendk('ENTER', 1)
# #添加IP
#     app.click(window_name, 'Edit11')
#     app.Sendk('RIGHT', 1)
#     time.sleep(1)
#根据本机IP输入
    app.click(window_name, 'Edit10')
    app.input(window_name, 'Edit10', '^a')
    app.input(window_name, 'Edit10', '19')
    app.Sendk('2', 1)
    app.click(window_name, 'Edit11')
    app.input(window_name, 'Edit11', '^a')
    app.input(window_name, 'Edit11', '16')
    app.Sendk('8', 1)
    app.click(window_name, 'Edit12')
    app.input(window_name, 'Edit12', '^a')
    app.input(window_name, 'Edit12', '1')
#     app.Sendk('.', 1)
    app.click(window_name, 'Edit13')
    app.input(window_name, 'Edit13', '^a')
    app.input(window_name, 'Edit13', ip[3])  

#设置端口
    app.click(window_name, 'Edit9')
    app.input(window_name, 'Edit9', '^a')
    app.input(window_name, 'Edit9', '6060')
    app.click(window_name, u'确定')   #确定
    app._wait_not_child(window_name, u'添加接口', 'ready', 10, 2)
    
#添加服务端接口
@location._getName
def add_TCP_Service_Interface(window_name):
    app.click(window_name, 'Pane2')
    x=py.position()[0]
    y=py.position()[1]          #获得Pane2的x，y值
    x_left=x-150
    y_left=y+50                    
    py.rightClick(x_left, y_left)
#     ms.right_click(coords=(923,510))
    app.Sendk('DOWN', 2)
    app.Sendk('ENTER', 1)
    app._wait_child(window_name, u'添加接口', 'ready', 10, 2)
    app.click(window_name, 'ComboBox1')
    time.sleep(1)
    app.Sendk('DOWN', 2)
    app.Sendk('ENTER', 1)
    app.click(window_name, u'确定')   #确定
    app._wait_not_child(window_name, u'添加接口', 'ready', 10, 2)
    
#添加信号
@location._getName
def add_TCP_Signal(window_name):
    app.click(window_name, 'Pane2')
    x=py.position()[0]
    y=py.position()[1]
    x_left=x-174
    y_left=y-5
    x_right=x-135
    y_right=y-5
#     ms.press(button='left', coords=(902, 456))
#     ms.move(coords=(940, 456))
#     ms.release(button='left', coords=(940, 456))
    ms.press(button='left', coords=(x_left,y_left))
    ms.move(coords=(x_right,y_right))
    ms.release(button='left', coords=(x_right,y_right))
    app._wait_child(window_name, u'编辑__信号__signal', 'ready', 10, 2)
    app.click(window_name, 'ComboBox5')
    time.sleep(1)
    app.input(window_name, 'ComboBox5', 'I_Block')  #添加数据结构
    app.Sendk('ENTER', 1)
    app.click(window_name, u'确定')   #确定
    app._wait_not_child(window_name, u'编辑__信号__signal', 'ready', 10, 2)

#新建测试用例
@location._getName
def add_TCP_Case(window_name):
    key.setenv()
    key.attr_Control.get_Allattr(window_name)
    con=key.attr_Control('测试用例')
    con_val=con.get_attrName()
    print con_val
#     print(con_val)
    app.click(window_name, con_val)
#     app.click(window_name, 'TreeItem6') #14421
    controller='TreeView2'
#     app._wait_child(window_name, u'测试用例集', 'ready', 10, 2)
#     try:
#         app._wait_child_nor(window_name,u'需求管理','ready',4,2)                #需求管理界面存在
#         print "111"
#         app._wait_child(window_name,u'需求管理','ready',10,2) #检查是否存在需求管理的UI控件
#         if 'PC' in getLatestRev.getRev('exe').split('\\')[-1]:
#         controller='TreeView2'
#         else:
#             if 'PC' in getLatestRev.getRev('exe').split('\\')[-1]:
#                 controller='TreeView2'                  #UI界面有需求管理控件，用例集frame值
#         print controller
#         print "exist"
#     except:
#         print "222"
#         controller='TreeView2'                  #UI界面没有需求管理控件，用例集frame值
#         print controller
    app.right_click(window_name, controller)                #点击用例集界面
    app.Sendk('DOWN', 1)
    app.Sendk('ENTER',1)
    app._wait_child(window_name, u'新建用例分类', 'ready', 10, 2)
    app.click(window_name, u'确定')
#     app._wait_not_child(window_name, u'新建用例分类', 'ready', 10, 2)
    app._wait_child(window_name, u'用例分类', 'ready', 10, 2)
    app.right_click(window_name,u'用例分类')    #测试用例root
    time.sleep(1)
    app.Sendk('DOWN',4)
    app.Sendk('ENTER',1)
    app._wait_child(window_name, u'新建测试用例', 'ready', 10, 2)
#     app.Sendk('TAB',2)
    app.input(window_name, 'Edit1', 'content2')     #输入用例名
    app.click(window_name,u'确定')
    app.click(window_name,u'用例分类')
    app.Sendk('RIGHT',1)
    app.Sendk('DOWN',1)
    app._wait_child(window_name, 'content2', 'ready', 10, 2)
     
 
#添加信号
    app.click(window_name, u'测试用例变量')
    app.click(window_name, u'添加信号变量')
    app._wait_child(window_name, u'选择信号对话框', 'ready', 10, 2)
    get_pos('signal',-95,0)
#     ms.click(coords=(602,450))      #选中信号
    app.click(window_name, u'确定')
    app._wait_child(window_name, 'signal', 'ready', 10, 2)
# 
# 
# #测试用例编辑    
#--------------------快速信号生成-------------------------------
    app.click(window_name, u'测试用例编辑')
    key.attr_Control.get_Allattr(window_name)
    con=key.attr_Control('主流程')
    con_val=con.get_attrName()          #获取主流程控件属性值
#     print(con_val)
    app.right_click(window_name, con_val)      #右键"主流程"属性值con_val
#     app.right_click(window_name, 'TreeItem12') #14421
    app.Sendk('UP', 1)
    app.Sendk('ENTER', 1)   #快速生成
    app._wait_child(window_name, u'删除', 'ready', 10, 2)
    app.click(window_name, 'ComboBox0')
    app.Sendk('DOWN', 1)
    app.Sendk('ENTER', 1)   #快速信号生成
    app.click(window_name, 'Edit3')
    SendKeys.SendKeys("^a")
    app.input(window_name, 'Edit3', 10) #循环次数设置为10
    app.click(window_name, 'Signal')
    get_pos(u'域名称',-40,33)
    app.click(window_name, u'确定')

#--------------------修改信号赋值-------------------------------
    app.click(window_name,con_val)
#     app.right_click(window_name, 'TreeItem12') #14421
#     app.Sendk('DOWN', 1)
    app.Sendk('RIGHT',1)
    app.Sendk('DOWN', 1)
    app.Sendk('RIGHT',1)
    app.Sendk('DOWN', 1)
    get_pos(con_val, 0, 40)
#     get_pos('TreeItem12', 0, 40) #14421
    py.click()
    get_pos(u'被赋值的变量', 0, 30)
    py.rightClick()
    app.Sendk('DOWN', 2)
    app.Sendk('ENTER', 1)       #删除赋值表达式
    app.click(window_name, u'确定')
    get_pos(u'表达式', 0, 30)
    py.doubleClick()            #双击修改表达式
    time.sleep(1)
    SendKeys.SendKeys("^a")
    SendKeys.SendKeys("15")  #赋值信号P1=15
    app.click(window_name, u'默认名称')
    app.click(window_name, u'确定')

#--------------------接收信号-------------------------------
    app.right_click(window_name,u'循环[10次]')
    app.Sendk('DOWN', 1)
    app.Sendk('RIGHT', 1)
    app.Sendk('DOWN', 1)
    app.Sendk('ENTER', 1)   #选择接收信号
    get_pos('signal', -110, 0)
    app.click(window_name, u'默认名称')
    app.click(window_name, u'确定')

#--------------------比较期望值-------------------------------
    app.right_click(window_name,u'循环[10次]')
    app.Sendk('UP', 1)
    app.Sendk('ENTER', 1)
    app._wait_child(window_name, u'删除', 'ready', 10, 2)
    app.click(window_name, 'ComboBox0')
    app.Sendk('DOWN', 2)
    app.Sendk('ENTER', 1)   #期望值比较选项
    app.click(window_name, 'signal')
    get_pos(u'域名称',-40,33)
    app._wait_child(window_name,u'固定值：','ready',4,2)
    print "right"
    app.click(window_name, 'Edit0')
    app.input(window_name, 'Edit0', 15)
    app.click(window_name, u'确定')
    
#     ms.press(button='left',coords=(600,229))
#     ms.move(coords=(661, 646))
#     ms.release(button='left', coords=(661, 646))
#     app.click(window_name, u'确定')
#     app._wait_child(window_name, u'发送[signal]', 'ready', 10, 2)

# #------------------单步调试--------------------------
# @location._getName
# def run_case(window_name):
#     app.click(window_name,u'启动测试')
#     app._wait_child(window_name, u'开始新测试', 'ready', 10, 2)
#     app.click(window_name, 'content2*')
#     app.click(window_name, 'ComboBox4')
#     time.sleep(1)
#     app.Sendk('UP', 2)
#     app.Sendk('ENTER', 1)    
#     app.click(window_name, u'开始')
#     try:
#         app._wait_child_nor(window_name,u'是','ready',10,2) 
#         app.click(window_name, u"是")
#     except:
#         pass
#     time.sleep(10)
#     app._wait_not_child(window_name, u'继续', 'ready', 10, 2)
#     time.sleep(2)
#     app.click(window_name,u'单步')
#     time.sleep(2)
#     app.click(window_name, u'单步运行')
# #     times=-2
#     while True:
#         try:
#             app._wait_child_nor(window_name, u'下一步', 'enabled', 10, 1)
#             app.click(window_name, u'下一步')
#         except:
#             break
# #         time.sleep(0.5)
# 
# #------------------比对调试结果--------------------------
# @location._getName
# def compareRes():
#     workSpace=getReg.getRegVal("workSpace")
#     filePath='%s\\runtime\\'%workSpace
#     print filePath
#     fileName=time.strftime('%Y_%m_%d',time.localtime((time.time()))) +'.log'
#     logFile=filePath+fileName
#     print logFile
# #     case.isNotIn('未通过',logFile, True,'测试成功')
# #     case.isNotIn('失败',logFile,'测试成功')
#     despath = sys.path[0] + r"\report"
#     if not os.path.exists(despath):
#         despath = os.path.abspath("..") + r"\report"
# 
#     if not os.path.exists(despath):
#         despath = os.path.abspath("..\..") + r"\report"
# #     os.chdir(despath)
# #     despath=os.getcwd()
#     print despath,"..."
#     os.system('copy %s %s'%(logFile,despath))
#     case.isNotIn('未通过',logFile,'测试成功')

    
if __name__=='__main__':
    pass
    app=pywin.Pywin()
    window_name =u'QuiKLab'
#     window_name =u'添加接口'
    time.sleep(2)
    app.connect(window_name)
#     app.click(window_name, 'Pane2')
#     app.click(window_name, 'TreeView2')
#     add_Bus(window_name)                                      

    add_TCP_Client_Interface(window_name,[192,168,1,5])
#     add_TCP_Service_Interface(window_name)
#     add_TCP_Signal(window_name)
#     get_pos('signal', -110, 0)
#     add_TCP_Case(window_name)
#     run_case(window_name)
#     compareRes()
