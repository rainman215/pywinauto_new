#! /usr/bin/env python
#coding=GB18030
import re,time,os,sys
from pywinauto import application
app=application.Application(backend='uia')

#��application.py��ӡ�Ŀؼ����Ե���./identify�ļ���
def setenv():
    for line in sys.path:                           #����ϵͳ���û���·��
        t='site-packages$'                              
        if re.findall(t, line):                         #����·���к�site-packages��·��
            old=line+'\\pywinauto\\application.py'
            new=line+'\\pywinauto\\application.bak'
    with open(old,'r') as f:                            #��\\pywinauto\\application.py��д
        patt='def\ print_control_identifiers'           
        f2=open(new,'w')
        for line in f:
            if re.findall(patt, line):                  #���ݹؼ���patt���в��һ�ò����е�����
                line=r"    def print_control_identifiers(self, depth=None, filename='./identif'):"  #�����ҵ������滻Ϊ������line
                f2.write(line)                                      #���滻������lineд�����ļ�
                f2.write('\n')                                      #����
            else:
                f2.write(line)                                      #����ƥ����м���д��new
        f2.close()
    os.remove(old)                                                  #ɾ�����ļ�
    os.rename(new, old)                                             #��new�ļ���application.bak����Ϊold�ļ���application.py
class attr_Control(object):
    def __init__(self,con_Name):
        self.con_Name=con_Name      
        
#��ӡָ�����������пؼ�����
    @staticmethod      
    def get_Allattr(window_name):
        time.sleep(1)
        app.connect(title = window_name)
        app[window_name].print_control_identifiers()

#����������ʽ���ָ���ؼ�����
    def get_attrName(self):
        path='./identif'
        _file=open(path)
        flag=0
        for line in _file:
#             t="'"+self.con_Name+"'"
            Name="\'%s\D?\d*\'"%self.con_Name
            if re.findall(Name, line):                   #����������ʽ��identif��ƥ����Һ����������ƵĶ���
                flag=1                                  #��ƥ�䵽��������flag=1
#                 print line
                continue
            if flag == 1:
                break
        _file.close()
        if flag == 0:                                   #flag=0��ʾû�и�Ԫ��
            print('No this Element')
            return (0)
        else:
            attr_list=line.split(',')               #�Ѷ��Ž��зָ�
            pattern=r'\'\w+\d+\''                   
            attrs=[]
            for i in attr_list:
                s=re.findall(pattern,i)                   #����������ʽ��ƥ������м���ƥ��ؼ��ı�ʶ����
                if s:                                       
                    attrs.append(s)                 #�����Ҵ�����׷�ӵ�attrs
            if attrs:
                attr_Name=attrs[0][0].replace('\'','').strip(' ')   #��attrs��һ���ַ���'\'�滻Ϊ' '��ȥ��
                return attr_Name                            #����ƥ��ı�ʶ����
            else:
                print('No this Element')
                return (0)
if __name__=='__main__':
    setenv()
    con_Name=raw_input("Please input Search Name:")
    con_list=con_Name.split(',')
    for Name in con_list:
        window_name=r'QuiKLab V3.0'
        print "Seraching all attr..."
        attr_Control.get_Allattr(window_name)
        print Name
        attr=attr_Control(Name)
        print attr.get_attrName()
        try:
            app[window_name][u'�������'].wait('ready', 10, 2)
            print "1"
        except:
            print "2"
#         app[window_name][attr.get_attrName()].click_input()

    