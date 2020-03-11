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
create table if not exists score_stream_ncore(
  node_num int(10) NOT NULL AUTO_INCREMENT,
  Copy varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  Scale varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `Add` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  Triad varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  PRIMARY KEY (node_num)
) CHARACTER SET utf8 COLLATE utf8_general_ci;
'''
#--------------------------------------------------------------------

cursor.execute(sql_create)
cursor.execute('truncate table score_stream_ncore;')
sql_insert = '''
insert into score_stream_ncore(Copy,Scale,`Add`,Triad) values(%s, %s, %s, %s);
'''

i=1
with io.open('stream_ncore.csv', mode= 'rt', encoding='utf-8') as file_handler:
    # 通过迭代器，遍历csv文件中的所有样本
    lines = file_handler.readlines()
    #使用islice的原因是跳过csv文件第一行
    for line in islice(lines, 1, None): 
       #res = ''.join(line).strip('\n').split(',')
       res = ''.join(line).strip('\n').split(',')
       print('-------------------------------------')
       #print(res)
       if res != ['']:
         cursor.execute(sql_insert,[res[0], res[1], res[2],res[3]])

         print(i)
         print(res)
       i = i + 1

    conn.commit()
    cursor.close()
    conn.close()

print('=========================================================')

