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

#防止自动将ini文件中的键名转换成小写
class myconf(ConfigParser.ConfigParser):
    def __init__(self,defaults=None):
        ConfigParser.ConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr


def read_iniHead(outputFile):

    f = open(outputFile,"w")
    f.write('Tag,node_num,core,test_option,ref_data\n')
    f.close

def read_ini(inputFile,outputFile,node_num,Tag):

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
            strLine = Tag + ',' + str(node_num) + ',' + section + ',' + option + ',' + value
            print(strLine)
            f.write(strLine)
            f.write('\n')
            j = j + 1

        i = i + 1
    f.close

    return 0


if __name__=='__main__':

  try:

      #输入参数
      test_type = sys.argv[1]
      test_platform = sys.argv[2]
      test_case = sys.argv[3]
      test_Tag = sys.argv[4]

      #拼接目标文件名
      caseDir='UnixBench' #区分单核和多核
      ResultIniPath = ResultPath + str(test_type) + '/' + str(test_platform) + '/' + str(detailDir) + '/' + str(caseDir) + '/' + str(PointsPath)
      iniFilePre = test_case + '_'
      iniFileEnd = '.ini'

      MaxCount=3  #并发节点最大为3个
      iniFileName = ResultIniPath + '/' + iniFilePre + '1' + iniFileEnd
      csvFileName = ResultIniPath + '/' + test_case +'.csv'

      result_code = read_iniHead(csvFileName)

      #遍历所有并发节点ini文件(正常情况下为:3个)
      for i in range(1,MaxCount+1):
        #iniFileName = iniFilePre + str(i) + iniFileEnd
        iniFileName = ResultIniPath + '/' + iniFilePre + str(i) + iniFileEnd
        print(iniFileName)
        print('-----------------------')
        result_code = read_ini(iniFileName,csvFileName,str(i),test_Tag)

  except Exception as E:
      #print('str(Exception):', str(Exception))
      print('str(e):', str(E))
      #print('repr(e):', repr(E))
      #print('traceback.print_exc(): ', traceback.print_exc())

