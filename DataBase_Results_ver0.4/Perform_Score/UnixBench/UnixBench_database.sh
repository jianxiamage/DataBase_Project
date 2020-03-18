#!/bin/bash
#set -e

if [ $# -ne 3 ];then
 echo "usage: $0 TestType Platform TestCase" 
 exit 1
fi

#----------------------------------------------------------------------------------------
TestType="$1"
Platform="$2"
TestCase="$3"
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

echo "Begin to write to database by csv file..."

#python -c 'import merge_Excel_Case; merge_Excel_Case.mergeTestExcel("'$TestType'","'$Platform'","'$TestCase'")' 

#class_type=`get_outputType "ClassifyType"`

class_type=`sh ../../Common/grab_TestTag.sh $TestType $Platform "ClassifyType"`
echo "class_type:$class_type"

Tag="${class_type}_${Platform}_${TestType}"

echo "TestCase:$TestCase"

python perform_UnixBench.py $TestType $Platform $TestCase $Tag
