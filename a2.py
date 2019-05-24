#!/usr/bin/python
#_*_ coding:utf-8 _*_

import shelve
import datetime

inf1o={'name':'bigberg','age':22}
name=['Apoll','Zous','Luna']
t=datetime.datetime.now()

f1= shelve.open('shelve.txt')
f1['name']=name
f1['inf1o']=inf1o
f1['time']=t
f1.close()

f2=shelve.open('shelve.txt')
n=f2.get('name')
i=f2.get('info')
now=f2.get('time')

print(n,i,now)


