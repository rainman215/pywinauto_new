#! /usr/bin/env python
#coding=GB18030
import os
import time

import SendKeys
from pywinauto import application
from pywinauto.timings import Timings

import exception as exp


class Pywin(object):
    def __init__(self):
        self.app = application.Application(backend='uia')
    
    #启动程序    
    @exp._exception
    def start(self,tl_dir,tl_name):
        _dir=os.getcwd()
        os.chdir(tl_dir)
        self.app.start(tl_name)
        os.chdir(_dir)
    
    #连接指定活动窗口    
    @exp._exception
    def connect(self, window_name):
        self.app.connect(title = window_name)
    
    #打印窗口下所有空间属性    
    @exp._exception
    def pr(self, window_name):
        self.app[window_name].print_control_identifiers()
        
    #关闭窗口    
    @exp._exception
    def close(self, window_name,contorl):
        self.app[window_name][contorl].click_input()
        self.app[window_name][u'确定'].click_input()
    
    #窗口最大化    
    @exp._exception
    def max_window(self, window_name):
        self.app[window_name].Maximize()
    
    #菜单栏点击操作    
    @exp._exception
    def menu_click(self, window_name, menulist):
        self.app[window_name].MenuSelect(menulist)
    
    #键盘输入    
    @exp._exception
    def input(self, window_name, controller, content):
        self.app[window_name][controller].type_keys(content)
    
    #鼠标左键单击    
    @exp._exception
    def click(self, window_name, controller):
        self.app[window_name][controller].click_input()
        time.sleep(1)
    
    #鼠标右键单击            
    @exp._exception
    def right_click(self, window_name, controller):
        self.app[window_name][controller].right_click_input()
    
    #鼠标左键双击    
    @exp._exception
    def double_click(self, window_name, controller, x ,y):
        self.app[window_name][controller].double_click_input(button = "left",coords = (x, y))
    
    #激活指定窗口    
    @exp._exception
    def focus(self,window_name,controller):
        self.app[window_name][controller].set_focus()
    
    #鼠标从(dx,dy)拖动控件到（sx,sy)    
    @exp._exception
    def drag(self,window_name,controller,dx,dy,sx,sy):
        self.app[window_name][controller].drag_mouse_input(dst=(dx,dy),src=(sx,sy),button='left',pressed='',absolute=True)
        
    @exp._exception
    #模拟键盘单个快捷键输入
    def Sendk(self,key_name,times):
        SendKeys.SendKeys('{%s %d}'%(key_name,times))    
        
    @exp._exception
    #模拟键盘单个/多个快捷键输入
    def sendKey(self,key_name,times):
        SendKeys.SendKeys("%s %d"%(key_name,times))
        
    #窗口等待超时检测   
    @exp._exception
    def _wait(self, window_name, wait_for, time, interval):
        self.app[window_name].wait(wait_for, timeout=time, retry_interval=interval)
    
    @exp._exception      
    def _wait_child(self, window_name, controller, wait_for, time, interval):
        self.app[window_name][controller].wait(wait_for, timeout=time, retry_interval=interval)
    
    def _wait_child_nor(self, window_name, controller, wait_for, time, interval):
        self.app[window_name][controller].wait(wait_for, timeout=time, retry_interval=interval)
    
    @exp._exception              
    def _wait_not(self,window_name,wait_for, time, interval):
        self.app[window_name].wait_not(wait_for, timeout=time, retry_interval=interval)
    
    @exp._exception         
    def _wait_not_child(self, window_name, controller, wait_for, time, interval):
        self.app[window_name][controller].wait_not(wait_for, timeout=time, retry_interval=interval)
                     
    def texts(self,window_name,controller):
        value = self.app[window_name][controller].texts()
        return(value)
        
if __name__ ==  "__main__":
    pass

    
    
    
    
        