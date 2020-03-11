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


def read_ini(inputFile,outputFile):

    config = myconf()
    config.readfp(open(inputFile))

    i = 0
    j = 1

    f = open(outputFile,"w")
    f.write('case_name,node_num,value\n')

    dictionary = {}
    for section in config.sections():
        dictionary[section] = {}
        print('---------------------------------')
        print section
        print('---------------------------------')

        for option in config.options(section):
            dictionary[section][option] = config.get(section, option)
            value = dictionary[section][option]
            option_num=option.lstrip('node_')
            #print 'option_num:%s,value:%s' %(option_num,dictionary[section][option])
            print 'section:%s,option_num:%s,value:%s' %(section,option_num,value)
            strLine = section + ',' + option_num + ',' + value
            print(strLine)
            f.write(strLine)
            f.write('\n')
            j = j + 1

        i = i + 1
    f.close

    return 0


if __name__=='__main__':

  try:

      iniFileName='TestResults.ini'
      csvFileName='TestResults.csv'
      result_code = read_ini(iniFileName,csvFileName)
      retCode = result_code
      print('---------------------------------')
      print 'retCode is:%s' %(retCode)
      print('---------------------------------')

  except Exception as E:
      #print('str(Exception):', str(Exception))
      print('str(e):', str(E))
      #print('repr(e):', repr(E))
      #print('traceback.print_exc(): ', traceback.print_exc())

