#!/bin/bash
#set -e

if [ $# -ne 2 ];then
 echo "usage: $0 TestType Platform" 
 exit 1
fi

#----------------------------------------------------------------------------------------
TestType="$1"
Platform="$2"
#----------------------------------------------------------------------------------------
sh backup_TestResults_Base_ALL.sh $TestType $Platform
if [ $? -ne 0 ];
then
  echo "Backup the TestResult_Base table failed!"
fi 

sh backup_TestResults_Detail_ALL.sh $TestType $Platform
if [ $? -ne 0 ];
then
  echo "Backup the TestResult_Detail table failed!"
fi 
