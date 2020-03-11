#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import islice

"""
Created on Tue Jul 10 22:06:43 2018
@author: User
"""
import io
 
input_file='UnixBench_1thread.csv'
list_data=[]
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
           print('-------------------------------------')
           print(type(res))
           list_data.append(res)
except Exception as e:
    print("操作出现错误：{}".format(e))
    # 回滚所有更改

#list_data.append(list_line)

print('============遍历list_line================')
for i in list_data:
    print i

print('========list_line[1]====================')
print(list_data[1][3])
