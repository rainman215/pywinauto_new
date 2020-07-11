#! /usr/bin/env python
#coding=GB18030
import re,time,os,sys
from pywinauto import application
app=application.Application(backend='uia')

#将application.py打印的控件属性导入./identify文件中
def setenv():
    for line in sys.path:                           #遍历系统配置环境路径
        t='site-packages$'                              
        if re.findall(t, line):                         #查找路径中含site-packages的路径
            old=line+'\\pywinauto\\application.py'
            new=line+'\\pywinauto\\application.bak'
    with open(old,'r') as f:                            #对\\pywinauto\\application.py读写
        patt='def\ print_control_identifiers'           
        f2=open(new,'w')
        for line in f:
            if re.findall(patt, line):                  #根据关键字patt逐行查找获得查找行的内容
                line=r"    def print_control_identifiers(self, depth=None, filename='./identif'):"  #将查找到的行替换为新内容line
                f2.write(line)                                      #将替换的内容line写入新文件
                f2.write('\n')                                      #换行
            else:
                f2.write(line)                                      #将不匹配的行继续写入new
        f2.close()
    os.remove(old)                                                  #删除旧文件
    os.rename(new, old)                                             #将new文件名application.bak更换为old文件名application.py
class attr_Control(object):
    def __init__(self,con_Name):
        self.con_Name=con_Name      
        
#打印指定窗口下所有控件属性
    @staticmethod      
    def get_Allattr(window_name):
        time.sleep(1)
        app.connect(title = window_name)
        app[window_name].print_control_identifiers()

#根据正则表达式获得指定控件属性
    def get_attrName(self):
        path='./identif'
        _file=open(path)
        flag=0
        for line in _file:
#             t="'"+self.con_Name+"'"
            Name="\'%s\D?\d*\'"%self.con_Name
            if re.findall(Name, line):                   #根据正则表达式从identif内匹配查找含有输入名称的段落
                flag=1                                  #若匹配到查找内容flag=1
#                 print line
                continue
            if flag == 1:
                break
        _file.close()
        if flag == 0:                                   #flag=0提示没有该元素
            print('No this Element')
            return (0)
        else:
            attr_list=line.split(',')               #已逗号进行分割
            pattern=r'\'\w+\d+\''                   
            attrs=[]
            for i in attr_list:
                s=re.findall(pattern,i)                   #根据正则表达式从匹配段落中继续匹配控件的标识名称
                if s:                                       
                    attrs.append(s)                 #若查找存在则追加到attrs
            if attrs:
                attr_Name=attrs[0][0].replace('\'','').strip(' ')   #将attrs第一个字符串'\'替换为' '并去除
                return attr_Name                            #返回匹配的标识名称
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
            app[window_name][u'需求管理'].wait('ready', 10, 2)
            print "1"
        except:
            print "2"
#         app[window_name][attr.get_attrName()].click_input()

    