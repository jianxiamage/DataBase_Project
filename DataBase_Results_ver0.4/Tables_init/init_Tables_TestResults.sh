#!/bin/bash

#---------------------------------------------------
#数据库信息
HOSTNAME="127.0.0.1"
PORT="3306"
USERNAME="autotest"
PASSWORD="loongson"
DBNAME="AutoTest"
#---------------------------------------------------
#数据表操作语句存放文件
TestResults_sql_path=/tmp/results_drop.sql
#---------------------------------------------------

#-----------------------------------------------------------------------------------------------
#results_BaseInfo表以及results_caseNode_Base表,results_caseNode_Detail
drop_TestResults_sql="Select CONCAT( 'drop table ', table_name, ';') 
                                 FROM information_schema.tables 
                                 Where table_schema='${DBNAME}' and table_name LIKE 'TestResults_%'; "

#echo $drop_TestResults_sql
#拼接删除语句到指定文件
mysql -h${HOSTNAME} -P${PORT}  -u${USERNAME} -p${PASSWORD} --skip-column-names -A -e "${drop_TestResults_sql}" > $TestResults_sql_path

#执行删除语句
mysql -h${HOSTNAME} -P${PORT}  -u${USERNAME} -p${PASSWORD} ${DBNAME} --show-warnings -v -v -v -e "source $TestResults_sql_path"
