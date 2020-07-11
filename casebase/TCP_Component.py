#! /usr/bin/env python
#coding=GB18030
from pywinauto import mouse as ms
import auto_lib as pywin 
import locFun as location
import time
app=pywin.Pywin()

#��ӿͻ��˽ӿ�
@location._getName
def add_TCP_Client_Interface(window_name):
    app.connect(window_name)
    app._wait_child(window_name, u'��ӽӿ�', 'ready', 10, 2)
    app.click(window_name, 'ComboBox1')
    app.Sendk('DOWN', 1)
    app.Sendk('ENTER', 1)
#���IP
    app.click(window_name, 'Edit9')
    app.Sendk('RIGHT', 1)
    app.input(window_name, 'Edit9', '192')
    app.Sendk('.', 1)
    app.input(window_name, 'Edit10', '168')
    app.Sendk('.', 1)
    app.input(window_name, 'Edit11', '1')
    app.Sendk('.', 1)
    app.input(window_name, 'Edit12', '5')
#���ö˿�
    app.click(window_name, 'Edit13')
    app.Sendk('BACKSPACE', 1)
    app.input(window_name, 'Edit13', '6060')
    app.click(window_name, u'ȷ��')#ȷ��
    app._wait_not_child(window_name, u'��ӽӿ�', 'ready', 10, 2)
    
#��ӷ���˽ӿ�
@location._getName
def add_TCP_Service_Interface(window_name):
    ms.right_click(coords=(923,510))
    app.Sendk('DOWN', 2)
    app.Sendk('ENTER', 1)
    app._wait_child(window_name, u'��ӽӿ�', 'ready', 10, 2)
    app.click(window_name, 'ComboBox1')
    app.Sendk('DOWN', 2)
    app.Sendk('ENTER', 1)
    app.click(window_name, u'ȷ��')#ȷ��
    app._wait_not_child(window_name, u'��ӽӿ�', 'ready', 10, 2)
    
#����ź�
@location._getName
def add_TCP_Signal(window_name):
    ms.press(button='left', coords=(902, 456))
    ms.move(coords=(940, 456))
    ms.release(button='left', coords=(940, 456))
    app._wait_child(window_name, u'�źű༭�Ի���', 'ready', 10, 2)
    app.click(window_name, 'ComboBox5')
    app.input(window_name, 'ComboBox5', 'i_block')#������ݽṹ
    app.Sendk('ENTER', 1)
    app.click(window_name, u'ȷ��')#ȷ��
    app._wait_not_child(window_name, u'�źű༭�Ի���', 'ready', 10, 2)

#�½���������
@location._getName
def add_TCP_Case(window_name):
    app.click(window_name, u'��������')
    app._wait_child(window_name, u'����������', 'ready', 10, 2)
    app.right_click(window_name, 'TreeView2')
    app.Sendk('DOWN', 2)
    app.Sendk('ENTER',1)
    app._wait_child(window_name, u'�½���������', 'ready', 10, 2)
    app.click(window_name, u'ȷ��')
#     app._wait_not_child(window_name, u'�½���������', 'ready', 10, 2)
    app._wait_child(window_name, u'��������', 'ready', 10, 2)
    app.right_click(window_name,u'��������') #��������root
    time.sleep(1)
    app.Sendk('DOWN',4)
    app.Sendk('ENTER',1)
    app._wait_child(window_name, u'�½���������', 'ready', 10, 2)
    app.Sendk('TAB',2)
    app.input(window_name, 'Edit1', 'content2')#����������
    app.click(window_name,u'ȷ��') #ȷ��
    app.click(window_name,u'��������')
    app.Sendk('RIGHT',1)
    app.Sendk('DOWN',1)
    app._wait_child(window_name, 'content2', 'ready', 10, 2)
    

#����ź�
    app.click(window_name, u'������������')
    app.click(window_name, 'Button16')
    app._wait_child(window_name, u'ѡ���źŶԻ���', 'ready', 10, 2)
    ms.click(coords=(610,470))#��ѡ�ź�
    app.click(window_name, 'Button14')#ȷ��
    app._wait_child(window_name, u'signal', 'ready', 10, 2)


#���������༭    
    app.click(window_name, u'���������༭')
    app.right_click(window_name, 'TreeItem16')
    app.Sendk('UP', 1)
    app.Sendk('ENTER', 1)#��������
    app._wait_child(window_name, u'ɾ��', 'ready', 10, 2)
    ms.press(button='left',coords=(600,229))
    ms.move(coords=(661, 646))
    ms.release(button='left', coords=(661, 646))
    app.click(window_name, u'ȷ��')
    app._wait_child(window_name, u'����[signal]', 'ready', 10, 2)

@location._getName
def run_case(window_name):
#     app.connect(window_name)
    app.click(window_name,u'��ʼ')
    app._wait_child(window_name, u'��ʼ�²���', 'ready', 10, 2)
    app.click(window_name, 'content2')
    app.click(window_name, 'ComBox4')
    app.Sendk('UP', 2)
    app.Sendk('ENTER', 1)    
    app.click(window_name, u'��ʼ')
    app.click(window_name, u'ȷ��')
#     app.click(window_name, u'����')
#     time.sleep(1)
#     app._wait_child(window_name, u'����', 'ready', 10, 2)
    time.sleep(5)
    app._wait_not_child(window_name, u'����', 'ready', 10, 2)
    app.click(window_name,u'����')
    time.sleep(2)
    app.click(window_name, u'ͣ  ֹ')
if __name__=='__main__':
    app=pywin.Pywin()
    window_name =u'QuiKLab V3.0'
    time.sleep(2)
    app.connect(window_name)
#     add_TCP_Client_Interface(window_name)
#     add_TCP_Service_Interface(window_name)
#     add_TCP_Signal(window_name)
    add_TCP_Case(window_name)