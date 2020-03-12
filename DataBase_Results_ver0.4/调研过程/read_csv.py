#!/usr/bin/python
# -*- coding: UTF-8 -*-

import io

import csv
# 先打开文件，file_handler为打开的文件的句柄
with io.open('demo.csv', 'r', encoding='utf-8') as file_handler:
	# 返回csv迭代器file_reader，用于迭代得到样本
    file_reader = csv.reader(file_handler)
    # print(type(file_reader))
	# 通过迭代器，遍历csv文件中的所有样本
    for sample in file_reader:
        print(sample)
