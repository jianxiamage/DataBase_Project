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
#----------------------------------------------------------------------------------------
resultsPath='/data'
PointsPath='Points_Files'
Node_count=0
#----------------------------------------------------------------------------------------
#测试结果目录(筛选内容后)地址
detailDir="Detail"
destPath="${resultsPath}/${TestType}/${Platform}/${detailDir}/${TestCase}/${PointsPath}"
#----------------------------------------------------------------------------------------


echo "-------------------------------------------------------------"
#----------------------------------------------------------------------------------------
#首先检查目标目录是否存在
if [ ! -s $destPath ];
then
  echo Error! [$destPath] not existed!Please check it!
  exit 1
fi

#----------------------------------------------------------------------------------------
#检查测试结果文件是否生成
ls $destPath/ | grep "${TestCase}" |grep "ini"

if [ $? -ne 0 ];
then
  echo "No ini files for $TestCase exists!Please check it!"
  exit 1
fi

echo "-------------------------------------------------------------"

#----------------------------------------------------------------------------------------
#判断是否存在相应的ini文件，从而分别写入csv文件
num_th="1 2 4 8 16"
for i in $num_th;
do
  ls $destPath/ | grep "${TestCase}" |grep "ini" |grep "${i}thread"
  if [ $? -eq 0 ];
  then
    echo "Begin to make csv files for UnixBench $i thread..."
    TestMode="UnixBench_${i}thread"
    sh UnixBench_csvFile_get.sh $TestType $Platform $TestMode
  fi
done
#----------------------------------------------------------------------------------------
