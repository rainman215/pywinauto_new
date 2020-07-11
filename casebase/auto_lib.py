#! /usr/bin/env python
#coding=GB18030
from pywinauto import application
import SendKeys
import time
import os
import sys
class Pywin(object):
    def __init__(self):
        self.app = application.Application(backend='uia')
    def start(self,tl_dir,tl_name):
        _dir=os.getcwd()
        os.chdir(tl_dir)
        self.app.start(tl_name)
        os.chdir(_dir)
    def connect(self, window_name):
        self.app.connect(title = window_name)
        time.sleep(1)
    def pr(self, window_name):
        self.app[window_name].print_control_identifiers()
    def close(self, window_name,contorl):
        self.app[window_name][contorl].click_input()
        self.app[window_name][u'确定'].click_input()
        time.sleep(1)
    def max_window(self, window_name):
        self.app[window_name].Maximize()
        time.sleep(1)
    def menu_click(self, window_name, menulist):
        self.app[window_name].MenuSelect(menulist)
        time.sleep(1)
    def input(self, window_name, controller, content):
        self.app[window_name][controller].type_keys(content)
        time.sleep(1)
    def click(self, window_name, controller):
        self.app[window_name][controller].click_input()
        time.sleep(1)
    def right_click(self, window_name, controller):
        self.app[window_name][controller].right_click_input()
    def double_click(self, window_name, controller, x ,y):
        self.app[window_name][controller].double_click_input(button = "left",coords = (x, y))
        time.sleep(1)
    def focus(self,window_name,controller):
        self.app[window_name][controller].set_focus()
    def drag(self,window_name,controller,dx,dy,sx,sy):
        self.app[window_name][controller].drag_mouse_input(dst=(dx,dy),src=(sx,sy),button='left',pressed='',absolute=True)
    def Sendk(self,key_name,times):
        SendKeys.SendKeys('{%s %d}'%(key_name,times))
    def _wait(self, window_name, wait_for, time, interval):
        try:
            self.app[window_name].wait(wait_for, timeout=time, retry_interval=interval)
        except:
#             print "current is"+sys._getframe().f_back.f_code.co_name
            exit()
        
    def _wait_child(self, window_name, controller, wait_for, time, interval):
        self.app[window_name][controller].wait(wait_for, timeout=time, retry_interval=interval)
        
    def _wait_not(self,window_name,wait_for, time, interval):
        self.app[window_name].wait_not(wait_for, timeout=time, retry_interval=interval)
        
    def _wait_not_child(self, window_name, controller, wait_for, time, interval):
        self.app[window_name][controller].wait_not(wait_for, timeout=time, retry_interval=interval)
        
    def texts(self,window_name,controller):
        value = self.app[window_name][controller].texts()
        return(value[0])
if __name__ ==  "__main__":
    pass

    
    
    
    
        