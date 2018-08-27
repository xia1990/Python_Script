#!/usr/bin/python
#_*_ coding:utf-8 _*_
#将Default.xml中没有revision的行添加上revision属性


from xml.etree import ElementTree as ET

str_xml=open("default.xml","r").read()
root=ET.XML(str_xml)


for child in root.iter("default"):
	#得到默认的分支名称
	default_revision=child.attrib['revision']
	for project in root.iter("project"):
		#得到project行中所有属性
		line=project.attrib
		#如果此属性中包含revision,就使用当前的值
		if "revision" in line:
			project.attrib['revision']=project.attrib['revision']
		else:	
			#如果没有revision,则添加为默认值
			project.attrib['revision']=default_revision
			

#保存文件
tree=ET.ElementTree(root)
tree.write("default2.xml",encoding="utf-8")


