本版本介绍:
主要实现了测试用例程序写入数据库的方法
包含测试平台，测试类型等输入参数
本版本除了加入了封装类操作数据库的方法,还将表名作为变量
本版本已将程序模块化，分为跑分程序和结果程序:
Perform_Score
Test_Results

1.参考网址：
  https://blog.csdn.net/weixin_42983055/article/details/88245954

2.通过PYTHON 将CSV 文件导入到MySQL 数据库
  readIni.py  //主要是将ini文件转换为csv文件
              //这里调研了一些专门的csv库来转换的方法，但选择了最简单的变量写入方式
              //因为含有编码问题，尚需进一步确认



