my_project/
├──.conda
├──.vscode
├── src/
│   ├── my_project_a/
│   │   ├── __init__.py     # 包初始化
│   │   ├── main.py         # 主模块
│   │   ├── config.py       # 配置管理模块
│   │   ├── utils.py        # 工具函数模块
│   │   ├── api.py          # 处理外部 API 的模块
│   │   ├── data/           # 数据模块
│   │   └── models/         # 机器学习模型或数据库模型
│   ├── tests/              # 测试目录
│   │   ├── test_main.py    # 测试主模块
│   │   └── test_utils.py   # 测试工具函数
│   ├── config/             # 配置文件目录
│   │   ├── settings.yaml   # 主配置文件
│   │   ├── db_config.json  # 数据库配置文件
│   └── data/               # 数据目录
│       ├── raw/            # 原始数据
│       └── processed/      # 处理过的数据
├── pyproject.toml          # Poetry 项目配置文件
├── README.md               # 项目说明
├── requirements.txt        # 依赖文件
└── .gitignore              # Git 忽略文件

'poetry env info --path' 查看依赖包路径
 如果你使用 Conda 来管理 Python 环境，而不是让 Poetry 创建自己的虚拟环境，那么项目的依赖将会安装到 Conda 的虚拟环境中 (.conda/site-packages)
