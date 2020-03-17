#!/bin/bash
set -e

if [ $# -ne 3 ];then
 echo "usage: $0 TestType Platform TestCase" 
 exit 1
fi
#----------------------------------------------------------------------------------------
TestType="$1"
Platform="$2"
TestCase="$3"
#----------------------------------------------------------------------------------------
echo --------------------------------------------------------------------------------
echo "将性能测试跑分结果csv文件数据写入数据库..."
echo "当前路径:"
pwd 
echo --------------------------------------------------------------------------------

#---------------------------------------------------
#进入测试用例目录
pushd ${TestCase}
#---------------------------------------------------

#There are many branches for test cases in judgment.So use case mode...
case $TestCase in
"iozone")
    echo --------------------------------------------------------------------------------
    cmdStr="The current test case is $TestCase."
    echo $cmdStr
    sh iozone_database.sh $TestType $Platform $TestCase
    echo --------------------------------------------------------------------------------
    ;;

"netperf")
    cmdStr="The current test case is $TestCase."
    echo $cmdStr
    ;;

"lmbench")
    echo --------------------------------------------------------------------------------
    cmdStr="The current test case is $TestCase."
    echo $cmdStr
    echo --------------------------------------------------------------------------------
    ;;

"stream")
    echo --------------------------------------------------------------------------------
    cmdStr="The current test case is $TestCase."
    echo $cmdStr

    #stream单核测试
    sh stream_database.sh $TestType $Platform $TestCase

    echo --------------------------------------------------------------------------------
    ;;

"UnixBench")
    echo --------------------------------------------------------------------------------
    cmdStr="The current test case is $TestCase."
    echo $cmdStr
    
    #UnixBench在不同机器上执行不同的线程脚本，会生成不同的测试结果文件，因此需要判断后执行
    sh judge_UnixBench_database.sh $TestType $Platform
    #echo --------------------------------------------------------------------------------
    ;;

"spec2000-1core")
    echo --------------------------------------------------------------------------------
    cmdStr="The current test case is $TestCase."
    echo $cmdStr
    
    #spec2000单核浮点型及整型测试结果
    sh spec2000-1core_database.sh $TestType $Platform $TestCase

    echo --------------------------------------------------------------------------------
    ;;

"spec2000-ncore")
    echo --------------------------------------------------------------------------------
    cmdStr="The current test case is $TestCase."
    echo $cmdStr

    #spec2000多核浮点型及整型测试结果
    sh spec2000-ncore_database.sh $TestType $Platform $TestCase

    echo --------------------------------------------------------------------------------
    ;;

"spec2006-1core")
    echo --------------------------------------------------------------------------------
    cmdStr="The current test case is $TestCase."
    echo $cmdStr

    #spec2006单核浮点型及整型测试结果
    sh spec2006-1core_database.sh $TestType $Platform $TestCase

    echo --------------------------------------------------------------------------------
    ;;

"spec2006-ncore")
    echo --------------------------------------------------------------------------------
    cmdStr="The current test case is $TestCase."
    echo $cmdStr

    #spec2000多核浮点型及整型测试结果
    sh spec2006-ncore_database.sh $TestType $Platform $TestCase

    echo --------------------------------------------------------------------------------
    ;;

"SpecJvm2008")
    echo --------------------------------------------------------------------------------
    cmdStr="The current test case is $TestCase."
    echo $cmdStr

    #SpecJvm2008测试
    sh SpecJvm2008_database.sh $TestType $Platform $TestCase

    echo --------------------------------------------------------------------------------
    ;;

*)
    cmdStr="Error:UnSupport this Testcase:$Testcase.Please check it!"
    echo $cmdStr
    exit 1
    ;;
esac

#---------------------------------------------------
#退出测试用例目录
pushd
#---------------------------------------------------

echo [$TestCase] score data write to database finished!
echo --------------------------------------------------------------------------------
