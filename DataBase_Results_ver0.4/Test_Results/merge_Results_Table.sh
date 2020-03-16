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

echo "Begin to write results to database..."

sh get_node_BaseInfo.sh $TestType $Platform

sh get_caseNode_BaseInfo.sh $TestType $Platform

sh get_caseNode_DetailInfo.sh $TestType $Platform

sh get_results_BaseInfo.sh $TestType $Platform

sh get_results_caseNode_BaseInfo.sh $TestType $Platform

sh get_results_caseNode_DetailInfo.sh $TestType $Platform

#sh get_Results_Base_ALL.sh $TestType $Platform

#sh get_Results_Detail_ALL.sh $TestType $Platform
