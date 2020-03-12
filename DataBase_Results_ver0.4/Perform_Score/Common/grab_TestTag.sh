#!/bin/bash
#set -e

if [ $# -ne 3 ];then
 echo "usage: $0 TestType Platform input_type" 
 exit 1
fi
#----------------------------------------------------------------------------------------
TestType="$1"
Platform="$2"
input_type=$3
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
resultsPath='/data'
webPath='/Results'
#----------------------------------------------------------------------------------------
destFileName=BasicInfo.txt
destPath="${resultsPath}/${TestType}/${Platform}"
destFile="${resultsPath}/${TestType}/${Platform}/${destFileName}"
#----------------------------------------------------------------------------------------


if [ ! -s ${destFile} ];
then
  echo "${destFile} Not exitsts!"
fi



input_type=$3

    case $input_type in
        "MarkTime")
        ;;
  
        "ClassifyType")
           ret_Str=`cat ${destFile} |grep ${input_type} | awk -F":" '{print $2}'|cut -d '[' -f2|cut -d ']' -f1`
        ;;
  
        "TestType")
        ;;
  
        "Platform")
        ;;
  
        "OS_Type")
        ;;
  
        "OS_Ver")
        ;;
  
        "Kernel_Ver")
        ;;
  
        *)
            echo "UnSupport This type:$input_type"
            exit 1
        ;;
    esac

ret_Str=`cat ${destFile} |grep ${input_type} | awk -F":" '{print $2}'|cut -d '[' -f2|cut -d ']' -f1`
echo "$ret_Str"
