#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys  #引入模块
import os
import traceback
import ConfigParser

reload(sys)
sys.setdefaultencoding('utf-8') 

#------------------------------------------
ResultPath='/data/'
detailDir='Detail'
PointsPath='Points_Files'
#------------------------------------------
section = 'EXT3 File System'
#------------------------------------------

#防止自动将ini文件中的键名转换成小写
class myconf(ConfigParser.ConfigParser):
    def __init__(self,defaults=None):
        ConfigParser.ConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr

#将ini文件中的section内容写入csv文件开头，用以标明各个字段名称
#注意的是写入section行到csv时是覆盖模式"w")
def read_iniHead(inputFile,outputFile):

    config = myconf()
    config.readfp(open(inputFile))

    f = open(outputFile,"w")

    options = config.options(section)
    optionStr = ','.join(options)
    print(optionStr)
    f.write('Tag,node_num,' + optionStr + '\n')

#将各个字段的值写入csv文件
def read_ini(inputFile,outputFile,num,Tag):

    config = myconf()
    config.readfp(open(inputFile))

    f = open(outputFile,"a")

    j=1
    dicts = {}
    #section = 'EXT3 File System'
    for option in config.options(section):
        dicts[option] = config.get(section, option)
        value = dicts[option]
        #print 'section:%s,option:%s,value:%s' %(section,option,value)
        print(value)
        j = j + 1
    
    print('===============================================')
    values = dicts.values()
    values_Str = ','.join(values)
    print(values_Str)
    f.write(Tag + ',' + num + ',' + values_Str+'\n')

    print('===============================================')

    return 0

if __name__=='__main__':

  try:

      #输入参数
      test_type = sys.argv[1]
      test_platform = sys.argv[2]
      test_case = sys.argv[3]
      test_Tag = sys.argv[4]

      #拼接目标文件名
      ResultIniPath = ResultPath + str(test_type) + '/' + str(test_platform) + '/' + str(detailDir) + '/' + str(test_case) + '/' + str(PointsPath)
      iniFilePre = test_case + '_'
      iniFileEnd = '.ini'

      MaxCount=3  #并发节点最大为3个
      #iniFileName='iozone_1.ini'
      iniFileName = ResultIniPath + '/' + iniFilePre + '1' + iniFileEnd
      #csvFileName='iozone.csv'
      csvFileName = ResultIniPath + '/' + test_case +'.csv'

      result_code = read_iniHead(iniFileName,csvFileName)

      #遍历所有并发节点ini文件(正常情况下为:3个)
      for i in range(1,MaxCount+1):
        #iniFileName = iniFilePre + str(i) + iniFileEnd
        iniFileName = ResultIniPath + '/' + iniFilePre + str(i) + iniFileEnd
        print(iniFileName)
        print('-----------------------')
        result_code = read_ini(iniFileName,csvFileName,str(i),test_Tag)
      
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
      sys.exit(1)
