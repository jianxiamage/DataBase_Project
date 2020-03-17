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


echo "Begin to make table:caseNode_BaseInfo"
python caseNode_BaseInfo.py $TestType $Platform $Tag
