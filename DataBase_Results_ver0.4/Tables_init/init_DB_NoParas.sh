#!/bin/bash

#初始化数据库中的表:
#删除数据库中有关中间测试结果表
#用户只需要看最终结果表，以免造成大量结果表展示效果不明晰

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
