#! /usr/bin/env python
#coding=GB18030
import time
from pywinauto import mouse as ms
import auto_lib as pywin 
import locFun as location
app=pywin.Pywin()

@location._getName
def add_Bus(window_name,busName):
    app.click(window_name,u'环境配置') #进入环境配置 
    ms.right_click(coords=(1577, 492))
    app.Sendk('DOWN', 1)
    app.Sendk('ENTER',1)
#判断弹出"添加总线"窗口 
    app._wait_child(window_name, u'添加总线', 'ready', 10, 2)
    app.click(window_name, 'ComboBox1')
    app.input(window_name, 'ComboBox1', busName)#添加 TCP/IP协议
    app.Sendk('ENTER',1)
    app.click(window_name, u'确定') #确定

#添加设备  
@location._getName
def add_dev(window_name):
    app.right_click(window_name,'Pane2')
    app.Sendk('DOWN', 3)
    app.Sendk('ENTER',1) #选择添加设备
    app._wait_child(window_name, u'添加设备', 'ready', 10, 2)

#添加目标机
@location._getName
def add_tar(window_name,ip):
    app.click(window_name, 'ComboBox1')
    time.sleep(1)
    app.Sendk('UP', 1)
    app.Sendk('ENTER', 1)

#添加IP
    app.click(window_name, 'Edit2')
    app.input(window_name, 'Edit2', '^a')
    app.input(window_name, 'Edit2', '19')
    app.Sendk('2', 1)
    app.click(window_name,'Edit3')
    app.input(window_name, 'Edit3', '^a')
    app.input(window_name, 'Edit3', '16')
    app.Sendk('8', 1)
    app.click(window_name,'Edit4')
    app.input(window_name, 'Edit4', '^a')
    app.input(window_name, 'Edit4', '1')
#     app.Sendk('.', 1)
    app.click(window_name,'Edit5')
    app.input(window_name, 'Edit5', '^a')
    app.input(window_name, 'Edit5', ip[3])
    app.click(window_name, u'确定')#确定
if __name__=='__main__':
    app=pywin.Pywin()
    window_name =u'QuiKLab V3.0'
    app.connect(window_name)
    time.sleep(2)
#     add_Bus(window_name)
    add_dev(window_name)
    add_tar(window_name,[192,168,1,5])