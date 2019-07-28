#!/usr/bin/python
#_*_ coding:utf-8 _*_


import xlwt
import subprocess
import time
import json


def setStyle(name,height,color,bold=False):
    style = xlwt.XFStyle()
    font=xlwt.Font()
    #字体类型
    font.name=name
    #字体颜色
    font.colour_index=color
    #字体大小
    font.height=height
    #定义格式
    style.font=font
    #设置背景颜色
    pattern=xlwt.Pattern()
    pattern.pattern=xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour=3
    #定义格式
    style.pattern=pattern
    #表格边框
    borders=xlwt.Borders()
    borders.left=xlwt.Borders.THIN
    borders.right=xlwt.Borders.THIN
    borders.top=xlwt.Borders.THIN
    borders.bottom=xlwt.Borders.THIN
    #定义格式
    style.borders=borders
    return style

def get_result():
    cmd="ssh -p 29418 10.80.30.10 gerrit query branch:Stable_Factory32_BRH after:'2019-07-19' project:^LNX_LA_SDM450_S102X_PSW/.*  status:merged  | grep 'subject' > message.txt"
    process=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    process.wait()

def write_excel():
    f=xlwt.Workbook(encoding='utf-8')
    sheet1=f.add_sheet(u"修改点",cell_overwrite_ok=True)
    label_row=[u'序号',u'BUG号',u'调试单元',u'软件确认状态',u'备注']
    for i in range(len(label_row)):
        #参数1：字体名称
        #参数2：字体大小
        #参数3：字体颜色
        sheet1.write(0,i,label_row[i],setStyle("Arial",220,0,False))
    with open("message.txt") as af:
        contents=af.readlines()
        type(contents)
        for j in range(len(contents)):
            sheet1.write(j+1,0,j)
            sheet1.write(j+1,2,contents[j])
            sheet1.write(j+1,3,"OK")
            sheet1.write(j+1,4,time.strftime("%Y%m%d"))
    f.save("修改点.xls")

if __name__=="__main__":
    get_result()
    write_excel()

