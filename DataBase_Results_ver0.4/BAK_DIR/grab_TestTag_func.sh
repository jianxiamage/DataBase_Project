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

#OS_Type=`cat /.buildstamp |grep Product|awk -F"=" '{print $2}'`

function get_outputType()
{
     
  if [ $# -ne 1 ];then
    echo "usage: $0 tpye" 
    return 1
  fi

  input_type=$1

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
          echo "UnSupport This OS Type:$OS_Type"
          exit 1
      ;;
  esac

  echo $ret_Str

}


#get_outputType ClassifyType

