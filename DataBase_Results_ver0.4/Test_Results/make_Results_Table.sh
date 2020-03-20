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

#----------------------------------------------------------
start_time=`date +%s`              #定义脚本运行的开始时间
#----------------------------------------------------------

#---------------------------------------------------------
#转换ini文件为csv文件并使用其制作节点基本信息表:[node_BaseInfo]
echo "Begin to make csv file for table:node_BaseInfo"
python node_BaseInfo_2csv.py $TestType $Platform $Tag

echo "Begin to make table:node_BaseInfo"
python node_BaseInfo.py $TestType $Platform $Tag
#---------------------------------------------------------

#---------------------------------------------------------
#转换ini文件为csv文件并使用其制作结果基本信息表:[results_BaseInfo]
echo "Begin to make csv file for table:results_BaseInfo"
python results_BaseInfo_2csv.py $TestType $Platform $Tag

echo "Begin to make table:results_BaseInfo"
python results_BaseInfo.py $TestType $Platform $Tag
#---------------------------------------------------------

#---------------------------------------------------------
#合并测试用例分组信息表与节点基本信息表-->[测试用例与节点基本信息表]
echo "Begin to make table:caseNode_BaseInfo"
python caseNode_BaseInfo.py $TestType $Platform $Tag

#合并测试用例详细信息表与节点基本信息表-->[测试用例与节点详细信息表]
echo "Begin to make table:caseNode_DetailInfo"
python caseNode_DetailInfo.py $TestType $Platform $Tag
#---------------------------------------------------------

#---------------------------------------------------------
#合并测试用例详细信息表与结果基本信息表-->[测试用例测试结果基本信息表]
echo "Begin to make table:results_caseNode_BaseInfo"
python results_caseNode_BaseInfo.py $TestType $Platform $Tag
#---------------------------------------------------------

#---------------------------------------------------------
#合并详细信息表与结果基本信息表-->[测试用例测试结果详细信息表]
echo "Begin to make table:results_caseNode_DetailInfo"
python results_caseNode_DetailInfo.py $TestType $Platform $Tag
#---------------------------------------------------------

#---------------------------------------------------------
#合并测试用例基本信息表与结果基本信息表-->[测试用例测试结果详细信息表]
echo "Begin to make table:TestResults_Table_Base_ALL"
python TestResults_Table_Base_ALL.py $TestType $Platform $Tag
#---------------------------------------------------------

#---------------------------------------------------------
#合并测试用例详细信息表与结果基本信息表-->[测试用例测试结果详细信息表]
echo "Begin to make table:TestResults_Table_Detail_ALL"
python TestResults_Table_Detail_ALL.py $TestType $Platform $Tag
#---------------------------------------------------------

#按照测试类型和平台生成的各自的数据表作为中间过渡，如需显示效果好像，可将其删除
#pushd ../Tables_init
#echo "================Delete the current test results tables of database Begin.=================="
#sh init_Tables_results.sh $TestType $Platform
#echo "================Delete the current test results tables of database End.=================="
#popd


#----------------------------------------------------------
stop_time=`date +%s`  #定义脚本运行的结束时间
#----------------------------------------------------------

echo "***************************************************"
echo "Exec Time:`expr $stop_time - $start_time`s"
echo "***************************************************"

