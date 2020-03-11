#!/bin/bash
#set -e

#----------------------------------------------------------------------------------------
#功能功能：
#读取性能测试跑分结果文件，并将其写入数据库
#----------------------------------------------------------------------------------------

if [ $# -ne 2 ];then
 echo "usage: $0 TestType Platform" 
 exit 1
fi

#----------------------------------------------------------------------------------------
TestType="$1"
Platform="$2"
#----------------------------------------------------------------------------------------
ResultPath='/data'
ResultFile="TestResults_new.ini"
srcIniPath="${ResultPath}/${TestType}/${Platform}/"
destPath="${ResultPath}/${TestType}/${Platform}"
destFile="${destPath}/${ResultFile}"
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
okfile='ok_file.txt'
errfile='err_file.txt'
#----------------------------------------------------------------------------------------


#:> ${okfile}
#:> ${errfile}

echo "[$TestType],[$Platform],writting to database Begin..."

echo "***************************************************"

start_time=`date +%s`              #定义脚本运行的开始时间

sh merge_Excel_Case_all.sh $TestType $Platform "${case_name}"

echo "***************************************************"
stop_time=`date +%s`  #定义脚本运行的结束时间

echo "Exec Time:`expr $stop_time - $start_time`s"

echo "**********************************************"
echo "[$TestType],[$Platform],Merging the each Result Excel file finished."
