#   1.	最简单的形式：空文件，标识为包。
# 	2.	导入包中的模块：通过 __init__.py 导入包中的模块，简化导入路径。
# 	3.	定义公共 API：控制用户导入包时可以访问的函数或类。
# 	4.	包初始化：执行一些包加载时的初始化逻辑。
# 	5.	控制 import * 行为：通过 __all__ 控制导入时暴露的内容。
# 	6.	设置包元数据：比如版本号、作者信息等
