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

#----------------------------------------------------------------------------
class_type=`sh ../Common/grab_TestTag.sh $TestType $Platform "ClassifyType"`
echo "class_type:$class_type"

Tag="${class_type}_${Platform}_${TestType}"
test_type=`sh ../Common/grab_TestTag.sh $TestType $Platform "TestType"`
echo "test_type:$test_type"

test_plat=`sh ../Common/grab_TestTag.sh $TestType $Platform "Platform"`
echo "test_plat:$test_plat"

name_Tag=''

case ${TestType} in

    "OS")

        OS_Ver=`sh ../Common/grab_TestTag.sh $TestType $Platform "OS_Ver"`
        echo "OS Version:$OS_Ver"
        name_Tag=$OS_Ver
        echo "name_Tag:${name_Tag}"
        echo "Begin to backup table:${name_Tag}_TestResults_Table_Base_ALL"
        python backup_TestResults_Table_Detail_ALL.py $TestType $Platform $Tag $name_Tag
        
        ;;
    "Kernel")

        Kernel_Ver=`sh ../Common/grab_TestTag.sh $TestType $Platform "Kernel_Ver"`
        echo "Kernel Version:$Kernel_Ver"
        name_Tag=$Kernel_Ver
        echo "name_Tag:${name_Tag}"
        echo "Begin to backup table:${name_Tag}_TestResults_Table_Base_ALL"
        python backup_TestResults_Table_Detail_ALL.py $TestType $Platform $Tag $name_Tag

        ;;

    "KVM")

        echo "test_type:$test_type"

        ;;
    *)
        echo "Not support the current class Type:${class_type}"
        exit 1
        ;;
esac

