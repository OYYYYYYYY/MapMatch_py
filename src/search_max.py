import os
import csv
import sys

def find_max_in_column(csv_filename, column_index):
    """ 查找指定列的最大值 """
    max_value = float('-inf')  # 初始化为负无穷大

    # 打开 CSV 文件并读取内容
    with open(csv_filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # 跳过表头
        for row in reader:
            try:
                # 读取指定列的值并更新最大值
                value = float(row[column_index])
                if value > max_value:
                    max_value = value
            except ValueError:
                # 跳过无法转换为浮动数值的情况
                continue

    return max_value

def process_directory(directory, column_index):
    """ 处理目录中的所有 .csv 文件 """
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            csv_filename = os.path.join(directory, filename)
            max_value = find_max_in_column(csv_filename, column_index)
            print(f"文件 '{filename}' 中指定列的最大值是: {max_value}")

def main():
    # 从命令行参数获取目录路径和列索引
    if len(sys.argv) != 3:
        print("用法: python script.py <目录路径> <列索引>")
        sys.exit(1)

    directory = sys.argv[1]
    try:
        column_index = int(sys.argv[2])
    except ValueError:
        print("列索引必须是整数。")
        sys.exit(1)

    # 处理目录中的所有文件
    process_directory(directory, column_index)

if __name__ == "__main__":
    main()
