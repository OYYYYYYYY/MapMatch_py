# import os

# # 设置目录路径
# directory_path = '/data/oydata/MapMatch_py/data/san_taxi/t_data'

# # 处理每个txt文件，将空格替换为逗号并转换为csv文件
# def process_txt_to_csv(input_file, output_file):
#     with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
#         outfile.write('lat,lng,no,timestamp\n')
#         for line in infile:
#             modified_line = line.replace('-', '')
#             # 将空格替换为逗号
#             modified_line = modified_line.replace(' ', ',')

#             outfile.write(modified_line)

# # 获取目录下所有txt文件并处理
# txt_files = [file for file in os.listdir(directory_path) if file.endswith('.txt')]
# for txt_file in txt_files:
#     txt_path = os.path.join(directory_path, txt_file)
#     csv_path = os.path.join(directory_path, txt_file.replace('.txt', '.csv'))
#     process_txt_to_csv(txt_path, csv_path)
#     print(f'文件 {txt_file} 转换为 {txt_file.replace(".txt", ".csv")} 完成')

# # # 合并所有csv文件到一个文件中
# # output_csv_file = 'merged_output.csv'
# # with open(os.path.join(directory_path, output_csv_file), 'w', newline='') as outfile:
# #     for csv_file in [file for file in os.listdir(directory_path) if file.endswith('.csv')]:
# #         csv_path = os.path.join(directory_path, csv_file)
# #         with open(csv_path, 'r') as infile:
# #             for line in infile:
# #                 outfile.write(line)

####################################################################################################

# import os
# import pandas as pd

# # 设置目录路径
# directory_path = '/data/oydata/MapMatch_py/data/san_taxi/t_data'

# # 获取目录下所有csv文件并处理
# csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]
# for csv_file in csv_files:
#     csv_path = os.path.join(directory_path, csv_file)
    
#     # 使用Pandas读取CSV文件
#     df = pd.read_csv(csv_path)
    
#     # 检查是否存在名为'no'的列，并删除
#     if 'no' in df.columns:
#         df.drop(columns=['no'], inplace=True)
    
#     # 保存修改后的数据回CSV文件
#     df.to_csv(csv_path, index=False)

#     print(f'文件 {csv_file} 处理完成')

# print('所有文件处理完成！')

####################################################################################################

# import os
# import pandas as pd

# # 设置目录路径
# directory_path = '/data/oydata/MapMatch_py/data/san_taxi/t_data'

# # 获取目录下所有csv文件并处理
# csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]
# for csv_file in csv_files:
#     csv_path = os.path.join(directory_path, csv_file)
    
#     # 使用Pandas读取CSV文件
#     df = pd.read_csv(csv_path)
    
#     # 检查是否存在名为'lat'和'lng'的列，并交换它们的位置
#     if 'lat' in df.columns and 'lng' in df.columns:
#         # 交换位置
#         columns = df.columns.tolist()
#         lat_index = columns.index('lat')
#         lng_index = columns.index('lng')
#         columns[lat_index], columns[lng_index] = columns[lng_index], columns[lat_index]
#         df = df.reindex(columns=columns)
    
#     # 保存修改后的数据回CSV文件
#     df.to_csv(csv_path, index=False)

#     print(f'文件 {csv_file} 处理完成')

# print('所有文件处理完成！')


####################################################################################################

# import os
# import pandas as pd

# # 设置目录路径
# directory_path = '/data/oydata/MapMatch_py/data/san_taxi/t_data'
# output_directory = '/data/oydata/MapMatch_py/data/san_taxi/t_data/time_data'

# # 定义时间戳格式转换函数
# def convert_timestamp(timestamp):
#     return pd.to_datetime(timestamp, unit='s').strftime('%Y-%m-%d,%H:%M:%S')

# # 获取目录下所有csv文件并处理
# csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]
# for csv_file in csv_files:
#     csv_path = os.path.join(directory_path, csv_file)
    
#     # 使用Pandas读取CSV文件
#     df = pd.read_csv(csv_path)
    
#     # 修改表头为指定字段名
#     df.columns = ['lat', 'lng', 'timestamp']
    
#     # 将时间戳转换为年月日,小时分钟秒的格式
#     df['timestamp'] = df['timestamp'].apply(convert_timestamp)
#     df[['day', 'time']] = df['timestamp'].str.split(',', expand=True)
#     df.drop(columns=['timestamp'], inplace=True)
    
#     # 构建输出文件路径
#     output_file = os.path.join(output_directory, csv_file)
    
#     # 保存修改后的数据到新的目录中
#     df.to_csv(output_file, index=False)

#     print(f'文件 {csv_file} 处理完成')

# print('所有文件处理完成！')

####################################################################################################

# import os
# import pandas as pd

# # 设置目录路径
# directory_path = '/data/oydata/MapMatch_py/data/san_taxi/t_data/time_data'

# # 获取目录下所有csv文件并处理
# csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]
# for csv_file in csv_files:
#     csv_path = os.path.join(directory_path, csv_file)
    
