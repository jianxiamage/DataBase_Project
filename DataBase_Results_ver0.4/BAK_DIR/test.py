#!/usr/bin/python
# -*- coding: UTF-8 -*-

from itertools import islice 

import MySQLdb
import io

# 打开数据库连接
conn = MySQLdb.connect("localhost", "autotest", "loongson", "AutoTest", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = conn.cursor()

sql_create = '''
create table if not exists bid_info  (node_ip varchar(60), node_num varchar(60),group_num varchar(60));
'''
cursor.execute(sql_create)
cursor.execute('truncate  bid_info;')
sql_insert = '''
insert into bid_info value(%s, %s, %s);
'''

i=0
with io.open('node_info.csv', mode= 'rt', encoding='utf-8') as file_handler:
    # 通过迭代器，遍历csv文件中的所有样本
    lines = file_handler.readlines()
    #使用islice的原因是跳过csv文件第一行
    for line in islice(lines, 1, None): 
       #res = ''.join(line).strip('\n').split(',')
       res = ''.join(line).strip('\n').split(',')
       print('-------------------------------------')
       print(res)
       if res != ['']:
         cursor.execute(sql_insert,[res[0], res[1], res[2]])
         print(i)
         #print(res)
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
