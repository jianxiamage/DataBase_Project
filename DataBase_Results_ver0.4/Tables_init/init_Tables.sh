#!/bin/bash

#-----------------------------------------------------
#初始化数据库中的表:
#-----------------------------------------------------

#初始化测试结果临时表
sh init_Tables_results.sh

#初始化测试结果临时表
sh init_Tables_TestResults.sh

#初始化性能跑分表
sh init_Tables_score.sh


