#!/bin/bash

if [ $# -ne 3 ];then
 echo "usage: $0 TestType Platform TestCase" 
 exit 1
fi
#----------------------------------------------------------------------------------------
TestType="$1"
Platform="$2"
TestCase="$3"


#spec2000 单核浮点型测试 写入数据库
sh spec2000-ncore_CFP_database.sh $TestType $Platform $TestCase

#spec2000 单核整型测试 写入数据库
sh spec2000-ncore_CINT_database.sh $TestType $Platform $TestCase
