import os
import pandas as pd
import numpy as np
import sys

def process_csv_file(file_path, output_dir):
    # 读取 CSV 文件
    df = pd.read_csv(file_path)

    # 检查 'values' 列中是否有 NaN 或 inf
    condition = df['values'].apply(lambda x: pd.isna(x) or np.isinf(x))
    # 统计包含 NaN 或 inf 的行数
    num_invalid_rows = condition.sum()

    # 输出包含 NaN 或 inf 的行数
    if num_invalid_rows > 0:
        print(f"{file_path} - 发现 {num_invalid_rows} 行包含 NaN 或 inf")

    # 过滤掉包含 NaN 或 inf 的行
    df_cleaned = df[~condition]

    # 获取文件名并生成新的输出文件路径
    file_name = os.path.basename(file_path)
    
    # 如果输入目录和输出目录相同，为新文件名加上 '_c'
    if os.path.dirname(file_path) == output_dir:
        file_name_without_ext, ext = os.path.splitext(file_name)
        file_name = file_name_without_ext + '_c' + ext

    output_file_path = os.path.join(output_dir, file_name)

    # 将清洗后的数据保存到新的 CSV 文件
    df_cleaned.to_csv(output_file_path, index=False)

    print(f"{file_path} 的清洗结果已保存到 {output_file_path}")

def process_directory(directory_path, output_dir):
    # 遍历目录下的所有 .csv 文件
    for filename in os.listdir(directory_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory_path, filename)
            process_csv_file(file_path, output_dir)

if __name__ == "__main__":
    # 从命令行参数获取目录路径和输出目录路径
    if len(sys.argv) != 3:
        print("使用方法: python process_csv.py <输入目录> <输出目录>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_directory = sys.argv[2]

    # 确保输出目录存在
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 处理目录中的所有 CSV 文件
    process_directory(input_directory, output_directory)
