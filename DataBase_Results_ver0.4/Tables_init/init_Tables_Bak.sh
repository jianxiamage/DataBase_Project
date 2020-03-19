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
opt_sql_path=/tmp/Bak_drop.sql
#---------------------------------------------------

#本机也可以写 HOSTNAME="localhost"，端口号 PORT可以不设定

#-----------------------------------------------------------------------------------------------
#备份数据表--->>进行删除的sql语句
drop_Bak_sql="Select CONCAT( 'drop table ', table_name, ';') 
                                 FROM information_schema.tables 
                                 Where table_schema='${DBNAME}' and table_name LIKE 'Bak_%'; " 

#echo $drop_Bak_sql
#将备份数据表的删除语句存放在文件中
mysql -h${HOSTNAME} -P${PORT}  -u${USERNAME} -p${PASSWORD} --skip-column-names -A -e "${drop_Bak_sql}" > $opt_sql_path


#---------------------------------------------------
#由于备份表名中含有保留字(如横线-,或者点.之类)，
#不能直接执行sql语句，因此需要在表名两侧添加符号:``
sed -i 's/Bak/`Bak/g' $opt_sql_path
sed -i 's/;/`;/g' $opt_sql_path
#---------------------------------------------------

#将备份数据表全部删除
mysql -h${HOSTNAME} -P${PORT}  -u${USERNAME} -p${PASSWORD} ${DBNAME} --show-warnings -v -v -v -e "source $opt_sql_path"
