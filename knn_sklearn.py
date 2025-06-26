# KNN算法：近朱者赤，近墨者黑
# 找到K个与新数据最近的样本，然后看这K个样本中哪个类别的样本多，新数据就属于哪个类别
# 算法优点：1.简单易懂，容易实现
#          2.对于边界不规则的数据效果较好
# 算法缺点：1.只适合小数据集
#          2.计算量大，需要计算新数据与所有样本的距离
#          3.对于样本不均衡的情况，可能会偏向样本多的类别
#          4.必须要做数据标准化处理
#          5.不适合特征维度太多的数据
# K值的选取会影响到模型的效果，K值太小，容易受到噪声的影响，K值太大，容易受到离群点的影响
# K值越小越容易过拟合，K值越大越容易欠拟合，合适的K值需要根据经验和效果去进行尝试

from sklearn import datasets    # sklearn的数据集
from sklearn.neighbors import KNeighborsClassifier  #sklearn模块的knn类
import numpy as np

# 设置随机种子，不设置的话默认是按系统时间作为参数，设置后可以保证我们每次产生的随机数是一样的
np.random.seed(0)

iris = datasets.load_iris()  # 加载鸢尾花数据集
# print(iris.data)  # 打印数据部分
# print(iris.target)  # 打印类别部分
iris_x = iris.data
iris_y = iris.target

# 从150条数据中选140条作为训练集，10条作为测试集。permutation接收一个数作为参数（这里为数据集长度150），产生一个0-149乱序一维数组
randomarr = np.random.permutation(len(iris_x))

iris_x_train = iris_x[randomarr[:-10]]  # 选取前140条数据作为训练集
iris_y_train = iris_y[randomarr[:-10]]  # 选取前140条类别作为训练集
iris_x_test = iris_x[randomarr[-10:]]   # 选取后10条数据作为测试集
iris_y_test = iris_y[randomarr[-10:]]    # 选取后10条类别作为测试集

# 定义一个knn分类器对象
knn = KNeighborsClassifier()

# 调用该对象的训练方法，主要接收两个参数：训练数据集及其类别标签
knn.fit(iris_x_train, iris_y_train)

# 调用预测方法，主要接收一个参数：测试数据集
iris_y_predict = knn.predict(iris_x_test)

#计算各测试样本预测的概率值，这里我们没有用概率值，但是实际工作中可能会参考概率值来进行最后结果的筛选，而不是直接使用给出的预测标签
probility = knn.predict_proba(iris_x_test)

# 计算与最后一个测试样本距离最近的5个点，返回的是这些样本的序号组成的数组
neighborpoint = knn.kneighbors([iris_x_test[-1]],5)

# 调用该对象的打分方法，计算出准确率
score = knn.score(iris_x_test, iris_y_test,sample_weight=None)

# 输出测试结果
print(f"iris_y_predict = {iris_y_predict}")

# 输出原始测试数据集的正确标签，以方便对比
print(f"iris_y_test = {iris_y_test}")

# 输出测试集的准确率
print(f"score = {score}")