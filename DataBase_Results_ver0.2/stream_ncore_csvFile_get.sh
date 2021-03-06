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
#source ./grab_TestTag.sh $TestType $Platform
#get_outputType=$get_outputType
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

echo "Begin to convert ini file to csv file..."

class_type=`sh grab_TestTag.sh $TestType $Platform "ClassifyType"`
echo "class_type:$class_type"

Tag="${class_type}_${Platform}_${TestType}"

python perform_stream_ncore_2csv.py $TestType $Platform $TestCase $Tag
