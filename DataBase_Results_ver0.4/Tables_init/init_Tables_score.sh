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
opt_sql_path=/tmp/score_drop.sql
#---------------------------------------------------

#也可以写 HOSTNAME="localhost"，端口号 PORT可以不设定

#-----------------------------------------------------------------------------------------------
#性能跑分数据表(以score_开头)进行删除的sql语句
drop_score_sql="Select CONCAT( 'drop table ', table_name, ';') 
                                 FROM information_schema.tables 
                                 Where table_schema='${DBNAME}' and table_name LIKE 'score_%'; " 

#echo $drop_score_sql
#将性能跑分数据表(以score_开头)表名查询后存放在文件中
mysql -h${HOSTNAME} -P${PORT}  -u${USERNAME} -p${PASSWORD} --skip-column-names -A -e "${drop_score_sql}" > $opt_sql_path

#将性能跑分数据表(以score_开头)全部删除
mysql -h${HOSTNAME} -P${PORT}  -u${USERNAME} -p${PASSWORD} ${DBNAME} --show-warnings -v -v -v -e "source $opt_sql_path"
