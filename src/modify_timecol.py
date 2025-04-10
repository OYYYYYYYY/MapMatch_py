# import os
# import csv
# import sys

# def process_csv_file(csv_filename, divisor):
#     """ 处理单个 CSV 文件，修改 'time' 列的数据 """
#     # 读取 CSV 文件
#     with open(csv_filename, 'r', newline='', encoding='utf-8') as f:
#         reader = csv.DictReader(f)
#         rows = list(reader)

#     # 检查 'time' 列是否存在
#     if 'time' not in rows[0]:
#         print(f"警告: 文件 {csv_filename} 中没有 'time' 列，跳过此文件。")
#         return

#     # 对 'time' 列进行操作
#     for row in rows:
#         try:
#             # 将 'time' 列的值除以 divisor，并取整
#             row['time'] = str(int(float(row['time']) / divisor))
#         except ValueError:
#             print(f"警告: 文件 {csv_filename} 中某行的 'time' 值无法转换为数字，跳过该行。")
#             continue

#     # 将修改后的内容保存回原文件
#     with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
#         fieldnames = reader.fieldnames
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(rows)

#     print(f"文件 {csv_filename} 的 'time' 列已处理并覆盖保存。")

# def process_directory(directory, divisor):
#     """ 处理目录中的所有 .csv 文件 """
#     for filename in os.listdir(directory):
#         if filename.endswith('.csv'):
#             csv_filename = os.path.join(directory, filename)
#             process_csv_file(csv_filename, divisor)

# def main():
#     # 从命令行参数获取目录路径和除以的整数
#     if len(sys.argv) != 3:
#         print("用法: python script.py <目录路径> <除以的整数>")
#         sys.exit(1)

#     directory = sys.argv[1]
#     try:
#         divisor = int(sys.argv[2])
#     except ValueError:
#         print("除以的整数必须是整数。")
#         sys.exit(1)

#     # 处理目录中的所有文件
#     process_directory(directory, divisor)

# if __name__ == "__main__":
#     main()



# import os
# import sys
# import pandas as pd

# # 获取命令行输入参数
# directory_path = sys.argv[1]  # 输入的目录路径
# column_name = sys.argv[2]  # 指定的列名

# def convert_column_to_int(file_path, column_name):
#     try:
#         # 读取CSV文件
#         df = pd.read_csv(file_path)

#         # 检查列是否存在
#         if column_name in df.columns:
#             # 强制转换为整数
#             df[column_name] = df[column_name].astype(int)
#             # 将修改后的数据覆盖保存到原文件
#             df.to_csv(file_path, index=False)
#             print(f"成功处理并覆盖文件: {file_path}")
#         else:
#             print(f"文件 {file_path} 中没有找到列: {column_name}")
#     except Exception as e:
#         print(f"处理文件 {file_path} 时发生错误: {e}")

# # 遍历指定目录中的所有CSV文件
# for root, dirs, files in os.walk(directory_path):
#     for file in files:
#         if file.endswith(".csv"):
#             file_path = os.path.join(root, file)
#             convert_column_to_int(file_path, column_name)


import os
import csv
import math

def process_file(file_path):
    # 读取文件内容
    with open(file_path, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)

    # 处理每一行的 time 列
    for row in rows:
        if row['time'].isdigit():  # 确保time是一个有效的数字
            row['time'] = str(math.floor(int(row['time']) / 5))

    # 将处理后的内容写回到原文件
    with open(file_path, 'w', newline='', encoding='utf-8') as outfile:
        fieldnames = ['road', 'time', 'days', 'values']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()  # 写入表头
        writer.writerows(rows)  # 写入处理过的行

    print(f"Processed file: {file_path}")

def main(argv):
    # 输入目录
    input_dir = argv[1]

    # 遍历输入目录中的所有文件
    for filename in os.listdir(input_dir):
        if filename.endswith('.csv'):
            file_path = os.path.join(input_dir, filename)
            # 处理每个csv文件
            process_file(file_path)

    print("Finished processing all files.")

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

