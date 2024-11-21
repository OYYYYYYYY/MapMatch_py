# import csv

# txt_file = '/data/oydata/MapMatch_py/data/san_taxi/raw_data/new_abboip.txt'
# csv_file = '/data/oydata/MapMatch_py/data/san_taxi/raw_data/new_abboip.csv'

# # # 打开 txt 文件和 csv 文件
# # with open(txt_file, 'r') as infile, open(csv_file, 'w', newline='') as outfile:
# #     # 逐行读取 txt 文件内容
# #     for line in infile:
# #         # 去除行末尾的换行符，并按空格分割行数据
# #         # data = line.strip().split()
# #         # 将分割后的数据连接成一个字符串，用逗号分隔
# #         csv_line = ','.join(data)
# #         # 写入到 csv 文件
# #         outfile.write(csv_line + '\n')

# # print(f'转换完成！结果保存在 {csv_file} 中。')

# # txt_file = 'input.txt'
# # csv_file = 'output.csv'

# # 打开 txt 文件和 csv 文件
# with open(txt_file, 'r') as infile, open(csv_file, 'w') as outfile:
#     # 逐行读取 txt 文件内容并写入 csv 文件
#     for line in infile:
#         outfile.write(line)

# print(f'转换完成！结果保存在 {csv_file} 中。')


import os

# 设置目录路径
directory_path = '/data/oydata/MapMatch_py/data/san_taxi/clean_data'

# 处理每个txt文件，将空格替换为逗号并转换为csv文件
def process_txt_to_csv(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        for line in infile:
            # 将空格替换为逗号
            modified_line = line.replace(' ', ',')
            outfile.write(modified_line)

# 获取目录下所有txt文件并处理
txt_files = [file for file in os.listdir(directory_path) if file.endswith('.txt')]
for txt_file in txt_files:
    txt_path = os.path.join(directory_path, txt_file)
    csv_path = os.path.join(directory_path, txt_file.replace('.txt', '.csv'))
    process_txt_to_csv(txt_path, csv_path)
    print(f'文件 {txt_file} 转换为 {txt_file.replace(".txt", ".csv")} 完成')

# 合并所有csv文件到一个文件中
output_csv_file = 'merged_output.csv'
with open(os.path.join(directory_path, output_csv_file), 'w', newline='') as outfile:
    for csv_file in [file for file in os.listdir(directory_path) if file.endswith('.csv')]:
        csv_path = os.path.join(directory_path, csv_file)
        with open(csv_path, 'r') as infile:
            for line in infile:
                outfile.write(line)