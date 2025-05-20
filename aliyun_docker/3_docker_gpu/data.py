import numpy as np
import os

# 创建数据目录
data_dir = './tcdata'
os.makedirs(data_dir, exist_ok=True)

# 创建一个简单的 NumPy 数组
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 将数组保存为 a.npy 文件
a_path = os.path.join(data_dir, 'b.npy')
np.save(a_path, a)

print(f"文件已创建: {a_path}")