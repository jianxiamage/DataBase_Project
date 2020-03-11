#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import io

# 打开数据库连接
conn = MySQLdb.connect("localhost", "autotest", "loongson", "AutoTest", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = conn.cursor()

sql_create = '''
create table if not exists bid  (bid varchar(225), bid_type int);
'''
cursor.execute(sql_create)
cursor.execute('truncate  bid;')
sql_insert = '''
insert into bid value(%s, %s);
'''

#with open('t.csv', mode= 'rt', encoding='GBK') as f:
with io.open('t.csv', mode= 'rt', encoding='utf-8') as f:
    while f.readline():
        res = f.readline().strip('\n').split(',')
        if res != ['']:
            cursor.execute(sql_insert,[res[0], res[1]])
            print(res)
    conn.commit()
    cursor.close()
    conn.close()
