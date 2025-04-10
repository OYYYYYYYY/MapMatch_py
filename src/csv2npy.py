# generate a npy tensor
import numpy as np
import pandas as pd
import argparse

def csv_to_sparse_tensor(csv_file, output_file, max_road, max_time, max_days):
    # 读取 CSV 文件
    df = pd.read_csv(csv_file)

    # 创建一个全零的稀疏张量
    sparse_tensor = np.zeros((max_road, max_time, max_days))

    # 提取索引和对应的值
    road_idx = df['road'].values
    time_idx = df['time'].values
    days_idx = df['days'].values
    values = df['values'].values

    # 填充稀疏张量
    for r, t, d, v in zip(road_idx, time_idx, days_idx, values):
        sparse_tensor[r, t, d] = v

    # 保存为 NPY 文件
    np.save(output_file, sparse_tensor)
    print(f"数据已成功保存为 {output_file}")

def main():
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description="将 CSV 文件转换为稀疏张量并保存为 NPY 文件")
    
    # 输入文件路径
    parser.add_argument('csv_file', type=str, help="输入的 CSV 文件路径")
    # 输出文件路径
    parser.add_argument('output_file', type=str, help="保存的 NPY 文件路径")
    # 张量维度：max_road, max_time, max_days
    parser.add_argument('max_road', type=int, help="稀疏张量的最大 road 维度")
    parser.add_argument('max_time', type=int, help="稀疏张量的最大 time 维度")
    parser.add_argument('max_days', type=int, help="稀疏张量的最大 days 维度")

    # 解析命令行参数
    args = parser.parse_args()

    # 调用转换函数
    csv_to_sparse_tensor(args.csv_file, args.output_file, args.max_road, args.max_time, args.max_days)

if __name__ == "__main__":
    main()

##############################################################################################################
# # generate a npy tensor and a npy binary tensor
# import numpy as np
# import pandas as pd
# import argparse

# def csv_to_sparse_tensor(csv_file, output_file, output_label_file, max_road, max_time, max_days):
#     # 读取 CSV 文件
#     df = pd.read_csv(csv_file)

#     # 创建一个全零的稀疏张量
#     sparse_tensor = np.zeros((max_road, max_time, max_days))
#     # 创建一个全零的标签张量
#     label_tensor = np.zeros((max_road, max_time, max_days))

#     # 提取索引和对应的值
#     road_idx = df['road'].values
#     time_idx = df['time'].values
#     days_idx = df['days'].values
#     values = df['values'].values

#     # 填充稀疏张量
#     for r, t, d, v in zip(road_idx, time_idx, days_idx, values):
#         sparse_tensor[r, t, d] = v
#         if v != 0:
#             label_tensor[r, t, d] = 1  # 如果值不为0，标记为1

#     # 保存为 NPY 文件
#     np.save(output_file, sparse_tensor)
#     np.save(output_label_file, label_tensor)
#     print(f"数据已成功保存为 {output_file} 和 {output_label_file}")

# def main():
#     # 设置命令行参数解析
#     parser = argparse.ArgumentParser(description="将 CSV 文件转换为稀疏张量并生成标签张量")
    
#     # 输入文件路径
#     parser.add_argument('csv_file', type=str, help="输入的 CSV 文件路径")
#     # 输出文件路径
#     parser.add_argument('output_file', type=str, help="保存的 NPY 文件路径（aaa.npy）")
#     parser.add_argument('output_label_file', type=str, help="保存的标签 NPY 文件路径（bbb.npy）")
#     # 张量维度：max_road, max_time, max_days
#     parser.add_argument('max_road', type=int, help="稀疏张量的最大 road 维度")
#     parser.add_argument('max_time', type=int, help="稀疏张量的最大 time 维度")
#     parser.add_argument('max_days', type=int, help="稀疏张量的最大 days 维度")

#     # 解析命令行参数
#     args = parser.parse_args()

#     # 调用转换函数
#     csv_to_sparse_tensor(args.csv_file, args.output_file, args.output_label_file, args.max_road, args.max_time, args.max_days)

# if __name__ == "__main__":
#     main()
