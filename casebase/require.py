#! /usr/bin/env python
#coding=GB18030
from pywinauto import application
import time
import os
import win32com.client
def check_exist(pro_name):
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_process where Name="%s"'%pro_name)
    if len(processCodeCov) > 0:
        return 1
    else:
        print "%s is not exist"%pro_name
        return 0

app=application.Application(backend='uia')
window_name = r'QuiKLab V3.0'
app.connect(title = window_name)
try:
    app[window_name][u'测试需求'].wait('active',30,2) 

except:
    app[window_name][u'TreeItem0'].click_input()
for i in range(10):
#     print i
    app[window_name][u'测试需求'].click_input()
    app[window_name][u'导入模板'].click_input()
    app[window_name]['Edit25'].type_keys('1234.docx')
    app[window_name][u'打开(O)'].click_input()
#     time.sleep(5)
    while check_exist('WINWORD.exe'):
        print '1111'
        time.sleep(2)
    time.sleep(2)
    app[window_name][u'编辑模板'].wait('enabled',10,2)
    app[window_name][u'编辑模板'].click_input()
    time.sleep(10)
#     print check_exist('WINWORD.exe')
#     if check_exist('WINWORD.exe') == 0:
#             print '111'
    app[window_name][u'提示信息'].wait('ready',30,2)
    app[window_name][u'是'].click_input()
    app[window_name][u'编辑模板'].wait('enabled',10,2)
    app[window_name][u'编辑模板'].click_input()
    os.system('taskkill /IM WINWORD.exe /F')
    time.sleep(10)
