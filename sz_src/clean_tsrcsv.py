# import pandas as pd

# # 读取CSV文件
# df = pd.read_csv('/data/oydata/MapMatch_py/data/week_sz_taxi/sz_nopoi.csv')

# # 按照第一列数据大小排序，并重新编号第一列
# df_sorted = df.sort_values(by=df.columns[0])
# df_sorted.iloc[:, 0] = pd.factorize(df_sorted.iloc[:, 0])[0]

# # 将第一列数据进行替换，处理相同值的情况
# def replace_duplicates(df, col_index):
#     seen = {}
#     result = []
#     for value in df.iloc[:, col_index]:
#         if value not in seen:
#             seen[value] = 0
#         else:
#             seen[value] += 1
#         result.append(seen[value])
#     return result

# df_sorted.iloc[:, 0] = replace_duplicates(df_sorted, 0)

# # 将结果输出到新的CSV文件
# df_sorted.to_csv('/data/oydata/MapMatch_py/data/week_sz_taxi/sz_nopoi_t.csv', index=False)

# import pandas as pd

# # 读取CSV文件
# df = pd.read_csv('/data/oydata/MapMatch_py/data/week_sz_taxi/sz_nopoi.csv')

# # 按照第一列数据大小排序，并重新编号第一列
# df_sorted = df.sort_values(by=df.columns[0])
# df_sorted.iloc[:, 0] = pd.factorize(df_sorted.iloc[:, 0])[0]

# # 处理相同值的情况，替换为前一个值的编号
# current_value = df_sorted.iloc[0, 0]
# for i in range(1, len(df_sorted)):
#     if df_sorted.iloc[i, 0] == df_sorted.iloc[i-1, 0]:
#         df_sorted.iloc[i, 0] = current_value
#     else:
#         current_value = df_sorted.iloc[i, 0]

# # 将结果输出到新的CSV文件
# df_sorted.to_csv('/data/oydata/MapMatch_py/data/week_sz_taxi/sz_nopoi_t.csv', index=False)




# import pandas as pd

# def count_unique_values(csv_file):
#     # 读取CSV文件为pandas DataFrame
#     df = pd.read_csv(csv_file)
    
#     # 检查 'road' 列是否存在于DataFrame中
#     if 'road' not in df.columns:
#         print("Error: 'road' 列在CSV文件中不存在。")
#         return
    
#     # 统计 'road' 列中的唯一值数量
#     unique_values_count = df['road'].nunique()
    
#     # 输出唯一值的数量
#     print(f"字段 'road' 中不同值的数量为: {unique_values_count}")
    
#     # 如果需要输出具体的不同值，可以使用下面的代码
#     # unique_values = df['road'].unique()
#     # print("不同的 'road' 列的值为:")
#     # for value in unique_values:
#     #     print(value)

# if __name__ == "__main__":
#     csv_file = '/data/oydata/MapMatch_py/data/week_sz_taxi/sz_nopoi_t.csv'  # 替换为你的CSV文件路径
#     count_unique_values(csv_file)




# import pandas as pd

# def sort_csv_by_road(input_file, output_file):
#     # 读取CSV文件为DataFrame
#     df = pd.read_csv(input_file)
    
#     # 按照'road'列进行排序
#     df_sorted = df.sort_values(by=['road'])
    
#     # 保存排序后的结果到CSV文件
#     df_sorted.to_csv(output_file, index=False)
#     print(f"已将排序后的结果保存到文件: {output_file}")

# if __name__ == "__main__":
#     input_file = '/data/oydata/MapMatch_py/data/week_sz_taxi/sz_nopoi.csv'   # 替换为输入CSV文件的路径
#     output_file = '/data/oydata/MapMatch_py/data/week_sz_taxi/sz_nopoi0.csv'  # 替换为输出排序后的CSV文件的路径
#     sort_csv_by_road(input_file, output_file)



# import pandas as pd

# # 读取原始的CSV文件
# df = pd.read_csv('/data/oydata/MapMatch_py/data/week_sz_taxi/sz_nopoi.csv')

# # 删除指定的列，假设要删除名为'XX'的列
# columns_to_drop = ['road', 'poi_score', 'from_id', 'to_id']
# df = df.drop(columns=columns_to_drop)

