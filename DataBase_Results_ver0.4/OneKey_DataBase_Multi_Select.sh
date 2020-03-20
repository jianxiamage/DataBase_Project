#!/bin/bash

if [ $# -ne 2 ];then
 echo "usage: $0 TestType Platform" 
 exit 1
fi
#---------------------------------------------
TestType=$1
Platform=$2
#---------------------------------------------

start_time=`date +%s`              #定义脚本运行的开始时间

echo "Begin to write database tables for the TestResults.TestType:[$TestType],TestPlat:[$Platform]"

pushd Test_Results
echo "========================writing Current Testresults to database Begin.=========================="
sh make_Results_Table.sh $TestType $Platform
echo "========================writing Current Testresults to database End============================="
popd

pushd Perform_Score
echo "===========converting ini files to csv files for the perform score testcases Begin.=============="
sh Make_score2csv_Multi.sh $TestType $Platform
echo "========================writing Current Testresults to database End============================="
echo "===========converting ini files to csv files for the perform score testcases End.=============="

echo "========================writing Current perform score to database Begin.========================"
sh Write_DataBase_Multi.sh $TestType $Platform
echo "========================writing Current perform score to database End.=========================="
popd

pushd Bak_Test_Results
echo "===================Bakup the Testresults to database Begin.===================="
sh backup_TestResults_ALL.sh $TestType $Platform
echo "===================Bakup Current Testresults to database Begin.===================="
popd

pushd Bak_Perform_Score
echo "===================Bakup the Perform Score tables to database Begin.=================="
sh Backup_DataBase_Multi.sh $TestType $Platform
echo "===================Bakup the Perform Score tables to database End.===================="
popd

stop_time=`date +%s`  #定义脚本运行的结束时间

echo "******************************************************"
echo "Exec Time:`expr $stop_time - $start_time`s"
echo "******************************************************"

echo "Write the database tables for the TestResults End.TestType:[$TestType],TestPlat:[$Platform]"