#     # 使用Pandas读取CSV文件
#     df = pd.read_csv(csv_path)
    
#     # 检查是否存在名为'day'的列，并进行条件筛选
#     if 'day' in df.columns:
#         # 保留day元素为2008-05-**的行
#         df = df[df['day'].str.startswith('2008-05')]
    
#     # 构建输出文件路径
#     output_file = os.path.join(directory_path, f'05_{csv_file}')
    
#     # 保存修改后的数据到新文件
#     df.to_csv(output_file, index=False)

#     print(f'文件 {csv_file} 处理完成')

# print('所有文件处理完成！')

####################################################################################################

# import os
# import pandas as pd

# # 设置目录路径
# directory_path = '/data/oydata/MapMatch_py/data/san_taxi/t_data/05_time_data'

# # 获取目录下所有csv文件并处理
# csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]
# for csv_file in csv_files:
#     csv_path = os.path.join(directory_path, csv_file)
    
#     # 使用Pandas读取CSV文件
#     df = pd.read_csv(csv_path)
    
#     # 检查是否存在名为'day'的列，并进行替换
#     if 'day' in df.columns:
#         # 替换day列中的日期为对应的序号
#         df['day'] = pd.to_datetime(df['day']).dt.day - 1
    
#     # 构建输出文件路径
#     output_file = os.path.join(directory_path, f'dr_{csv_file}')
    
#     # 保存修改后的数据到新文件
#     df.to_csv(output_file, index=False)

#     print(f'文件 {csv_file} 处理完成')

# print('所有文件处理完成！')

####################################################################################################

# import os
# import pandas as pd

# # 设置目录路径
# directory_path = '/data/oydata/MapMatch_py/data/san_taxi/t_data/dr_time_data'
# output_path = '/data/oydata/MapMatch_py/data/san_taxi/t_data/sample_traj'
# # 定义时间转换函数
# def convert_time(time_str):
#     parts = time_str.split(':')
#     aa = int(parts[0])
#     bb = int(parts[1])
#     cc = int(parts[2])
#     # 判断bb是否在指定的采样时间中
#     if bb % 5 == 0:
#         # 计算转换后的值
#         value = aa * 12 + bb // 5
#         # 确保value的范围在0-287之间
#         value = max(0, min(287, value))
#         return int(value)
#     else:
#         return None

# # 获取目录下所有csv文件并处理
# csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]
# for csv_file in csv_files:
#     csv_path = os.path.join(directory_path, csv_file)
    
#     # 使用Pandas读取CSV文件
#     df = pd.read_csv(csv_path)
    
#     # 检查是否存在名为'time'的列，并进行采样和转换
#     if 'time' in df.columns:
#         # 对time列进行采样和转换
#         df['time'] = df['time'].apply(convert_time)
#         # 删除未采样到的行
#         df.dropna(subset=['time'], inplace=True)
    
#     # 构建输出文件路径
#     output_file = os.path.join(output_path, f'sampled_{csv_file}')
    
#     # 保存修改后的数据到新文件
#     df.to_csv(output_file, index=False)

#     print(f'文件 {csv_file} 处理完成')

# print('所有文件处理完成！')


####################################################################################################


# import os
# import pandas as pd

# # 设置目录路径
# directory_path = '/data/oydata/MapMatch_py/data/san_taxi/t_data/sample_traj'

# # 获取目录下所有csv文件并处理
# csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]

# # 确保至少有一个csv文件
# if len(csv_files) == 0:
#     print('目录中没有找到任何.csv文件。')
#     exit()

# # 读取第一个csv文件的表头
# first_csv_file = os.path.join(directory_path, csv_files[0])
# df_combined = pd.read_csv(first_csv_file)

# # 合并其余csv文件的数据，忽略表头
# for csv_file in csv_files[1:]:
#     csv_path = os.path.join(directory_path, csv_file)
#     df = pd.read_csv(csv_path, header=None)  # 不读取表头
#     df_combined = pd.concat([df_combined, df], ignore_index=True)

# # 构建输出文件路径
# output_file = os.path.join(directory_path, 'trajactory.csv')

# # 保存合并后的数据到新文件，只保留第一个文件的表头
# df_combined.to_csv(output_file, index=False, header=True)

# print(f'所有文件合并完成，并保存到 {output_file}')

####################################################################################################

import pandas as pd

# 读取CSV文件
csv_file = '/data/oydata/MapMatch_py/data/san_taxi/t_data/sample_traj/trajactory.csv'
df = pd.read_csv(csv_file)

# 找出lat字段的最大值和最小值
lat_max = df['lat'].max()
lat_min = df['lat'].min()

# 找出lng字段的最大值和最小值
lng_max = df['lng'].max()
lng_min = df['lng'].min()

# 输出结果
print(f'lat字段的最大值: {lat_max}')
print(f'lat字段的最小值: {lat_min}')
print(f'lng字段的最大值: {lng_max}')
print(f'lng字段的最小值: {lng_min}')