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

# pyinstaller工具
# pyinstaller工具可以将Python程序打包成可执行文件。
# 安装pyinstaller工具
# pip install pyinstaller
# 打包Python程序
# pyinstaller <python程序的路径>
# pyinstaller --onefile .\main.py --distpath .\dist --workpath .\build --specpath .\spec --clean --add-data .\data\*.txt;.data --add-binary .\data\*.png;.data --add-binary .\data\*.jpg;.data --add-binary .\data\*.exe;.data
# --onefile: 将所有文件打包成一个可执行文件
# --windowed: 不显示控制台窗口(GUI程序)
# --name: 指定输出文件名    None
# --icon: 指定可执行文件的图标，格式为<图标文件路径>    None
# --debug: 生成调试版本     None
# --distpath: 指定打包后的可执行文件的存放路径  None
# --workpath: 指定打包过程中的临时文件的存放路径    None
# --specpath: 指定打包过程中的spec文件的存放路径    None
# --clean: 清理打包过程中的临时文件 None
# --add-data: 指定需要打包的数据文件，格式为<源文件路径>:<目标文件路径>     None
# --add-binary: 指定需要打包的二进制文件，格式为<源文件路径>:<目标文件路径>     None
# --hidden-import: 指定需要导入的模块，格式为<模块名>   None
# --exclude-module: 指定需要排除的模块，格式为<模块名>  None
# --version-file: 指定可执行文件的版本信息，格式为<版本信息文件路径>    None
# --noconfirm: 不提示确认信息   None
# --noicon: 不显示图标  None

# 单元测试工具
# pip install nose
# pip install coverage
# 运行一个测试文件
# python3 -m unittest -v tests.basic.test_calculator
# 运行所有的测试文件
# nosetests -v tests/*
# 运行所有的测试文件并生成测试覆盖率报告
# nosetests --with-coverage --cover-erase -v tests/*
# 运行coverage工具
# coverage run --help

# Python标准库
# os: 提供了与操作系统交互的函数，如文件操作、目录操作、环境变量操作等
# sys: 提供了与Python解释器交互的函数，如命令行参数、标准输入输出等
# datetime: 提供了日期和时间相关的函数，如日期时间的创建、格式化、解析等
# time: 提供了时间相关的函数，如时间戳、时间间隔、时间格式化等
# json: 提供了JSON数据的解析和生成功能
# csv: 提供了CSV文件的读写功能
# re: 提供了正则表达式的匹配和替换功能
# hashlib: 提供了哈希算法的实现，如MD5、SHA1等
# file: 提供了文件操作的功能，如文件的打开、读取、写入等
# math: 提供了数学运算的功能，如三角函数、对数函数等
# random: 提供了随机数生成的功能

# 第三方库--网络爬虫
# requests: 用于发送HTTP请求的库
# beautifulsoup4: 用于解析HTML和XML的库
# selenium: 用于自动化测试的库
# scrapy: 用于爬虫的库
# urllib: 用于发送HTTP请求的库
# urllib3: 用于发送HTTP请求的库
# http.client: 用于发送HTTP请求的库
# http.server: 用于创建HTTP服务器的库
# socket: 用于网络编程的库
# ssl: 用于SSL/TLS加密的库

# 第三方库--科学运算基础模块
# numpy: 用于科学计算的库，支持大量的维度数组和矩阵运算。官方文档：https://numpy.org/doc/stable/reference/index.html#other-topics
# matplotlib: 专门用来绘图的工具包，用于数据可视化的库
# pandas: 数据分析工具包，基于numpy构建，纳入了大量的库和标准数据模型。官方文档：https://pandas.pydata.org/docs/reference/index.html#api
# scipy: 集成了数学、科学和工程学中常用的算法的库，它用于有效计算numpy矩阵使numpy和scipy协同工作

# 第三方库--机器学习
# scikit-learn: 机器学习库，基于numpy、scipy和matplotlib构建，提供了大量的机器学习算法和工具。有6搭基本功能：分类、回归、聚类、数据降维、模型选择和数据预处理。官方文档：https://scikit-learn.org/stable/modules/classes.html
# OpenCV: 计算机视觉库，提供了大量的计算机视觉算法和工具。如图像视频加载、基础特征获取、边检检测等处理图像通常都需要其支持。官方文档：https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
# NLTK: 自然语言处理库，提供了大量的自然语言处理算法和工具。官方文档：https://www.nltk.org/book/
# Gensim: 用于主题建模和文档相似性分析的工具包。官方文档：https://radimrehurek.com/gensim/models/ldamodel.html

# 第三方库--深度学习平台
# TensorFlow: Google开源的深度学习平台，支持多种深度学习算法和工具。相对成熟、应用广泛、服务全面、提供学习视频和其认证计划。官方文档：https://www.tensorflow.org/api_docs/python/tf
# PyTorch: Facebook开源的深度学习平台，支持多种深度学习算法和工具。支持更加快速地构建项目。官方文档：https://pytorch.org/docs/stable/index.html
# Keras: 高级神经网络API，用于快速构建和训练深度学习模型。官方文档：https://keras.io/api/
# MXNet: Apache开源的深度学习平台，支持多种深度学习算法和工具。官方文档：https://mxnet.apache.org/api/python/docs/api/index.html
# PaddlePaddle: 百度开源的深度学习平台，支持多种深度学习算法和工具。中文文档全面，对于汉语的相关模型比较丰富。官方文档：https://www.paddlepaddle.org.cn/documentation/docs/zh/develop/api/index_cn.html


# 第三方库--Web开发
# Django: 一个高级的Web框架，用于快速开发Web应用和网站。官方文档：https://docs.djangoproject.com/zh-hans/3.2/
# Flask: 一个轻量级的Web框架，用于快速开发Web应用和网站。官方文档：https://flask.palletsprojects.com/en/2.0.x/
# Tornado: 一个异步Web框架，用于开发高性能的Web应用和网站。官方文档：https://www.tornadoweb.org/en/stable/