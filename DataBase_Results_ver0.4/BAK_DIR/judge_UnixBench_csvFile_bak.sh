#!/bin/bash

#----------------------------------------------------------------------------------------

if [ $# -ne 2 ];then
 echo "usage: $0 TestType Platform" 
 exit 1
fi

#----------------------------------------------------------------------------------------
TestType="$1"
Platform="$2"
TestCase="UnixBench"
#TestMode="1thread"
#----------------------------------------------------------------------------------------
resultsPath='/data'
PointsPath='Points_Files'
Node_count=0
#----------------------------------------------------------------------------------------
#测试结果目录(筛选内容后)地址
detailDir="Detail"
destResultPath="${resultsPath}/${TestType}/${Platform}/${detailDir}/${TestCase}/${PointsPath}"


if [ ! -s $destResultPath ];
then
  echo Error! [$destResultPath] not existed!Please check it!
  exit 1
fi

#if [ ! -s $destIniPath ];
#then
#  echo Error! [$destIniPath] not existed!Please check it!
#  exit 1
#fi

echo -------------------------------------------------------------

ls $destResultPath/ | grep "${TestCase}" |grep "ini"

if [ $? -ne 0 ];
then
  echo "No ini files for $TestCase exists!Please check it!"
  exit 1
fi

echo -------------------------------------------------------------


ls $destResultPath/ | grep "${TestCase}" |grep "ini" |grep "1thread"

if [ $? -eq 0 ];
then
  echo "Begin to make csv files for UnixBench 1 thread..."
  sh UnixBench_1thread_csvFile_get.sh $TestType $Platform $TestCase
fi

ls $destResultPath/ | grep "${TestCase}" |grep "ini" |grep "2thread"

if [ $? -eq 0 ];
then
  echo "Begin to make csv files for UnixBench 2 threads..."
  sh UnixBench_2thread_csvFile_get.sh $TestType $Platform $TestCase
fi

ls $destResultPath/ | grep "${TestCase}" |grep "ini" |grep "4thread"

if [ $? -eq 0 ];
then
  echo "Begin to make csv files for UnixBench 4 threads..."
  sh UnixBench_4thread_csvFile_get.sh $TestType $Platform $TestCase
fi

ls $destResultPath/ | grep "${TestCase}" |grep "ini" |grep "8thread"

if [ $? -eq 0 ];
then
  echo "Begin to make csv files for UnixBench 8 threads..."
  sh UnixBench_8thread_csvFile_get.sh $TestType $Platform $TestCase
fi


ls $destResultPath/ | grep "${TestCase}" |grep "ini" |grep "16thread"

if [ $? -eq 0 ];
then
  echo "Begin to make csv files for UnixBench 16 threads..."
  sh UnixBench_16thread_csvFile_get.sh $TestType $Platform $TestCase
fi

