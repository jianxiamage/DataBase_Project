关于数据库表的初始化策略：

init_Tables_results.sh     //删除测试结果中间临时生成的各个表(以results开头)
init_Tables_TestResults.sh //删除当前一轮测试结果总表(以TestResults开头)
init_Tables_score.sh       //删除性能跑分数据表(以score开头)

init_Tables.sh             //删除除备份表之外的所有当前表，用于每轮测试初始化时使用
init_Tables_Bak.sh         //删除备份数据表,基本只用于调试(以Bak_开头)

#批量删除数据表直接操作命令参考
Debug_init_Tables.sh      //关于删除一切表的脚本，只用于手工参考，不会实际执行
init_DB_NoParas.sh        //只是将有关测试结果中间临时数据表进行删除,用于手工操作参考
