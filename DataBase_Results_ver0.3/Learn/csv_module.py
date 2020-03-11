#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unicodecsv as ucsv
"""
Created on Tue Jul 10 22:06:43 2018
@author: User
"""
import io
 
import csv
 
datas = [['俄罗斯', '1707'],
         ['加拿大', 997],
         ['中国', 960],
        ['美国', '936']]
 
#with io.open('country.csv', 'w', newline='') as csvfile:
#    writer  = ucsv.writer(csvfile,encoding='utf8')
#    for row in datas:
#        writer.writerow(row)


with open('test.csv', 'wb') as f:
    w = ucsv.writer(f, encoding = 'utf8')
    w.writerows(datas)


#打开一个csv文件，并赋予读的权限
csvHand=open('test.csv',"r")
#调用csv的reader函数读取csv文件
readcsv=ucsv.reader(csvHand,encoding = 'utf8')
#创建一个list用来保存csv中的内容
buffer=[]

#把csv中内容存入list 中
for row in readcsv:
  buffer.append(row)

print(buffer)
