#!/usr/bin/python
# -*- coding: UTF-8 -*-

from itertools import islice 

import MySQLdb
import io

# 打开数据库连接
conn = MySQLdb.connect("localhost", "autotest", "loongson", "AutoTest", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = conn.cursor()

#--------------------------------------------------------------------
sql_create = '''
create table if not exists score_UnixBench_16thread(
id int(10) auto_increment,
node_num  varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci,
test_option varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci,
ref_data varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci,
score varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
PRIMARY key(id)
)CHARACTER SET utf8 COLLATE utf8_general_ci;
'''
#--------------------------------------------------------------------

cursor.execute(sql_create)
cursor.execute('truncate table score_UnixBench_16thread;')
sql_insert = '''
insert into score_UnixBench_16thread(node_num,test_option,ref_data,score) values(%s, %s, %s, %s);
'''

i=1
with io.open('UnixBench_16thread.csv', mode= 'rt', encoding='utf-8') as file_handler:
    # 通过迭代器，遍历csv文件中的所有样本
    lines = file_handler.readlines()
    #使用islice的原因是跳过csv文件第一行
    for line in islice(lines, 1, None): 
       #res = ''.join(line).strip('\n').split(',')
       res = ''.join(line).strip('\n').split(',')
       print('-------------------------------------')
       #print(res)
       if res != ['']:
         cursor.execute(sql_insert,[res[0], res[1], res[2], res[3]])

         print(i)
         print(res)
       i = i + 1

    conn.commit()
    cursor.close()
    conn.close()

print('=========================================================')

#i=0
##with open('t.csv', mode= 'rt', encoding='GBK') as f:
#with io.open('node_info.csv', mode= 'rt', encoding='utf-8') as f:
#    while f.readline():
#        res = f.readline().strip().split(',')
#        print(res)
#        if res != ['']:
#            cursor.execute(sql_insert,[res[0], res[1], res[2]])
#            print('------------------')
#            print(res)
#            print('------------------')
#    conn.commit()
#    cursor.close()
#    conn.close()
