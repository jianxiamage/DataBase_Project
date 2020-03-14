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

#----------------------------------------------------------------------------------------
#使用python虚拟环境执行命令
export WORKON_HOME=/home/work/env-wrapper

echo ---------------------------------
echo 'active the virtualenvwrapper'
echo ---------------------------------
source /usr/bin/virtualenvwrapper.sh

echo ---------------------------------
echo 'change to virtualenv:env-database'
echo ---------------------------------
workon env-database

#-----------------------------------------------------------------------------
class_type=`sh ../Common/grab_TestTag.sh $TestType $Platform "ClassifyType"`
echo "class_type:$class_type"

Tag="${class_type}_${Platform}_${TestType}"

echo "TestCase:$TestCase"

echo "Begin to make csv file for table:node_BaseInfo"
python node_BaseInfo_2csv.py $TestType $Platform $TestCase $Tag

echo "Begin to make table:node_BaseInfo"
python node_BaseInfo.py $TestType $Platform $TestCase $Tag

echo "Begin to make csv file for table:results_BaseInfo"
python results_BaseInfo_2csv.py $TestType $Platform $TestCase $Tag

echo "Begin to make table:results_BaseInfo"
python results_BaseInfo.py $TestType $Platform $TestCase $Tag

echo "Begin to make table:caseNode_BaseInfo"
python caseNode_BaseInfo.py $TestType $Platform $TestCase $Tag

echo "Begin to make table:caseNode_DetailInfo"
python caseNode_DetailInfo.py $TestType $Platform $TestCase $Tag

echo "Begin to make table:results_caseNode_BaseInfo"
python results_caseNode_BaseInfo.py $TestType $Platform $TestCase $Tag

echo "Begin to make table:results_caseNode_DetailInfo"
python results_caseNode_DetailInfo.py $TestType $Platform $TestCase $Tag

echo "Begin to make table:Results_Table_Base_ALL"
python Results_Table_Base_ALL.py $TestType $Platform $TestCase $Tag

echo "Begin to make table:Results_Table_Detail_ALL"
python Results_Table_Detail_ALL.py $TestType $Platform $TestCase $Tag