# # 删除重复行
# # df.drop_duplicates(inplace=True)

#     # 将 new_road 列移到第一列
# if 'new_road' in df.columns:
#     new_road_col = df['new_road']
#     df.drop(labels=['new_road'], axis=1, inplace=True)
#     df.insert(0, 'new_road', new_road_col)

# # 保存处理后的结果为新的CSV文件
# df.to_csv('/data/oydata/MapMatch_py/data/week_sz_taxi/sz_poi.csv', index=False)

# import pandas as pd

# def remove_duplicates_and_save(csv_file):
#     # 读取CSV文件
#     df = pd.read_csv(csv_file)

#     # 删除重复行
#     df = df.drop_duplicates()

#     # 保存新的CSV文件
#     # new_file = 'u' + csv_file  # 新文件名为在原文件名前加上 "unique_"
#     df.to_csv('/data/oydata/MapMatch_py/data/week_sz_taxi/usz_nopoi_sin.csv', index=False)

# if __name__ == "__main__":
#     csv_file = '/data/oydata/MapMatch_py/data/week_sz_taxi/sz_nopoi_sin.csv'  # 替换为实际的CSV文件路径
#     remove_duplicates_and_save(csv_file)

# import pandas as pd

# def decrease_column_inplace_and_save(csv_file):
#     # 读取CSV文件
#     df = pd.read_csv(csv_file)

#     # 将 new_road 列的所有元素减1
#     # df['road'] = df['road'] + 1
#     # df['time'] = df['time'] / 2 + 1
#     df['days'] = df['days'] / 2 + 1

#     # 保存回原始CSV文件（覆盖原文件）
#     df.to_csv(csv_file, index=False)

# if __name__ == "__main__":
#     csv_file = '/data/oydata/MapMatch_py/data/week_sz_taxi/sz_poi_end.csv'  # 替换为实际的CSV文件路径
#     decrease_column_inplace_and_save(csv_file)


# import pandas as pd

# def process_and_save_csv(csv_file):
#     # 读取CSV文件
#     df = pd.read_csv(csv_file)

#     # 删除指定列
#     columns_to_drop = ['road', 'poi_score', 'from_id', 'to_id']
#     df = df.drop(columns=columns_to_drop)

#     # 将 new_road 列移到第一列
#     if 'new_road' in df.columns:
#         new_road_col = df['new_road']
#         df.drop(labels=['new_road'], axis=1, inplace=True)
#         df.insert(0, 'new_road', new_road_col)

#     # 保存回原始CSV文件（覆盖原文件）
#     df.to_csv('/data/oydata/MapMatch_py/data/week_sz_taxi/sz_poi_r.csv', index=False)

# if __name__ == "__main__":
#     csv_file = '/data/oydata/MapMatch_py/data/week_sz_taxi/sz_poi.csv'  # 替换为实际的CSV文件路径
#     process_and_save_csv(csv_file)

# import pandas as pd

# # 读取CSV文件到DataFrame
# df = pd.read_csv('/data/oydata/MapMatch_py/data/week_sz_taxi/sz_poi_end.csv')

# # 指定要检查重复的列
# subset_columns = ['road', 'time', 'days']

# # 检查是否有重复行
# duplicate_rows = df[df.duplicated(subset=subset_columns, keep=False)]

# # 打印重复行
# if not duplicate_rows.empty:
#     print("重复的行：")
#     print(duplicate_rows)
# else:
#     print("没有重复行。")


import pandas as pd

# 读取CSV文件到DataFrame
df = pd.read_csv('/data/oydata/MapMatch_py/data/week_sz_taxi/sz_poi_end.csv')

# 指定要检查重复的列
subset_columns = ['road', 'time', 'days']

# 删除重复行，并且对指定列取整
df = df.drop_duplicates(subset=subset_columns).astype({col: int for col in subset_columns})

# 保存处理后的数据到新的CSV文件
df.to_csv('/data/oydata/MapMatch_py/data/week_sz_taxi/sz_poi_end.csv', index=False)

print("处理完成，已保存到 processed_file.csv。")


