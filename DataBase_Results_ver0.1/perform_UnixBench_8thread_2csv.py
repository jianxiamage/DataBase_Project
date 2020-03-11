#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys  #引入模块
import os
import traceback
import ConfigParser

reload(sys)
sys.setdefaultencoding('utf-8') 

#防止自动将ini文件中的键名转换成小写
class myconf(ConfigParser.ConfigParser):
    def __init__(self,defaults=None):
        ConfigParser.ConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr


def read_iniHead(outputFile):

    f = open(outputFile,"w")
    f.write('node_num,score,test_option,ref_data\n')
    f.close

def read_ini(inputFile,outputFile,node_num):

    config = myconf()
    config.readfp(open(inputFile))

    i = 0
    j = 1

    f = open(outputFile,"a")
    dictionary = {}
    for section in config.sections():
        dictionary[section] = {}
        print('---------------------------------')
        print section
        print('---------------------------------')

        for option in config.options(section):
            dictionary[section][option] = config.get(section, option)
            value = dictionary[section][option]
            #print 'value:%s,option:%s,section:%s' %(value,option,section)
            print 'section:%s,option:%s,value:%s' %(section,option,value)
            #strLine = value + ',' + option + ',' + section
            strLine = str(node_num) + ',' + section + ',' + option + ',' + value
            print(strLine)
            f.write(strLine)
            f.write('\n')
            j = j + 1

        i = i + 1
    f.close

    return 0


if __name__=='__main__':

  try:

      MaxCount=3  #并发节点最大为3个
      #iniFileName='UnixBench_8thread_1.ini'
      csvFileName='UnixBench_8thread.csv'

      result_code = read_iniHead(csvFileName)

      iniFilePre = 'UnixBench_8thread_'
      iniFileEnd = '.ini'

      #遍历所有并发节点ini文件(正常情况下为:3个)
      for i in range(1,MaxCount+1):
        iniFileName = iniFilePre + str(i) + iniFileEnd
        print(iniFileName)
        print('-----------------------')
        result_code = read_ini(iniFileName,csvFileName,str(i))

      #单个文件写入逻辑
      #result_code = read_ini(iniFileName,csvFileName)
      #retCode = result_code
      #print('---------------------------------')
      #print 'retCode is:%s' %(retCode)
      #print('---------------------------------')

  except Exception as E:
      #print('str(Exception):', str(Exception))
      print('str(e):', str(E))
      #print('repr(e):', repr(E))
      #print('traceback.print_exc(): ', traceback.print_exc())

