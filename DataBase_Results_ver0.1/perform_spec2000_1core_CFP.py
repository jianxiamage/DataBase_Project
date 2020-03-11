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
create table if not exists score_spec2000_1core_CFP(
  node_num int(10) NOT NULL AUTO_INCREMENT,
  `168.wupwise` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `171.swim` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `172.mgrid` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `173.applu` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `177.mesa` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `178.galgel` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `179.art` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `183.equake` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `187.facerec` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `188.ammp` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `189.lucas` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `191.fma3d` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `200.sixtrack` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `301.apsi` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  SPECfp_base2000 varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  PRIMARY KEY (node_num)
) CHARACTER SET utf8 COLLATE utf8_general_ci;
'''
#--------------------------------------------------------------------

cursor.execute(sql_create)
cursor.execute('truncate table score_spec2000_1core_CFP;')
sql_insert = '''
insert into score_spec2000_1core_CFP(`168.wupwise`,`171.swim`,`172.mgrid`,`173.applu`,`177.mesa`,`178.galgel`,`179.art`,`183.equake`,`187.facerec`,`188.ammp`,`189.lucas`,`191.fma3d`,`200.sixtrack`,`301.apsi`,SPECfp_base2000) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s);
'''

i=1
with io.open('spec2000-1core_CFP.csv', mode= 'rt', encoding='utf-8') as file_handler:
    # 通过迭代器，遍历csv文件中的所有样本
    lines = file_handler.readlines()
    #使用islice的原因是跳过csv文件第一行
    for line in islice(lines, 1, None): 
       #res = ''.join(line).strip('\n').split(',')
       res = ''.join(line).strip('\n').split(',')
       print('-------------------------------------')
       #print(res)
       if res != ['']:
         cursor.execute(sql_insert,[res[0], res[1], res[2],res[3], res[4], res[5], res[6], res[7], res[8], res[9], res[10], res[11], res[12], res[13], res[14]])

         print(i)
         print(res)
       i = i + 1

    conn.commit()
    cursor.close()
    conn.close()

print('=========================================================')

