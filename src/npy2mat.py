import numpy as np
import scipy.io
import sys

# 确保输入和输出路径是从命令行参数获取的
if len(sys.argv) != 3:
    print("用法: python script.py <输入npy文件路径> <输出mat文件路径>")
    sys.exit(1)

# 获取输入和输出路径
npy_file = sys.argv[1]  # 从命令行获取输入文件路径
mat_file = sys.argv[2]  # 从命令行获取输出文件路径

# 读取 .npy 文件
try:
    data = np.load(npy_file)
except Exception as e:
    print(f"读取 .npy 文件时发生错误: {e}")
    sys.exit(1)

# 保存为 .mat 文件
try:
    scipy.io.savemat(mat_file, {'data': data})
    print(f"转换完成，文件保存在：{mat_file}")
except Exception as e:
    print(f"保存 .mat 文件时发生错误: {e}")
    sys.exit(1)
