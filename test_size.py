"""
用来测试 .npy 文件的大小 根据大小改变 主函数中的各种参数
"""

import numpy as np

arr = np.load('~/name.npy')
print(arr.shape)  # 输出 .npy 文件的大小
# print(arr)  # 直接输出 .npy 文件


