#coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8') 

s = u'中文'
f = open("test.txt","w")
f.write(s)
f.close()
