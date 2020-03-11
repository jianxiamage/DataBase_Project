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
create table if not exists score_spec2006_ncore_CFP(
  node_num int(10) NOT NULL AUTO_INCREMENT,
  `410.bwaves` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `416.gamess` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `433.milc` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `434.zeusmp` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `435.gromacs` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `436.cactusADM` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `437.leslie3d` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `444.namd` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `447.dealII` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `450.soplex` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `453.povray` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `454.calculix` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `459.GemsFDTD` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `465.tonto` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `470.lbm` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `481.wrf` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `482.sphinx3` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  SPECfp_rate_base2006 varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  PRIMARY KEY (node_num)
) CHARACTER SET utf8 COLLATE utf8_general_ci;
'''
#--------------------------------------------------------------------

cursor.execute(sql_create)
cursor.execute('truncate table score_spec2006_ncore_CFP;')
sql_insert = '''
insert into score_spec2006_ncore_CFP(`410.bwaves`,`416.gamess`,`433.milc`,`434.zeusmp`,`435.gromacs`,`436.cactusADM`,`437.leslie3d`,`444.namd`,`447.dealII`,`450.soplex`,`453.povray`,`454.calculix`,`459.GemsFDTD`,`465.tonto`,`470.lbm`,`481.wrf`,`482.sphinx3`,SPECfp_rate_base2006)
values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
'''

i=1
with io.open('spec2006-ncore_CFP.csv', mode= 'rt', encoding='utf-8') as file_handler:
    # 通过迭代器，遍历csv文件中的所有样本
    lines = file_handler.readlines()
    #使用islice的原因是跳过csv文件第一行
    for line in islice(lines, 1, None): 
       #res = ''.join(line).strip('\n').split(',')
       res = ''.join(line).strip('\n').split(',')
       print('-------------------------------------')
       #print(res)
       if res != ['']:
         cursor.execute(sql_insert,[res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7],res[8],res[9],res[10],res[11],res[12],res[13],res[14],res[15],res[16],res[17]])

         print(i)
         print(res)
       i = i + 1

    conn.commit()
    cursor.close()
    conn.close()

print('=========================================================')

