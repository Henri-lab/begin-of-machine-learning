# 导入必要的库
import tensorflow as tf  # TensorFlow 是一个深度学习框架，用于构建和训练神经网络
from tensorflow.keras import datasets, layers, models  # Keras 是 TensorFlow 的高级 API，简化了神经网络的构建
import matplotlib.pyplot as plt  # 用于可视化图像和模型的预测结果

# 1. 加载 MNIST 数据集
# MNIST 是一个经典的手写数字图像数据集，包含 0-9 共 10 类数字，每个数字是 28x28 像素的灰度图
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

# 2. 预处理数据
# - 将每张图像从 2D 变成 3D，因为 CNN 期望输入的是多维数据（28x28 像素，1个颜色通道）。
# - 同时将像素值从 0-255 缩放到 0-1，这有助于加速模型的训练，使模型更容易收敛。

train_images = train_images.reshape((train_images.shape[0], 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1)).astype('float32') / 255

# 打印训练和测试图像的形状，确保数据已正确加载和预处理
print(f"Training images shape: {train_images.shape}")
print(f"Testing images shape: {test_images.shape}")

# 3. 构建卷积神经网络模型
# CNN 由多层组成，通常包括卷积层、池化层和全连接层。

model = models.Sequential([  # Sequential 表示模型是逐层线性堆叠的
    # 第一层：卷积层（Convolutional Layer）
    # - 输入是 28x28x1 的图像。
    # - 32 是卷积核的数量（也叫过滤器），每个卷积核大小为 3x3。
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    
    # 第二层：最大池化层（Max Pooling Layer）
    # - 池化层的作用是缩小特征图的尺寸，减少参数数量。
    # - 池化窗口大小为 2x2，即将 2x2 区域内的最大值作为输出。
    layers.MaxPooling2D((2, 2)),

    # 第三层：卷积层
    # - 使用 64 个卷积核，卷积核的大小仍然是 3x3。
    layers.Conv2D(64, (3, 3), activation='relu'),

    # 第四层：最大池化层
    layers.MaxPooling2D((2, 2)),

    # 第五层：卷积层
    layers.Conv2D(64, (3, 3), activation='relu'),

    # Flatten 层：将 3D 特征图展平成 1D 向量，准备传递给全连接层。
    layers.Flatten(),

    # 全连接层：有 64 个神经元，每个神经元与前一层所有的输出相连。
    layers.Dense(64, activation='relu'),

    # 输出层：10 个神经元，对应于 10 个分类（0-9）。
    # - softmax 激活函数将每个神经元的输出值归一化为概率（所有概率之和为 1）。
    layers.Dense(10, activation='softmax')
])

# 4. 编译模型
# - optimizer='adam'：Adam 是一种常用的优化算法，能帮助模型在训练时更快地找到最优参数。
# - loss='sparse_categorical_crossentropy'：适用于多分类问题，计算模型的预测与真实标签之间的差异。
# - metrics=['accuracy']：模型的性能指标是准确率，即预测正确的样本占总样本的比例。
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 5. 训练模型
# - epochs=5：模型将在整个训练集上训练 5 轮。
# - 训练过程会输出每一轮的损失值和准确率，以帮助你了解模型的训练进度。
model.fit(train_images, train_labels, epochs=5)

# 6. 评估模型
# - 在测试集上评估模型的性能，输出测试集上的损失值和准确率。
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(f'\nTest accuracy: {test_acc}')

# 7. 可视化模型预测
# 定义一个函数用于显示预测结果和真实标签
def plot_image_predictions(images, labels, predictions):
    plt.figure(figsize=(10, 10))  # 设置绘图窗口大小
    for i in range(25):  # 展示前 25 张图像
        plt.subplot(5, 5, i + 1)  # 将图像排列为 5x5 的网格
        plt.xticks([])  # 去掉 x 轴刻度
        plt.yticks([])  # 去掉 y 轴刻度
        plt.grid(False)  # 去掉网格线
        plt.imshow(images[i].reshape(28, 28), cmap=plt.cm.binary)  # 显示灰度图
        predicted_label = predictions[i].argmax()  # 获取预测结果中概率最大的标签
        true_label = labels[i]  # 获取真实标签
        color = 'blue' if predicted_label == true_label else 'red'  # 如果预测正确显示蓝色，错误则显示红色
        plt.xlabel(f'Pred: {predicted_label}, True: {true_label}', color=color)  # 标注预测和真实标签
    plt.show()

# 使用模型对测试集中的前 25 张图像进行预测
predictions = model.predict(test_images[:25])

# 显示预测结果和真实标签
plot_image_predictions(test_images[:25], test_labels[:25], predictions)