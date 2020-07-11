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

#��ӿͻ��˽ӿ�
def get_pos(pos,x_dis,y_dis):
    window_name=r'QuiKLab V3.0'
    app.click(window_name,pos)  
#     print py.position()
    x1=py.position()[0]          #���pos�ؼ���x����
    y1=py.position()[1]          #���pos�ؼ���y����
    checkbox_x=x1+x_dis          #����ƫ��������xֵ
    checkbox_y=y1+y_dis          #����ƫ��������yֵ
#     py.moveTo(checkbox_x, checkbox_y)
    py.click(checkbox_x,checkbox_y)

#�������
@location._getName
def add_Bus(window_name):                              
    app.click(window_name,u'��������') #���뻷������ 
#     app._wait_child(window_name,u'��������','ready',10,2) 
    ms.right_click(coords=(1577, 492))
    app.Sendk('DOWN',1)
    app.Sendk('ENTER',1)
#�жϵ���"�������"���� 
    app._wait_child(window_name, u'�������', 'ready', 10, 2)
    app.click(window_name, 'ComboBox1')
    app.input(window_name, 'ComboBox1', 'tcp')#��� TCP/IPЭ��
    app.Sendk('ENTER',1)
    app.click(window_name, u'ȷ��') #ȷ��

#���TCP�ͻ��˽ӿ�
@location._getName
def add_TCP_Client_Interface(window_name,ip):                       
    app.connect(window_name)
    app._wait_child(window_name, u'��ӽӿ�', 'ready', 10, 2)
    app.click(window_name, 'ComboBox1')
    time.sleep(1)
    app.Sendk('DOWN', 1)
    app.Sendk('ENTER', 1)
# #���IP
#     app.click(window_name, 'Edit11')
#     app.Sendk('RIGHT', 1)
#     time.sleep(1)
#���ݱ���IP����
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

#���ö˿�
    app.click(window_name, 'Edit9')
    app.input(window_name, 'Edit9', '^a')
    app.input(window_name, 'Edit9', '6060')
    app.click(window_name, u'ȷ��')   #ȷ��
    app._wait_not_child(window_name, u'��ӽӿ�', 'ready', 10, 2)
    
#��ӷ���˽ӿ�
@location._getName
def add_TCP_Service_Interface(window_name):
    app.click(window_name, 'Pane2')
    x=py.position()[0]
    y=py.position()[1]          #���Pane2��x��yֵ
    x_left=x-150
    y_left=y+50                    
    py.rightClick(x_left, y_left)
#     ms.right_click(coords=(923,510))
    app.Sendk('DOWN', 2)
    app.Sendk('ENTER', 1)
    app._wait_child(window_name, u'��ӽӿ�', 'ready', 10, 2)
    app.click(window_name, 'ComboBox1')
    time.sleep(1)
    app.Sendk('DOWN', 2)
    app.Sendk('ENTER', 1)
    app.click(window_name, u'ȷ��')   #ȷ��
    app._wait_not_child(window_name, u'��ӽӿ�', 'ready', 10, 2)
    
#����ź�
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
    app._wait_child(window_name, u'�༭__�ź�__signal', 'ready', 10, 2)
    app.click(window_name, 'ComboBox5')
    time.sleep(1)
    app.input(window_name, 'ComboBox5', 'I_Block')  #������ݽṹ
    app.Sendk('ENTER', 1)
    app.click(window_name, u'ȷ��')   #ȷ��
    app._wait_not_child(window_name, u'�༭__�ź�__signal', 'ready', 10, 2)

#�½���������
@location._getName
def add_TCP_Case(window_name):
    key.setenv()
    key.attr_Control.get_Allattr(window_name)
    con=key.attr_Control('��������')
    con_val=con.get_attrName()
    print con_val
#     print(con_val)
    app.click(window_name, con_val)
#     app.click(window_name, 'TreeItem6') #14421
    controller='TreeView2'
#     app._wait_child(window_name, u'����������', 'ready', 10, 2)
#     try:
#         app._wait_child_nor(window_name,u'�������','ready',4,2)                #�������������
#         print "111"
#         app._wait_child(window_name,u'�������','ready',10,2) #����Ƿ������������UI�ؼ�
#         if 'PC' in getLatestRev.getRev('exe').split('\\')[-1]:
#         controller='TreeView2'
#         else:
#             if 'PC' in getLatestRev.getRev('exe').split('\\')[-1]:
#                 controller='TreeView2'                  #UI�������������ؼ���������frameֵ
#         print controller
#         print "exist"
#     except:
#         print "222"
#         controller='TreeView2'                  #UI����û���������ؼ���������frameֵ
#         print controller
    app.right_click(window_name, controller)                #�������������
    app.Sendk('DOWN', 1)
    app.Sendk('ENTER',1)
    app._wait_child(window_name, u'�½���������', 'ready', 10, 2)
    app.click(window_name, u'ȷ��')
#     app._wait_not_child(window_name, u'�½���������', 'ready', 10, 2)
    app._wait_child(window_name, u'��������', 'ready', 10, 2)
    app.right_click(window_name,u'��������')    #��������root
    time.sleep(1)
    app.Sendk('DOWN',4)
    app.Sendk('ENTER',1)
    app._wait_child(window_name, u'�½���������', 'ready', 10, 2)
#     app.Sendk('TAB',2)
    app.input(window_name, 'Edit1', 'content2')     #����������
    app.click(window_name,u'ȷ��')
    app.click(window_name,u'��������')
    app.Sendk('RIGHT',1)
    app.Sendk('DOWN',1)
    app._wait_child(window_name, 'content2', 'ready', 10, 2)
     
 
