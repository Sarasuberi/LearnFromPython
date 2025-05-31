# Python Package索引
# 第三方库可以从PyPI来获得。PyPI社区是最大的Python仓库，是由Pyhone社区来维护的。
# PyPI中的所有Package都有版本号，如果需要获取这些Package，最好指定你需要的版本号。
# major.minor.patch
# major: 主版本号，通常是有重大变化时更新
# minor: 次版本号，通常是有新功能时更新
# patch: 修订号，通常是有bug修复时更新
# pip是Python的包管理工具，可以用来安装、升级和卸载Python包。
# 查看pip工具本身的版本号
# pip --version
# 查看pip工具的帮助信息
# pip --help
# 查看pip工具的配置信息
# pip config list
# 查看pip工具的安装源
# pip config get global.index-url
# 配置pip工具的默认镜像源
# pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/
# 升级pip到最新版本
# pip install --upgrade pip
# 安装Package
# pip install -i<仓库镜像的地址><package的名字>
# pip install requests
# 国内镜像源
# 清华：https://pypi.tuna.tsinghua.edu.cn/simple/
# 阿里：https://mirrors.aliyun.com/pypi/simple/
# 豆瓣：https://pypi.douban.com/simple/
# 中国科技大学：https://pypi.mirrors.ustc.edu.cn/simple/
# 华中科技大学：https://pypi.hustunique.com/
# 腾讯云：https://mirrors.cloud.tencent.com/pypi/simple
# 升级Package
# pip install --upgrade requests
# 安装指定版本的Package
# pip install <package的名字>==<version>
# pip install requests==2.25.1
# 卸载Package
# pip uninstall requests
# 查看已经安装的Package
# pip list
# 检查Package的是不是最新的
# pip list --outdated
# 查看已经安装的Package的详细信息
# pip show <package的名字>
# pip show requests

# 假设多个Python的项目需要同一个Package的不同版本，每个项目没有独立的环境就难以解决这个问题。
# 虚拟环境就是个独立的环境（文件夹）用于存放安装的Package和必须的Python的开发与运行工具。
# 安装venv工具
# pip install virtualenv
# python -m pip install --user virtualenv
# 创建虚拟环境
# python -m venv <虚拟环境的名字>
# python -m venv .venv
# 激活虚拟环境
# windows
# .venv\Scripts\activate
# macos/linux
# source .venv/bin/activate
# 查看虚拟环境是否激活
# which python
# 查看虚拟环境中的Package
# pip list
# 退出虚拟环境
# deactivate
# 删除虚拟环境
# rm -rf .venv

# 通过requirements.txt文件来管理Package
# requirements.txt文件是一个文本文件，用于记录项目所需的Package及其版本。
# 创建requirements.txt文件
# pip freeze > requirements.txt
# 查看requirements.txt文件的内容
# pip install -r requirements.txt
# 升级requirements.txt文件中的Package
# pip install -r requirements.txt --upgrade
# 强制重新安装requirements.txt文件中的Package
# pip install -r requirements.txt --upgrade --force-reinstall