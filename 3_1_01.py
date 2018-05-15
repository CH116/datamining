from sklearn.datasets import load_iris
from sklearn import tree
import graphviz

iris = load_iris()  # 加载数据
# 参数含义：criterion='entropy'基于熵的；min_impurity_split=0.05纯度至少为95%；max_leaf_nodes=5结点小于等于5则停止
CTree = tree.DecisionTreeClassifier(criterion='entropy',  min_impurity_split=0.05, max_leaf_nodes=5)
# 参数含义：iris.data为要预测的数据；iris.target为数据的分类（训练模型）
CTree = CTree.fit(iris.data, iris.target)
# 将生成的树的信息导成DOT格式保存
dot_data = tree.export_graphviz(CTree, out_file=None,
                                feature_names=iris.feature_names,
                                class_names=iris.target_names,
                                filled=True, rounded=True,
                                special_characters=True)
# 将保存的DOT文件可视化
graph = graphviz.Source(dot_data)
# 生成PDF文件
graph.render("myiris")
