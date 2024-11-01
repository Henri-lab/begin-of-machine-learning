#!/bin/bash
chmod +x ./conda.sh
# 获取用户输入的环境名称
read -p "请输入要创建的 Conda 环境名称: " ENV_NAME

# 检查环境名称是否为空
if [ -z "$ENV_NAME" ]; then
    echo "环境名称不能为空！请重新运行脚本并输入有效的名称。"
    exit 1
fi

# 检查环境是否已经存在
if conda env list | grep -q "^$ENV_NAME\s"; then
    echo "Conda 环境 '$ENV_NAME' 已经存在。"

    # 提示用户是否覆盖已有环境
    read -p "是否覆盖已有环境？(y/n): " answer
    if [ "$answer" = "y" ] || [ "$answer" = "Y" ]; then
        echo "正在删除旧的 Conda 环境 '$ENV_NAME'..."
        conda remove --name "$ENV_NAME" --all -y
        echo "旧环境已删除，正在创建新的 Conda 环境（3.10） '$ENV_NAME'..."
        conda create --name "$ENV_NAME" python=3.10 -y
        # 安装基础爬虫工具
        conda install scrapy selenium beautifulsoup4 requests lxml pandas sqlalchemy pymongo redis-py 
    else
        echo "保留已有环境，不进行操作。"
    fi
else
    # 创建新的 Conda 环境
    echo "Conda 环境 '$ENV_NAME' 不存在，正在创建..."
    conda create --name "$ENV_NAME" python=3.10 -y
fi

# 激活环境
conda activate "$ENV_NAME"
echo "Conda 环境 '$ENV_NAME' 已激活。"

# 询问是否安装额外的包
read -p "是否要安装额外的包？(y/n): " install_packages
if [ "$install_packages" = "y" ] || [ "$install_packages" = "Y" ]; then
    # 提示用户输入包名
    read -p "请输入要安装的包名（用空格分隔多个包）： " package_names

    # 检查是否输入了包名
    if [ -n "$package_names" ]; then
        echo "正在安装包: $package_names"
        conda install $package_names -y
    else
        echo "未输入包名，跳过安装。"
    fi
else
    echo "不安装额外的包。"
fi

echo "设置完成！"

conda activate "$ENV_NAME"
conda env export > environment.yml  # conda env export --from-history > environment.yml 不指定版本