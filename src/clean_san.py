# import csv

# input_file = '/data/oydata/MapMatch_py/data/san_taxi/raw_data/merged.csv'
# output_file = '/data/oydata/MapMatch_py/data/san_taxi/raw_data/merged_new.csv'


# # 打开输入文件和输出文件
# with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
#     reader = csv.reader(infile)
    
#     # 遍历输入文件的每一行
#     for row in reader:
#         # 将每个单元格中的空格替换为逗号
#         modified_row = [cell.replace(' ', ',') for cell in row]
#         # 将列表转换为字符串，以逗号分隔
#         line = ','.join(modified_row)
#         # 写入修改后的行到输出文件
#         outfile.write(line + '\n')

# print(f'处理完成！结果保存在 {output_file} 中。')

# import csv

# input_file = '/data/oydata/MapMatch_py/data/san_taxi/raw_data/merged_new.csv'
# output_file = '/data/oydata/MapMatch_py/data/san_taxi/raw_data/merged_new-.csv'

# # 打开输入文件和输出文件
# with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
#     reader = csv.reader(infile)
#     writer = csv.writer(outfile)

#     # 遍历输入文件的每一行
#     for row in reader:
#         # 将每个单元格中的 - 符号替换为空字符串
#         modified_row = [cell.replace('-', '') for cell in row]
#         # 写入修改后的行到输出文件
#         writer.writerow(modified_row)

import pandas as pd
import random
import math
import sys


def main(argv):
    input = argv[1]
    output = argv[2]
    # poi.csv clean code
    df = pd.read_csv(input)

    # 只输出列名
    print(df.columns.values)

    df=df[['lat','lng','no','timestamp']]
    # 结果  (行数,列数)
    print(df.shape)

    # 显示每一列中的缺失值数量
    print(df.isnull().sum())

    # 返回重复的行数
    print(df.duplicated().sum())

    # 删除重复值 不改变源数据 临时生成的表
    df.drop_duplicates(inplace=True)

    with open(output,'w+', encoding='utf-8') as f:
        f.write('lng,lat,timestamp\n')
        for line in df.values:
            #str(line[0])：csv中第0列；+','+：csv两列之间保存到txt用逗号（，）隔开；'\n'：读取csv每行后在txt中换行
            f.write((str(line[1])+','+str(line[0])+','+str(line[3])+'\n'))

if __name__ == '__main__':
    sys.exit(main(sys.argv))
