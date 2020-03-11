#!/usr/bin/env python
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
create table if not exists score_SpecJvm2008(
  node_num int(10) NOT NULL AUTO_INCREMENT,
  compiler varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  compress varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  crypto varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  derby varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  mpegaudio varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `scimark.large` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `scimark.small` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  serial varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  startup varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  sunflow varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  xml varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `Composite-result` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  PRIMARY KEY (node_num)
) CHARACTER SET utf8 COLLATE utf8_general_ci;
'''
#--------------------------------------------------------------------

cursor.execute(sql_create)
cursor.execute('truncate table score_SpecJvm2008;')
sql_insert = '''
insert into score_SpecJvm2008(compiler,compress,crypto,derby,mpegaudio,`scimark.large`,`scimark.small`,serial,startup,sunflow,xml,`Composite-result`) values(%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s);
'''

i=1
with io.open('SpecJvm2008.csv', mode= 'rt', encoding='utf-8') as file_handler:
    # 通过迭代器，遍历csv文件中的所有样本
    lines = file_handler.readlines()
    #使用islice的原因是跳过csv文件第一行
    for line in islice(lines, 1, None): 
       #res = ''.join(line).strip('\n').split(',')
       res = ''.join(line).strip('\n').split(',')
       print('-------------------------------------')
       #print(res)
       if res != ['']:
         cursor.execute(sql_insert,[res[0], res[1], res[2],res[3], res[4], res[5], res[6], res[7], res[8],res[9], res[10], res[11]])

         print(i)
         print(res)
       i = i + 1

    conn.commit()
    cursor.close()
    conn.close()

print('=========================================================')

