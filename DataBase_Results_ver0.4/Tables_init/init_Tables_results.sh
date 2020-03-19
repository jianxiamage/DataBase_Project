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
node_BaseInfo_sql_path=/tmp/node_BaseInfo_drop.sql
caseNode_sql_path=/tmp/caseNode_drop.sql
results_sql_path=/tmp/results_drop.sql
#---------------------------------------------------

#-----------------------------------------------------------------------------------------------
#node_BaseInfo表
drop_nodeBaseInfo_sql="Select CONCAT( 'drop table ', table_name, ';') 
                                 FROM information_schema.tables 
                                 Where table_schema='${DBNAME}' and table_name LIKE 'node_BaseInfo_%'; " 

#echo $drop_nodeBaseInfo_sql
#拼接删除语句到指定文件
mysql -h${HOSTNAME} -P${PORT}  -u${USERNAME} -p${PASSWORD} --skip-column-names -A -e "${drop_nodeBaseInfo_sql}" > $node_BaseInfo_sql_path

#执行删除语句
mysql -h${HOSTNAME} -P${PORT}  -u${USERNAME} -p${PASSWORD} ${DBNAME} --show-warnings -v -v -v -e "source $node_BaseInfo_sql_path"

#-----------------------------------------------------------------------------------------------
#caseNode_BaseInfo表以及caseNode_Detail表
drop_caseNode_sql="Select CONCAT( 'drop table ', table_name, ';') 
                                 FROM information_schema.tables 
                                 Where table_schema='${DBNAME}' and table_name LIKE 'caseNode_%'; "

#echo $drop_caseNode_sql
#拼接删除语句到指定文件
mysql -h${HOSTNAME} -P${PORT}  -u${USERNAME} -p${PASSWORD} --skip-column-names -A -e "${drop_caseNode_sql}" > $caseNode_sql_path

#执行删除语句
mysql -h${HOSTNAME} -P${PORT}  -u${USERNAME} -p${PASSWORD} ${DBNAME} --show-warnings -v -v -v -e "source $caseNode_sql_path"

#-----------------------------------------------------------------------------------------------
#results_BaseInfo表以及results_caseNode_Base表,results_caseNode_Detail
drop_results_sql="Select CONCAT( 'drop table ', table_name, ';') 
                                 FROM information_schema.tables 
                                 Where table_schema='${DBNAME}' and table_name LIKE 'results_%'; "

#echo $drop_results_sql
#拼接删除语句到指定文件
mysql -h${HOSTNAME} -P${PORT}  -u${USERNAME} -p${PASSWORD} --skip-column-names -A -e "${drop_results_sql}" > $results_sql_path

#执行删除语句
mysql -h${HOSTNAME} -P${PORT}  -u${USERNAME} -p${PASSWORD} ${DBNAME} --show-warnings -v -v -v -e "source $results_sql_path"
