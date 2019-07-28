#!/usr/bin/python
#_*_ coding:utf-8 _*_


import subprocess
import json

def get_info():
    cmd="ssh -p 29418 10.80.30.10 gerrit query merged --format JSON --current-patch-set | grep -v runTimeMilliseconds >project.txt"
    process=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    process.wait()

def head():
    head_str="""
<html>
<body>
<table border="1" aligin="center" width="600" height="600" cellspacing="1">
    <tr>
        <th bgcolor="EEEE00">number</th>
        <th bgcolor="EEEE00" width="200">subject</th>
        <th bgcolor="EEEE00">project</th>
        <th bgcolor="EEEE00">branch</th>
        <th bgcolor="EEEE00">url</th>
    </tr>
"""
    return head_str

def foot():
    foot_str="""
    </table>
</body>
</html>
"""

def write_html():
    heads=head()
    foots=foot()

    #写入头部
    with open("test.html","w") as f1:
        f1.write(heads)
    with open("project.txt") as f2:
        for line in f2.readlines():
            content=json.loads(line)
            number=content.get("number").encode("gbk")
            subject=content.get("subject").encode("gbk")
            project=content.get("project").encode("gbk")
            branch=content.get("branch").encode("gbk")
            url=content.get("url").encode("gbk")

            with open("test.html","a+") as f3:
                str1="""
            <tr>
                <td>%s</td>
                <td width="160">%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
            </tr>
            """ % (number,subject,project,branch,url)
        
                f3.write(str1)
    #with open("test.html","a+") as f4:
    #    f4.write(foots)

if __name__=="__main__":
    write_html()
