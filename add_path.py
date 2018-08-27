#!/usr/bin/python
#_*_ coding:utf-8 _*_
#将Default.xml中没有path的行添加上path属性


from xml.etree import ElementTree as ET

str_xml=open("default.xml","r").read()
root=ET.XML(str_xml)


for project in root.findall("project"):
	path=project.get("path")
	if path is None:
		print "没有PATH属性,请进行添加"
		project.attrib['path']=project.attrib['name']
	else:
		print "有PATH属性值,直接输出"
		project.attrib['path']=project.attrib['path']
			

#保存文件
tree=ET.ElementTree(root)
tree.write("default2.xml",encoding="utf-8")

