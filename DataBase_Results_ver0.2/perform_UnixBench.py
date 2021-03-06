#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
程序说明:
其中关于从csv文件中获取数据，并存入数据库的方法，现已修正为从csv文件中读入到list，
再从list中依此循环写入数据库中，
原来的逻辑是:直接从csv文件读取数据写入数据库，对于表名是变量的情况不方便处理
"""

import sys
import os
import traceback

from itertools import islice

import MySQLdb
import io

#------------------------------------------
ResultPath='/data/'
detailDir='Detail'
PointsPath='Points_Files'
#------------------------------------------

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

    def get_data_from_csv(self, input_file, list_data=[]):
        """生成csv文件,准备写入数据库"""
        try:

            i=1
            with io.open(input_file, mode= 'rt', encoding='utf-8') as file_handler:
                # 通过迭代器，遍历csv文件中的所有样本
                lines = file_handler.readlines()
                #使用islice的原因是跳过csv文件第一行
                for line in islice(lines, 1, None):
                   #res = ''.join(line).strip('\n').split(',')
                   res = ''.join(line).strip('\n').split(',')
                   #print('-------------------------------------')
                   #print(res)
                   list_data.append(res)
        except Exception as e:
            print("操作出现错误：{}".format(e))
            # 回滚所有更改


    def insertData_db(self, table_name, list_data):
        """更新/插入/删除"""
        try:

            i=1
            for line in list_data:
                 #self.cur.execute(sql,[res[0], res[1], res[2],res[3], res[4]])
                 sql = '''
                 insert into %s(Tag,node_num,test_option,ref_data,score) values('%s','%s', '%s', '%s', '%s')
                 '''  % (table_name,line[0],line[1],line[2],line[3],line[4])
                 self.cur.execute(sql)
                 #print('=====================================================')
                 #print(i)
                 i = i + 1
            
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

    try:

        test_type = sys.argv[1]
        test_platform = sys.argv[2]
        test_case = sys.argv[3]
        test_Tag = sys.argv[4]
    
        #---------------------------------------------------------------------
        #拼接目标文件名
        caseDir='UnixBench'
        ResultIniPath = ResultPath + str(test_type) + '/' + str(test_platform) + '/' + str(detailDir) + '/' + str(caseDir) + '/' + str(PointsPath)
        csvFileName = ResultIniPath + '/' + test_case +'.csv'
        #---------------------------------------------------------------------
    
        #---------------------------------------------------------------------
        table_name = 'score_' + test_case
        sql_create = '''
        create table if not exists %s
        (
          id int(10) NOT NULL AUTO_INCREMENT,
          Tag varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
          node_num varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
          test_option varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci,
          ref_data varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci,
          score varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
          PRIMARY KEY (id)
        ) CHARACTER SET utf8 COLLATE utf8_general_ci;
        ''' %(table_name)
        #---------------------------------------------------------------------

        #---------------------------------------------------------------------
        #清空数据表
        #trunc_sql = 'truncate table score_UnixBench_1thread'
        sql_delete = "delete from %s where Tag ='%s'" %(table_name, test_Tag)
        #---------------------------------------------------------------------
 
        #------------------------------------------------------------------------------
        #读取csv文件插入表数据
        #sql_insert = '''
        #insert into score_UnixBench_1thread(Tag,node_num,test_option,ref_data,score) values(%s, %s, %s, %s, %s);
        #'''
        #------------------------------------------------------------------------------

        list_data=[]
        db.get_data_from_csv(csvFileName,list_data)
        print list_data[1][4]

        db.execute_db(sql_create)
        
        print('清理旧数据,准备重新插入...')
        #db.execute_db(trunc_sql)
        db.execute_db(sql_delete)

        print('插入数据开始...')
        db.insertData_db(table_name,list_data)
        print('插入数据完成.')

    except Exception as E:
        #print('str(Exception):', str(Exception))
        print('str(e):', str(E))
        #print('repr(e):', repr(E))
        #print('traceback.print_exc(): ', traceback.print_exc())
        sys.exit(1)
