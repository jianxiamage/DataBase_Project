#!/bin/bash

#-----------------------------------------------------
#初始化数据库中的表:
#-----------------------------------------------------

#初始化性能跑分表
mysql -uroot -h127.0.0.1 --skip-column-names -A -e "Select CONCAT( 'drop table ', table_name, ';') 
                                 FROM information_schema.tables 
                                 Where table_schema='AutoTest' and table_name LIKE 'score_%'; " > /tmp/score_drop.sql


mysql -uroot -h127.0.0.1 AutoTest --show-warnings -v -v -v -e "source /tmp/score_drop.sql"


#初始化性能跑分表
mysql -uroot -h127.0.0.1 --skip-column-names -A -e "Select CONCAT( 'drop table ', table_name, ';') 
                                 FROM information_schema.tables 
                                 Where table_schema='AutoTest' and table_name LIKE 'Bak_%'; " > /tmp/Bak_drop.sql

#---------------------------------------------------
#由于备份表名中含有保留字(如横线-,或者点.之类)，
#不能直接执行sql语句，因此需要在表名两侧添加符号:``
sed -i 's/Bak/`Bak/g' /tmp/Bak_drop.sql
sed -i 's/;/`;/g' /tmp/Bak_drop.sql
#---------------------------------------------------

mysql -uroot -h127.0.0.1 AutoTest --show-warnings -v -v -v -e "source /tmp/Bak_drop.sql"


#初始化测试结果文件(caseNode表)
mysql -uroot -h127.0.0.1 --skip-column-names -A -e "Select CONCAT( 'drop table ', table_name, ';') 
                                 FROM information_schema.tables 
                                 Where table_schema='AutoTest' and table_name LIKE 'caseNode_%'; " > /tmp/caseNode_drop.sql

mysql -uroot -h127.0.0.1 AutoTest --show-warnings -v -v -v -e "source /tmp/caseNode_drop.sql"

#初始化测试结果文件(node_BaseInfo)
mysql -uroot -h127.0.0.1 --skip-column-names -A -e "Select CONCAT( 'drop table ', table_name, ';') 
                                 FROM information_schema.tables 
                                 Where table_schema='AutoTest' and table_name LIKE 'node_BaseInfo_%'; " > /tmp/node_BaseInfo_drop.sql

mysql -uroot -h127.0.0.1 AutoTest --show-warnings -v -v -v -e "source /tmp/node_BaseInfo_drop.sql"


#初始化测试结果文件(node_BaseInfo)
mysql -uroot -h127.0.0.1 --skip-column-names -A -e "Select CONCAT( 'drop table ', table_name, ';') 
                                 FROM information_schema.tables 
                                 Where table_schema='AutoTest' and table_name LIKE 'results_BaseInfo_%'; " > /tmp/results_BaseInfo_drop.sql

mysql -uroot -h127.0.0.1 AutoTest --show-warnings -v -v -v -e "source /tmp/results_BaseInfo_drop.sql"


#初始化测试结果文件(node_BaseInfo)
mysql -uroot -h127.0.0.1 --skip-column-names -A -e "Select CONCAT( 'drop table ', table_name, ';') 
                                 FROM information_schema.tables 
                                 Where table_schema='AutoTest' and table_name LIKE 'results_caseNode_BaseInfo_%'; " > /tmp/results_caseNode_BaseInfo_drop.sql

mysql -uroot -h127.0.0.1 AutoTest --show-warnings -v -v -v -e "source /tmp/results_caseNode_BaseInfo_drop.sql"

#初始化测试结果文件(node_BaseInfo)
mysql -uroot -h127.0.0.1 --skip-column-names -A -e "Select CONCAT( 'drop table ', table_name, ';') 
                                 FROM information_schema.tables 
                                 Where table_schema='AutoTest' and table_name LIKE 'results_caseNode_DetailInfo_%'; " > /tmp/results_caseNode_DetailInfo_drop.sql

mysql -uroot -h127.0.0.1 AutoTest --show-warnings -v -v -v -e "source /tmp/results_caseNode_DetailInfo_drop.sql"
