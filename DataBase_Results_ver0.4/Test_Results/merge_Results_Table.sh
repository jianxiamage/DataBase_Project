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

#----------------------------------------------------------
start_time=`date +%s`              #定义脚本运行的开始时间
#----------------------------------------------------------

echo "Begin to write results to database..."

sh get_node_BaseInfo.sh $TestType $Platform

sh get_caseNode_BaseInfo.sh $TestType $Platform

sh get_caseNode_DetailInfo.sh $TestType $Platform

sh get_results_BaseInfo.sh $TestType $Platform

sh get_results_caseNode_BaseInfo.sh $TestType $Platform

sh get_results_caseNode_DetailInfo.sh $TestType $Platform

sh get_Results_Base_ALL.sh $TestType $Platform

sh get_Results_Detail_ALL.sh $TestType $Platform

#按照测试类型和平台生成的各自的数据表作为中间过渡，如需显示效果好像，可将其删除
#pushd ../Tables_init
#echo "================Delete the current test results tables of database Begin.================"
#sh init_Tables_results.sh $TestType $Platform
#echo "================Delete the current test results tables of database End.=================="
#popd

#----------------------------------------------------------
stop_time=`date +%s`  #定义脚本运行的结束时间
#----------------------------------------------------------

echo "***************************************************"
echo "Exec Time:`expr $stop_time - $start_time`s"
echo "***************************************************"

