#! /usr/bin/env python
#coding=utf-8

from lxml import etree


class lxmlReaderModify(object):
    def __init__(self,strlXml):
        
        if type(strlXml) == str:
            self.xml = etree.XML(strlXml)     #将string转化为python对象
            
        else:
            self.xml = etree.parse(strlXml)     #导入并解析xml文件
    
    #获取标签对之间的文本及标签的属性的值   
    def getTabNodeValue(self,xpathName):
        
        value = self.xml.xpath(xpathName)   
        return value

    
    #修改标签对之间的文本
    def modifyNodeText(self,xpathDir,value,fileUrl):
        node = self.xml.find(xpathDir)     #定位元素        
        node.text = value                  #修改节点的文本内容
        self.xml.write(open(fileUrl,"w"),pretty_print = True)   #将修改之后的内容写入文件中

     
    #修改标签属性的值   
    def modifyTabQualityValue(self,xpathDir,quality,value,fileUrl):
        node = self.xml.find(xpathDir)    #定位元素
        node.set(quality,value)           #修改节点属性的值
        self.xml.write(open(fileUrl,"w"),pretty_print = True)   #将修改之后的内容写入文件中
        
if __name__=='__main__':        
    str1 = '''<?xml version="1.0" encoding="GBK"?><note><to>World</to><from>Linvo</from><heading>Hi</heading>
    <body i="TCP我们" ID="6342" classname="InterfaceTcpClient" 
    config="&lt;Config&gt;&#10;    &lt;clientPort&gt;0&lt;/clientPort&gt;&#10;    &lt;ServerIP&gt;192.168.1.5&lt;/ServerIP&gt;&#10;    
    &lt;ServerPort&gt;6060&lt;/ServerPort&gt;&#10;&lt;/Config&gt;" filterConfig=""/><Interface name= "第n个端口对应第16路" ID="6342" classname="InterfaceTcpClient" 
    config="&lt;Config&gt;&#10;    &lt;clientPort&gt;0&lt;/clientPort&gt;&#10;    &lt;ServerIP&gt;192.168.1.5&lt;/ServerIP&gt;&#10;    
    &lt;ServerPort&gt;6060&lt;/ServerPort&gt;&#10;&lt;/Config&gt;" filterConfig=""/></note>'''
    str1 = str1.replace('GBK','utf-8')     
    dom = lxmlReaderModify(str1)
    print dom.getTabNodeValue("//body/@i")         #获取标签中属性的值
    print dom.getTabNodeValue("//to/text()")       #获取标签对中间的文本
     
    file = open(r"C:\Users\KLJS044\QuiKLab3\config.xml","r")
    print type(file)
    dom = lxmlReaderModify(file)
    fileUrl = r"C:\Users\KLJS044\QuiKLab3\config.xml"
    dom.modifyNodeText("//config/targetMode",'7',fileUrl)
    dom.modifyTabQualityValue("//config/useDatabase","useDatabase","11",fileUrl)
    file.close()