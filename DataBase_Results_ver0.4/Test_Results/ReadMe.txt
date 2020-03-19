说明:

一、基本表(Base)
测试用例作为基本表，需要提前做出来
1.测试用例分组表
  case_BaseGroupInfo
2.用例基本信息表
  case_BaseInfo
3.用例详细信息表
  case_DetailInfo

二、基本表(Base)
1.节点基本信息表
  表名:node_BaseInfo
  处理方法:
  node_BaseInfo_2csv.py
  node_BaseInfo.py
  
2.测试用例基本信息表
  表名:caseNode_BaseInfo
  处理方法:
  caseNode_BaseInfo.py

3.测试用例详细信息表
  表名:caseNode_DetailInfo
  处理方法:
  caseNode_DetailInfo.py

4.测试结果基本信息表
  表名:results_BaseInfo
  处理方法:
  results_BaseInfo.py

5.测试用例结果基本信息表
  表名:results_caseNode_BaseInfo
  处理方法:
  results_caseNode_BaseInfo.py

6.测试用例结果详细信息表
  表名:results_caseNode_DetailInfo
  处理方法:
  results_caseNode_DetailInfo.py

三、结果表
   
   根据前两个部分作为基础，形成了(二)中6的测试用例结果详细信息表
   results_caseNode_BaseInfo
   需要注意的是每个不同的平台及测试类型都有独自的表生成，
   因为最终形成的结果表需要进行多表联合拼接，所以它们作为中间临时表，不可缺少，
   但最终生成的表才是我们需要的总表

   分了两种情况，一个是基本表，一个是详细表
   暂命名为:TestResults_Table_Base_ALL
            TestResults_Table_Detail_ALL

