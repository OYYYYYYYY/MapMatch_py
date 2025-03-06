import numpy as np
import sys
import csv

def load_csv_to_dense(csv_filename, order, dimensions):
    # 创建稠密矩阵，初始全为0
    dense_matrix = np.zeros(dimensions)

    # 读取CSV文件中的四元组，并填充稠密矩阵
    with open(csv_filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # 跳过表头
        for row in reader:
            indices = tuple(int(row[i]) for i in range(order))  # 获取索引
            value = float(row[order])  # 获取值
            dense_matrix[indices] = value  # 将值放入对应位置
            
    return dense_matrix

def main():
    # 获取命令行参数，确保用户提供了输入文件名、输出文件名、秩和维度信息
    if len(sys.argv) != 7:
        print("用法: python script.py <输入文件名.csv> <输出文件名.npy> <秩> <维度1> <维度2> <维度3>")
        sys.exit(1)

    csv_filename = sys.argv[1]  # 第一个参数为输入文件名
    output_filename = sys.argv[2]  # 第二个参数为输出文件名
    order = int(sys.argv[3])  # 第三个参数为秩
    dim1 = int(sys.argv[4])  # 第四个参数为维度1
    dim2 = int(sys.argv[5])  # 第五个参数为维度2
    dim3 = int(sys.argv[6])  # 第六个参数为维度3

    # 维度信息
    dimensions = (dim1, dim2, dim3)

    # 读取CSV文件并转换为稠密矩阵
    dense_matrix = load_csv_to_dense(csv_filename, order, dimensions)
    
    # 保存稠密矩阵为 .npy 文件
    np.save(output_filename, dense_matrix)

    print(f"稠密矩阵已保存为 '{output_filename}' 文件。")

if __name__ == "__main__":
    main()
