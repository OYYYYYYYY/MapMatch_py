# import pandas as pd
# import numpy as np
# import csv
# import math
# import sys

# def main(argv):
#     # input tensor file .csv
#     input = argv[1]
#     # output tensor file .csv
#     output = argv[2]

#     # read tensor file
#     with open(input, 'r') as f:
#         reader = csv.DictReader(f)
#         link_id = []
#         times = []
#         days = []
#         values = []
#         for row in reader:
#             temp0 = float(row['road'])
#             temp1 = float(row['time'])
#             temp2 = float(row['days'])
#             link_id.append(int(temp0))
#             times.append(int(temp1))
#             days.append(int(temp2))
#             values.append(float(row['values']))

#     num = len(link_id)

#     with open(output, 'w') as fww:
#         fww.write('3\n')
#         # fww.write('5393 1080 25\n')
#         fww.write('2235 144 7\n')
#         # fww.write('road,time,days,values\n')
#         for i in range(num):
#             fww.write((str(link_id[i])+' '+str(times[i])+' '+str(days[i])+' '+str(values[i])+'\n'))

#     print("finish")

# if __name__ == '__main__':
#     sys.exit(main(sys.argv))

##################################################################################################################################
import os
import sys
import csv

def process_file(input_file, output_file):
    # 打开原始CSV文件读取内容
    with open(input_file, 'r') as infile:
        reader = csv.reader(infile)
        # 跳过表头
        next(reader)
        
        # 打开目标输出文件
        with open(output_file, 'w') as outfile:
            # 写入第一行
            outfile.write('3\n')
            # 写入第二行
            # outfile.write('7471 288 28\n')
            outfile.write('2109 288 72\n')
            
            # 处理剩下的每一行
            for row in reader:
                # 将逗号分隔的数据改为空格分隔，并写入文件
                outfile.write(' '.join(row) + '\n')
    
    print(f"Processed file: {input_file} -> {output_file}")

def main(argv):
    # 输入目录
    input_dir = argv[1]
    # 输出目录
    output_dir = argv[2]

    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 遍历输入目录中的所有文件
    for filename in os.listdir(input_dir):
        if filename.endswith('.csv'):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, filename.replace('.csv', '.tns'))
            
            # 处理文件
            process_file(input_file, output_file)

    print("Finished processing all files.")

if __name__ == '__main__':
    sys.exit(main(sys.argv))
