# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score

# # 1. 加载数据
# iris = load_iris()
# X = iris.data
# y = iris.target

# # 2. 划分训练集和测试集
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # 3. 训练模型
# clf = RandomForestClassifier(n_estimators=100, random_state=42)
# clf.fit(X_train, y_train)

# # 4. 预测并评估模型
# y_pred = clf.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)

# # 打印结果
# print(f"Model accuracy: {accuracy * 100:.2f}%")

