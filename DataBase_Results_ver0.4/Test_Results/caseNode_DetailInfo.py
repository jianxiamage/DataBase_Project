#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
程序说明:
制作数据表:节点与测试用例详细信息表
           将节点信息表与测试用例详细信息表合并
"""

import sys
import os
import traceback

from itertools import islice

import MySQLdb
import io

#------------------------------------------
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


    def insertData_db(self, table_name, list_data):
        """更新/插入/删除"""
        try:

            i=1
            for line in list_data:
                 sql = '''
                 insert into %s(Tag,case_name,node_num,value)
                 values('%s','%s', '%s', '%s')
                 '''  % (table_name,line[0],line[1],line[2],line[3])
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
        test_Tag = sys.argv[3]
    
        #---------------------------------------------------------------------
        #创建数据表
        table_name = 'caseNode_DetailInfo_' + test_Tag
        table_nodeBase = 'node_BaseInfo_' + test_Tag


        drop_sql = 'drop table if exists %s' %(table_name)
        db.execute_db(drop_sql)

        #create table if not exists %s (id int primary key auto_increment) 
        sql_create = '''
        create table if not exists %s (id int primary key auto_increment) 
        as select 
        case_DetailInfo.case_name,case_DetailInfo.case_alias,case_DetailInfo.case_detail,%s.node_num,%s.IP,case_DetailInfo.group_num 
        from  case_DetailInfo right join %s on case_DetailInfo.group_num = %s.group_num;
        ''' %(table_name,table_nodeBase,table_nodeBase,table_nodeBase,table_nodeBase)
        #---------------------------------------------------------------------
        db.execute_db(sql_create)
        #---------------------------------------------------------------------

        #------------------------------------------------------------------------------
        #sql_dropID = "ALTER TABLE %s DROP column id" %(table_name)
        #db.execute_db(sql_dropID)
        #sql_addID = "ALTER TABLE %s ADD id int first" %(table_name)
        #db.execute_db(sql_addID)
        #sql_addIDAttr = "ALTER TABLE %s change id id int NOT NULL AUTO_INCREMENT primary key" %(table_name)
        #db.execute_db(sql_addIDAttr)
        #------------------------------------------------------------------------------

        #---------------------------------------------------------------------
        #清空数据表
        #trunc_sql = 'truncate table score_UnixBench_1thread'
        #sql_delete = "delete from %s where Tag ='%s'" %(table_name, test_Tag)
        #---------------------------------------------------------------------
 
        #---------------------------------------------------------------------
        #print('清理旧数据,准备重新插入...')
        #db.execute_db(trunc_sql)
        #db.execute_db(sql_delete)

        #------------------------------------------------------------------------------
        #在删除数据后，会造成表中的自增字段序号不连续，
        #解决方法是truancate或创建临时表备份后重新创建新表,但都缺点明显
        #因此以下操作是先将id删除，再重新加入
        #------------------------------------------------------------------------------
        #sql_dropID = "ALTER TABLE %s DROP column id" %(table_name)
        #db.execute_db(sql_dropID)
        #sql_addID = "ALTER TABLE %s ADD id int first" %(table_name)
        #db.execute_db(sql_addID)
        #sql_addIDAttr = "ALTER TABLE %s change id id int NOT NULL AUTO_INCREMENT primary key" %(table_name)
        #db.execute_db(sql_addIDAttr)
        #------------------------------------------------------------------------------

        #------------------------------------------------------------------------------
        #新的方法:

        #print('插入数据开始...')
        #db.insertData_db(table_name,list_data)
        #print('插入数据完成.')

    except Exception as E:
        #print('str(Exception):', str(Exception))
        print('str(e):', str(E))
        #print('repr(e):', repr(E))
        #print('traceback.print_exc(): ', traceback.print_exc())
        sys.exit(1)
