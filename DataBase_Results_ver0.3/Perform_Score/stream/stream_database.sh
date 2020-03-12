#!/bin/bash

if [ $# -ne 3 ];then
 echo "usage: $0 TestType Platform TestCase" 
 exit 1
fi
#----------------------------------------------------------------------------------------
TestType="$1"
Platform="$2"
TestCase="$3"


#stream 单核测试 写csv文件
sh stream_1core_database.sh $TestType $Platform "stream_1core"

#stream 多核测试 写csv文件
sh stream_ncore_database.sh $TestType $Platform "stream_ncore"
