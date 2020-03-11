#!/usr/bin/python
# -*- coding: UTF-8 -*-

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

#------------------------------------------------------------------------------
#创建表结构
sql_create = '''
create table if not exists score_spec2006_1core_CFP(
  id int(10) NOT NULL AUTO_INCREMENT,
  Tag varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  node_num varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
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
  SPECfp_base2006 varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
  PRIMARY KEY (id)
) CHARACTER SET utf8 COLLATE utf8_general_ci;
'''
#------------------------------------------------------------------------------
#读取csv文件插入表数据
sql_insert = '''
insert into score_spec2006_1core_CFP(Tag,node_num,`410.bwaves`,`416.gamess`,`433.milc`,`434.zeusmp`,`435.gromacs`,`436.cactusADM`,`437.leslie3d`,`444.namd`,`447.dealII`,`450.soplex`,`453.povray`,`454.calculix`,`459.GemsFDTD`,`465.tonto`,`470.lbm`,`481.wrf`,`482.sphinx3`,SPECfp_base2006) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
'''
#------------------------------------------------------------------------------
trunc_sql = 'truncate table score_spec2006_1core_CFP'
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

    def insertDataFromCSV_db(self, sql, input_file):
        """更新/插入/删除"""
        try:

            i=1
            with io.open(input_file, mode= 'rt', encoding='utf-8') as file_handler:
                # 通过迭代器，遍历csv文件中的所有样本
                lines = file_handler.readlines()
                #使用islice的原因是跳过csv文件第一行
                for line in islice(lines, 1, None):
                   #res = ''.join(line).strip('\n').split(',')
                   res = ''.join(line).strip('\n').split(',')
                   print('-------------------------------------')
                   #print(res)
                   if res != ['']:
                     self.cur.execute(sql,[res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7],res[8],res[9],res[10],res[11],res[12],res[13],res[14],res[15],res[16],res[17],res[18],res[19]])
            
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

    try:

        test_type = sys.argv[1]
        test_platform = sys.argv[2]
        test_case = sys.argv[3]
        test_Tag = sys.argv[4]
    
        #---------------------------------
        #拼接目标文件名
        caseDir='spec2006-1core'
        ResultIniPath = ResultPath + str(test_type) + '/' + str(test_platform) + '/' + str(detailDir) + '/' + str(caseDir) + '/' + str(PointsPath)
        csvFileName = ResultIniPath + '/' + test_case +'.csv'
        #---------------------------------
    
        #trunc_sql = 'truncate table score_spec2006_1core_CFP'
        sql_delete = "delete from score_spec2006_1core_CFP where Tag ='%s'" %(test_Tag)

    
        db.execute_db(sql_create)
        #db.execute_db(trunc_sql)
        db.execute_db(sql_delete)
        db.insertDataFromCSV_db(sql_insert,csvFileName)

    except Exception as E:
        #print('str(Exception):', str(Exception))
        print('str(e):', str(E))
        #print('repr(e):', repr(E))
        #print('traceback.print_exc(): ', traceback.print_exc())
        sys.exit(1)
