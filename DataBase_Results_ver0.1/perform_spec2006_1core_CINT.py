#!/usr/bin/python
# -*- coding: UTF-8 -*-

from itertools import islice 

import MySQLdb
import io

# 打开数据库连接
conn = MySQLdb.connect("localhost", "autotest", "loongson", "AutoTest", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = conn.cursor()

#node_num varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci,
#--------------------------------------------------------------------
sql_create = '''
create table if not exists score_spec2006_1core_CINT(
  node_num int(10) NOT NULL AUTO_INCREMENT,
  `400.perlbench` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci, 
  `401.bzip2` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci, 
  `403.gcc` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci, 
  `429.mcf` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci, 
  `445.gobmk` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci, 
  `456.hmmer` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci, 
  `458.sjeng` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci, 
  `462.libquantum` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci, 
  `464.h264ref` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci, 
  `471.omnetpp` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci, 
  `473.astar` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci, 
  `483.xalancbmk` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci, 
  SPECint_base2006 varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci, 
  PRIMARY KEY (node_num)
) CHARACTER SET utf8 COLLATE utf8_general_ci;
'''
#--------------------------------------------------------------------

cursor.execute(sql_create)
cursor.execute('truncate table score_spec2006_1core_CINT;')
sql_insert = '''
insert into score_spec2006_1core_CINT(`400.perlbench`,`401.bzip2`,`403.gcc`,`429.mcf`,`445.gobmk`,`456.hmmer`,`458.sjeng`,`462.libquantum`,`464.h264ref`,`471.omnetpp`,`473.astar`,`483.xalancbmk`,SPECint_base2006
) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
'''

i=1
with io.open('spec2006-1core_CINT.csv', mode= 'rt', encoding='utf-8') as file_handler:
    # 通过迭代器，遍历csv文件中的所有样本
    lines = file_handler.readlines()
    #使用islice的原因是跳过csv文件第一行
    for line in islice(lines, 1, None): 
       #res = ''.join(line).strip('\n').split(',')
       res = ''.join(line).strip('\n').split(',')
       print('-------------------------------------')
       #print(res)
       if res != ['']:
         cursor.execute(sql_insert,[res[0], res[1], res[2],res[3], res[4], res[5], res[6], res[7], res[8], res[9], res[10], res[11], res[12]])

         print(i)
         print(res)
       i = i + 1

    conn.commit()
    cursor.close()
    conn.close()

print('=========================================================')

