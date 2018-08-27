#!/usr/bin/python
#_*_ coding:utf-8 _*_
#将Default.xml中没有path的行添加上path属性


from xml.etree import ElementTree as ET

str_xml=open("default.xml","r").read()
root=ET.XML(str_xml)


for node in root.iter("project"):
	#node.attrib['name']得到name属性的值，然后添加PATH属性
	node.set('path',node.attrib['name'])

#保存文件
tree=ET.ElementTree(root)
tree.write("default2.xml",encoding="utf-8")

