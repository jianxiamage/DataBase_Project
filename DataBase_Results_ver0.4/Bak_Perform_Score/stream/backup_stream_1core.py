#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
程序说明:
制作数据表:用例测试结果详细信息表
           存储测试用例详细信息表与结果基本信息表连接
"""

import sys
import os
import traceback
import re

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


    def insertData_db(self, table_name):
        """更新/插入/删除"""
        try:

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

    #-----------------------------------------------------------------------
    #判断表是否存在
    #-----------------------------------------------------------------------
    def table_exists(self,table_name):        #这个函数用来判断表是否存在
        sql = "show tables;"
        self.cur.execute(sql)
        tables = [self.cur.fetchall()]
        table_list = re.findall('(\'.*?\')',str(tables))
        table_list = [re.sub("'",'',each) for each in table_list]
        if table_name in table_list:
            return 1        #存在返回1
        else:
            return 0        #不存在返回0

    def drop_ID(self, table_name):
        """删除自增id，重新加入，重新排序"""
        try:

            sql_dropID = "ALTER TABLE `%s` DROP column id" %(table_name)
            self.cur.execute(sql_dropID)
            sql_addID = "ALTER TABLE `%s` ADD id int first" %(table_name)
            self.cur.execute(sql_addID)
            sql_addIDAttr = "ALTER TABLE `%s` change id id int NOT NULL AUTO_INCREMENT primary key" %(table_name)
            self.cur.execute(sql_addIDAttr)

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
        test_case = sys.argv[4]
        test_Ver = sys.argv[5]

        #为避免表名过长，删除版本号码末尾的.mips64el
        tbl_header = test_Ver.strip('.mips64el')
        print("表头[%s]") %(tbl_header)
        #sys.exit(1)
        #---------------------------------------------------------------------
        #创建数据表
        table_name = 'Bak_' + test_case + '_' + tbl_header
        table_score_case = 'score_' + test_case
        #---------------------------------------------------------------------

        #---------------------------------------------------------------------
        if(db.table_exists(table_score_case) != 1):
            print("表[%s]尚未生成,程序退出!") %(table_score_case)
            db.drop_ID(table_name)
            sys.exit(1)
        else:
            print("表[%s]已生成") %(table_score_case)
        #---------------------------------------------------------------------

        #---------------------------------------------------------------------
        #如果不存在表:Results_Table_Base_ALL,则创建表，并将相应表数据插入
        sql_create = '''
        create table if not exists `%s` (id int primary key auto_increment) 
        as
        select * from %s where Tag ='%s'
        ''' %(table_name,table_score_case,test_Tag)

        if(db.table_exists(table_name) != 1):
            print("表[%s]不存在,需要新建") %(table_name)
            db.execute_db(sql_create)
            sys.exit(0)
        else:
            print("表[%s]已存在") %(table_name)

        #sys.exit(1)

        #---------------------------------------------------------------------
        #如果存在表:Results_Table_Base_ALL,则清空数据表，并将相应表数据插入
        #---------------------------------------------------------------------
        #清空数据表
        sql_delete = "delete from `%s` where Tag ='%s'" %(table_name, test_Tag)
        print('清理旧数据,准备重新插入...')
        db.execute_db(sql_delete)
        #---------------------------------------------------------------------

        #------------------------------------------------------------------------------
        #检查临时表是否存在并删除
        Tmp_Table = 'Tmp_' + table_score_case
        #---------------------------------------------------------------------
        print('检查临时表是否存在并删除')
        sql_dropTmp = "DROP TABLE IF EXISTS %s" %(Tmp_Table)
        db.execute_db(sql_dropTmp)

        #------------------------------------------------------------------------------
        #创建临时表
        print('开始创建临时表...')
        sql_createTmp = '''
        create table if not exists %s
        as
        select Tag,node_num,Copy,Scale,`Add`,Triad from %s where Tag ='%s';
        ''' %(Tmp_Table,table_score_case,test_Tag)

        db.execute_db(sql_createTmp)
        print('创建临时表结束.')
        #------------------------------------------------------------------------------

        #------------------------------------------------------------------------------
        print('将临时表数据插入大表...')
        #------------------------------------------------------------------------------
        sql_insert = '''
        insert into `%s`(Tag,node_num,Copy,Scale,`Add`,Triad)
        select * from %s
        ''' %(table_name,Tmp_Table)
        #---------------------------------------------------------------------
        db.execute_db(sql_insert)

        #---------------------------------------------------------------------
        print('开始删除总表id并重新排序后恢复...')
        #---------------------------------------------------------------------
        #在删除数据后，会造成表中的自增字段序号不连续，
        #解决方法是truancate或创建临时表备份后重新创建新表,但都缺点明显
        #因此以下操作是先将id删除，再重新加入
        #------------------------------------------------------------------------------
        db.drop_ID(table_name)
        #------------------------------------------------------------------------------

        #---------------------------------------------------------------------
        print('删除临时表')
        sql_dropTmp = "DROP TABLE IF EXISTS %s" %(Tmp_Table)
        db.execute_db(sql_dropTmp)
        #---------------------------------------------------------------------

    except Exception as E:
        #print('str(Exception):', str(Exception))
        print('str(e):', str(E))
        #print('repr(e):', repr(E))
        #print('traceback.print_exc(): ', traceback.print_exc())
        sys.exit(1)
