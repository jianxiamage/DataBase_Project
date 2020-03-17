#!/bin/bash

if [ $# -ne 3 ];then
 echo "usage: $0 TestType Platform TestCase" 
 exit 1
fi
#----------------------------------------------------------------------------------------
TestType="$1"
Platform="$2"
TestCase="$3"


#spec2006 单核浮点型测试 备份数据表
sh backup_spec2006_1core_CFP_database.sh $TestType $Platform "spec2006_1core_CFP"

#spec2006 单核整型测试 备份数据表
sh backup_spec2006_1core_CINT_database.sh $TestType $Platform "spec2006_1core_CINT"