#����ź�
    app.click(window_name, u'������������')
    app.click(window_name, u'����źű���')
    app._wait_child(window_name, u'ѡ���źŶԻ���', 'ready', 10, 2)
    get_pos('signal',-95,0)
#     ms.click(coords=(602,450))      #ѡ���ź�
    app.click(window_name, u'ȷ��')
    app._wait_child(window_name, 'signal', 'ready', 10, 2)
# 
# 
# #���������༭    
#--------------------�����ź�����-------------------------------
    app.click(window_name, u'���������༭')
    key.attr_Control.get_Allattr(window_name)
    con=key.attr_Control('������')
    con_val=con.get_attrName()          #��ȡ�����̿ؼ�����ֵ
#     print(con_val)
    app.right_click(window_name, con_val)      #�Ҽ�"������"����ֵcon_val
#     app.right_click(window_name, 'TreeItem12') #14421
    app.Sendk('UP', 1)
    app.Sendk('ENTER', 1)   #��������
    app._wait_child(window_name, u'ɾ��', 'ready', 10, 2)
    app.click(window_name, 'ComboBox0')
    app.Sendk('DOWN', 1)
    app.Sendk('ENTER', 1)   #�����ź�����
    app.click(window_name, 'Edit3')
    SendKeys.SendKeys("^a")
    app.input(window_name, 'Edit3', 10) #ѭ����������Ϊ10
    app.click(window_name, 'Signal')
    get_pos(u'������',-40,33)
    app.click(window_name, u'ȷ��')

#--------------------�޸��źŸ�ֵ-------------------------------
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
    get_pos(u'����ֵ�ı���', 0, 30)
    py.rightClick()
    app.Sendk('DOWN', 2)
    app.Sendk('ENTER', 1)       #ɾ����ֵ���ʽ
    app.click(window_name, u'ȷ��')
    get_pos(u'���ʽ', 0, 30)
    py.doubleClick()            #˫���޸ı��ʽ
    time.sleep(1)
    SendKeys.SendKeys("^a")
    SendKeys.SendKeys("15")  #��ֵ�ź�P1=15
    app.click(window_name, u'Ĭ������')
    app.click(window_name, u'ȷ��')

#--------------------�����ź�-------------------------------
    app.right_click(window_name,u'ѭ��[10��]')
    app.Sendk('DOWN', 1)
    app.Sendk('RIGHT', 1)
    app.Sendk('DOWN', 1)
    app.Sendk('ENTER', 1)   #ѡ������ź�
    get_pos('signal', -110, 0)
    app.click(window_name, u'Ĭ������')
    app.click(window_name, u'ȷ��')

#--------------------�Ƚ�����ֵ-------------------------------
    app.right_click(window_name,u'ѭ��[10��]')
    app.Sendk('UP', 1)
    app.Sendk('ENTER', 1)
    app._wait_child(window_name, u'ɾ��', 'ready', 10, 2)
    app.click(window_name, 'ComboBox0')
    app.Sendk('DOWN', 2)
    app.Sendk('ENTER', 1)   #����ֵ�Ƚ�ѡ��
    app.click(window_name, 'signal')
    get_pos(u'������',-40,33)
    app._wait_child(window_name,u'�̶�ֵ��','ready',4,2)
    print "right"
    app.click(window_name, 'Edit0')
    app.input(window_name, 'Edit0', 15)
    app.click(window_name, u'ȷ��')
    
#     ms.press(button='left',coords=(600,229))
#     ms.move(coords=(661, 646))
#     ms.release(button='left', coords=(661, 646))
#     app.click(window_name, u'ȷ��')
#     app._wait_child(window_name, u'����[signal]', 'ready', 10, 2)

# #------------------��������--------------------------
# @location._getName
# def run_case(window_name):
#     app.click(window_name,u'��������')
#     app._wait_child(window_name, u'��ʼ�²���', 'ready', 10, 2)
#     app.click(window_name, 'content2*')
#     app.click(window_name, 'ComboBox4')
#     time.sleep(1)
#     app.Sendk('UP', 2)
#     app.Sendk('ENTER', 1)    
#     app.click(window_name, u'��ʼ')
#     try:
#         app._wait_child_nor(window_name,u'��','ready',10,2) 
#         app.click(window_name, u"��")
#     except:
#         pass
#     time.sleep(10)
#     app._wait_not_child(window_name, u'����', 'ready', 10, 2)
#     time.sleep(2)
#     app.click(window_name,u'����')
#     time.sleep(2)
#     app.click(window_name, u'��������')
# #     times=-2
#     while True:
#         try:
#             app._wait_child_nor(window_name, u'��һ��', 'enabled', 10, 1)
#             app.click(window_name, u'��һ��')
#         except:
#             break
# #         time.sleep(0.5)
# 
# #------------------�ȶԵ��Խ��--------------------------
# @location._getName
# def compareRes():
#     workSpace=getReg.getRegVal("workSpace")
#     filePath='%s\\runtime\\'%workSpace
#     print filePath
#     fileName=time.strftime('%Y_%m_%d',time.localtime((time.time()))) +'.log'
#     logFile=filePath+fileName
#     print logFile
# #     case.isNotIn('δͨ��',logFile, True,'���Գɹ�')
# #     case.isNotIn('ʧ��',logFile,'���Գɹ�')
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
#     case.isNotIn('δͨ��',logFile,'���Գɹ�')

    
if __name__=='__main__':
    pass
    app=pywin.Pywin()
    window_name =u'QuiKLab'
#     window_name =u'��ӽӿ�'
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
