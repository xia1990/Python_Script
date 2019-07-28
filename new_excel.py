#!/usr/bin/python
#_*_ coding:utf-8 _*_


import xlwt
import subprocess
import json


def setStyle(name,height,color,bold=False):
    style=xlwt.XFStyle()
    font=xlwt.Font()
    font.name=name
    font.colour_index=color
    font.height=height
    style.font=font
    #设置边框
    borders=xlwt.Borders()
    borders.left=color
    borders.left=xlwt.Borders.THIN
    borders.right=xlwt.Borders.THIN
    borders.top=xlwt.Borders.THIN
    borders.bottom=xlwt.Borders.THIN
    style.borders=borders
    #设置背景
    pattern=xlwt.Pattern()
    pattern.pattern=xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour=3
    style.pattern=pattern
    return style

def get_project_info():
    cmd="ssh -p 29418 10.80.30.10 gerrit query merged --format JSON --current-patch-set | grep -v runTimeMilliseconds >project.txt"
    process=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    process.wait()


def write_excel():
    f=xlwt.Workbook(encoding="utf-8")
    sheet1=f.add_sheet(u'sheet1',cell_overwrite_ok=False)
    row_list=["number","subject","project","branch","url"]
    for i in range(len(row_list)):
        sheet1.write(0,i,row_list[i],setStyle("Times New Roman",400,0,False))

    index=0
    with open("project.txt") as f1:
        for m in f1:
            number=json.loads(m)["number"]
            subject=json.loads(m)["subject"]
            project=json.loads(m)["project"]
            branch=json.loads(m)["branch"]
            url=json.loads(m)["url"]
            index=index+1
            print(index)
            sheet1.write(index,0,number)
            sheet1.write(index,1,subject)
            sheet1.write(index,2,project)
            sheet1.write(index,3,branch)
            sheet1.write(index,4,url)


    f.save("new_excel.xls")

if __name__=="__main__":
    get_project_info()
    write_excel()
