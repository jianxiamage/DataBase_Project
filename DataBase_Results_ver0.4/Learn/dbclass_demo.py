#!/usr/bin/python
# -*- coding: UTF-8 -*-

from itertools import islice

import MySQLdb
import io


#------------------------------------------------------------------------------
#创建表结构
sql_create = '''
create table if not exists score_iozone(
  Tag varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  node_num varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `read` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `Re-reader` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `Random-Read` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `write` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `Re-writer` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  `Random-Write` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  PRIMARY KEY (node_num)
) CHARACTER SET utf8 COLLATE utf8_general_ci;
'''
#------------------------------------------------------------------------------
#读取csv文件插入表数据
sql_insert = '''
insert into score_iozone(Tag,node_num,`read`,`Re-reader`,`Random-Read`,`write`,`Re-writer`,`Random-Write`) values(%s, %s, %s, %s, %s, %s, %s, %s);
'''
#------------------------------------------------------------------------------

class MySQLDB():

    def __init__(self, host, port, user, passwd, db, charset):
        # 建立数据库连接
        self.conn = MySQLdb.connect(
            host=host,
            port=port,
            user=user,
            passwd=passwd,
            db=db,
            charset=charset
        )

        self.conn = MySQLdb.connect("localhost", "autotest", "loongson", "AutoTest", charset='utf8' )


        # 通过 cursor() 创建游标对象，并让查询结果以字典格式输出
        self.cur = self.conn.cursor()

    def __del__(self): # 对象资源被释放时触发，在对象即将被删除时的最后操作
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()

    def insertDataFromCSV_db(self, sql):
        """更新/插入/删除"""
        try:

            i=1
            with io.open('iozone.csv', mode= 'rt', encoding='utf-8') as file_handler:
                # 通过迭代器，遍历csv文件中的所有样本
                lines = file_handler.readlines()
                #使用islice的原因是跳过csv文件第一行
                for line in islice(lines, 1, None):
                   #res = ''.join(line).strip('\n').split(',')
                   res = ''.join(line).strip('\n').split(',')
                   print('-------------------------------------')
                   #print(res)
                   if res != ['']:
                     self.cur.execute(sql,[res[0], res[1], res[2],res[3], res[4], res[5], res[6], res[7]])
            
                     print(i)
                     print(res)
                   i = i + 1
            
                #conn.commit()
                #cursor.close()
                #conn.close()

            # 使用 execute() 执行sql
            #self.cur.execute(sql)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            print("操作出现错误：{}".format(e))
            # 回滚所有更改
            self.conn.rollback()

    def select_db(self, sql):
        """查询"""
        # 使用 execute() 执行sql
        self.cur.execute(sql)
        # 使用 fetchall() 获取查询结果
        data = self.cur.fetchall()
        return data

    def execute_db(self, sql):
        """更新/插入/删除"""
        try:
            # 使用 execute() 执行sql
            self.cur.execute(sql)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            print("操作出现错误：{}".format(e))
            # 回滚所有更改
            self.conn.rollback()

if __name__ == '__main__':

    db = MySQLDB("localhost", 3306, "autotest", "loongson", "AutoTest","utf8")


    select_sql = 'SELECT * FROM user WHERE username="张三2"'
    update_sql = 'UPDATE user SET username = "张三2" WHERE id = 1'
    insert_sql = 'INSERT INTO user(id, username, password) VALUES(11, "王五", "333333")'
    delete_sql = 'DELETE FROM user WHERE id = 11'

    #data = db.select_db(select_sql)
    #print(data)
    #db.execute_db(update_sql)
    #db.execute_db(insert_sql)
    #db.execute_db(delete_sql)
 
    trunc_sql = 'truncate table score_iozone'

    db.execute_db(sql_create)
    db.execute_db(trunc_sql)
    db.insertDataFromCSV_db(sql_insert)
