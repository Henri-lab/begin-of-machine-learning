#!/bin/bash
# chmod +x init.sh

# 定义项目根目录名称
PROJECT_NAME="crawler_project"

# 创建项目根目录
mkdir -p $PROJECT_NAME

# 创建数据目录和子目录
mkdir -p $PROJECT_NAME/data/raw
mkdir -p $PROJECT_NAME/data/processed
mkdir -p $PROJECT_NAME/data/logs
mkdir -p $PROJECT_NAME/data/output

# 创建源代码目录
mkdir -p $PROJECT_NAME/src
mkdir -p $PROJECT_NAME/src/spiders        # 存放爬虫代码
mkdir -p $PROJECT_NAME/src/utils          # 存放工具模块

# 创建配置和其他辅助目录
mkdir -p $PROJECT_NAME/config             # 配置文件目录
mkdir -p $PROJECT_NAME/tests              # 单元测试目录

# 创建 README 和 .gitignore 文件
echo "# $PROJECT_NAME" > $PROJECT_NAME/README.md
echo "__pycache__/" > $PROJECT_NAME/.gitignore
echo "data/raw/" >> $PROJECT_NAME/.gitignore
echo "data/processed/" >> $PROJECT_NAME/.gitignore
echo "data/output/" >> $PROJECT_NAME/.gitignore
echo "data/logs/" >> $PROJECT_NAME/.gitignore

# 创建 __init__.py 文件
touch $PROJECT_NAME/src/__init__.py
touch $PROJECT_NAME/src/spiders/__init__.py
touch $PROJECT_NAME/src/utils/__init__.py
touch $PROJECT_NAME/tests/__init__.py
touch $PROJECT_NAME/config/__init__.py

#创建常用文件
touch $PROJECT_NAME/src/utils/html_parser.py
touch $PROJECT_NAME/src/utils/db_connecter.py
touch $PROJECT_NAME/src/utils/data_cleaner.py


# 创建入口文件
cat <<EOL > $PROJECT_NAME/src/main.py
from spiders import main_spider

if __name__ == "__main__":
    url = "https://example.com"
    spider = main_spider.MainSpider(url)
    html = spider.fetch()
    if html:
        parsed_data = spider.parse(html)
        print(parsed_data)
EOL



# 创建初始爬虫代码文件
cat <<EOL > $PROJECT_NAME/src/spiders/main_spider.py
import requests
from bs4 import BeautifulSoup

class MainSpider:
    def __init__(self, start_url):
        self.start_url = start_url

    def fetch(self):
        response = requests.get(self.start_url)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Failed to fetch {self.start_url}")
            return None

    def parse(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        # 这里根据需要编写解析逻辑
        return soup

if __name__ == "__main__":
    url = "https://example.com"
    spider = MainSpider(url)
    html = spider.fetch()
    if html:
        parsed_data = spider.parse(html)
        print(parsed_data)
EOL

# 创建实用工具模块
cat <<EOL > $PROJECT_NAME/src/utils/file_helpers.py
def save_to_file(content, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def load_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
EOL

# 创建测试文件
cat <<EOL > $PROJECT_NAME/tests/test_spider.py
import unittest
from src.spiders.main_spider import MainSpider

class TestMainSpider(unittest.TestCase):

    def test_fetch(self):
        spider = MainSpider("https://example.com")
        content = spider.fetch()
        self.assertIsNotNone(content)

if __name__ == "__main__":
    unittest.main()
EOL

# 创建简单的配置文件
cat <<EOL > $PROJECT_NAME/config/settings.py
# 配置文件示例
USER_AGENT = "MyCrawlerBot/1.0"
TIMEOUT = 5  # seconds
EOL

echo "Project directory and basic files for '$PROJECT_NAME' created successfully!"
