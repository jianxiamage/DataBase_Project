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
create table if not exists score_spec2000_ncore_CINT(
  node_num int(10) NOT NULL AUTO_INCREMENT,
  `164.gzip` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `175.vpr` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `176.gcc` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `181.mcf` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `186.crafty` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `197.parser` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `252.eon` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `253.perlbmk` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `254.gap` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `255.vortex` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `256.bzip2` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `300.twolf` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  SPECint_rate_base2000 varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  PRIMARY KEY (node_num)
) CHARACTER SET utf8 COLLATE utf8_general_ci;
'''
#--------------------------------------------------------------------

cursor.execute(sql_create)
cursor.execute('truncate table score_spec2000_ncore_CINT;')
sql_insert = '''
insert into score_spec2000_ncore_CINT(`164.gzip`,`175.vpr`,`176.gcc`,`181.mcf`,`186.crafty`,`197.parser`,`252.eon`,`253.perlbmk`,`254.gap`,`255.vortex`,`256.bzip2`,`300.twolf`,SPECint_rate_base2000) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
'''

i=1
with io.open('spec2000-ncore_CINT.csv', mode= 'rt', encoding='utf-8') as file_handler:
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

