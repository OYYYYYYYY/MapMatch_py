import pandas as pd

def filter_fileB_based_on_fileA(fileA, fileB, output_file):
    # 读取文件A并提取'road'列数据
    df_A = pd.read_csv(fileA)
    roads_from_A = df_A['road'].unique()
    
    # 读取文件B并筛选数据
    df_B = pd.read_csv(fileB)
    filtered_df_B = df_B[df_B['link_id'].isin(roads_from_A)]
    
    # 输出为新的.csv文件C
    filtered_df_B.to_csv(output_file, index=False)
    print(f"已将筛选后的结果保存到文件: {output_file}")

if __name__ == "__main__":
    fileA = '/data/oydata/MapMatch_py/data/week_sz_taxi/sz_nopoi.csv'  # 替换为文件A的路径
    fileB = '//data/oydata/MapMatch_py/data/week_sz_taxi/link_single0.csv'  # 替换为文件B的路径
    output_file = '/data/oydata/MapMatch_py/data/week_sz_taxi/link_sin_rm.csv'  # 替换为输出文件C的路径
    filter_fileB_based_on_fileA(fileA, fileB, output_file)


import pandas as pd

# 读取文件A，假设road字段是整数，如16
df_a = pd.read_csv('/data/oydata/MapMatch_py/data/week_sz_taxi/sz_nopoi.csv')

# 读取文件B，假设文件B的列名为link_id，字段是浮点数，如17.0
df_b = pd.read_csv('/data/oydata/MapMatch_py/data/week_sz_taxi/link_single.csv')

# 提取文件A中的road字段的整数值作为要匹配的条件
roads_to_keep = df_a['road'].astype(int).tolist()

# 筛选文件B中符合条件的行
df_c = df_b[df_b['link_id'].astype(int).isin(roads_to_keep)]

# 将筛选后的结果保存为新的CSV文件C
df_c.to_csv('/data/oydata/MapMatch_py/data/week_sz_taxi/link_sin_rm.csv', index=False)


# import pandas as pd
# import random
# import math
# import csv
# import sys 

# def main(argv):
#     input1 = argv[1]
#     input2 = argv[2]
#     output = argv[3]
#     with open(input1 , 'r') as f:
#         reader = csv.DictReader(f)
#         road_id = []
#         for line in reader:
#             road_id.append(line['road'])
    
#     num = len(road_id)

#     with open(input2,'r') as f1:
#         reader = csv.DictReader(f1)
#         link_id = []
#         from_id = []
#         to_id = []
#         lng = []
#         lat = []
#         for row in reader:
#             link_id.append(row['link_id'])
#             from_id.append(float(row['from_node_id']))
#             to_id.append(float(row['to_node_id']))
#             lng.append(row['lng'])
#             lat.append(row['lat'])
    
#     num1 = len(link_id)

#     # cp_link = []
#     # cp_link = [0] * num
#     # cp_from =[]
#     # cp_from = [0] * num
#     # cp_to = []
#     # cp_to = [0] * num
#     # cp_lng =[]
#     # cp_lng = [0.0000] * num
#     # cp_lat = []
#     # cp_lat = [0.0000] * num

#     # count = 0
#     # for i in range(num1):
#     #     for j in range(num):
#     #         if(int(link_id[i]) == road_id[j]):
#     #             cp_link[count] = link_id[i]
#     #             cp_from[count] = from_id[i]
#     #             cp_to[count] = to_id[i]
#     #             cp_lng[count] = lng[i]
#     #             cp_lat[count] = lat[i]
#     #             count = count + 1
    
#     # print(count)
    
#     with open(output, 'w') as fw:
#         fw.write(('link_id,from_node_id,to_node_id,lng,lat\n'))
#         # for k in range(count):
#         #     if(k != 0):
#         #         if(cp_link[k] != cp_link[k-1]):
#         #             fw.write((str(int(cp_link[k]))+','+str(int(cp_from[k]))+','+str(int(cp_to[k]))+str(cp_lng[k])+','+str(cp_lat[k])+'\n'))
#         for i in range(num1):
#             for j in range(num):
#                 if(link_id[i] == road_id[j]):
#                     fw.write((str(link_id[i])+','+str(int(from_id[i]))+','+str(int(to_id[i]))+str(lng[i])+','+str(lat[i])+'\n'))

# if __name__ == '__main__':
#     sys.exit(main(sys.argv))
            



# import pandas as pd

# def remove_duplicates(input_file, output_file):
#     # 读取CSV文件为DataFrame
#     df = pd.read_csv(input_file)
    
#     # 去除重复行
#     df_no_duplicates = df.drop_duplicates()
    
#     # 保存结果到CSV文件
#     df_no_duplicates.to_csv(output_file, index=False)
#     print(f"已将去重后的结果保存到文件: {output_file}")

# if __name__ == "__main__":
#     input_file = '/data/oydata/MapMatch_py/data/week_sz_taxi/link_sin_rm.csv'   # 替换为输入CSV文件的路径
#     output_file = '/data/oydata/MapMatch_py/data/week_sz_taxi/link_sin_rm0.csv' # 替换为输出去重后的CSV文件的路径
#     remove_duplicates(input_file, output_file)





# import pandas as pd

# def convert_link_id(input_file, output_file):
#     # 读取CSV文件为DataFrame
#     df = pd.read_csv(input_file)
    
#     # 将'link_id'列的浮点数格式转换为整数
#     df['link_id'] = df['link_id'].astype(int)
    
#     # 保存结果到CSV文件
#     df.to_csv(output_file, index=False)
#     print(f"已将处理后的结果保存到文件: {output_file}")

# if __name__ == "__main__":
#     input_file = '/data/oydata/MapMatch_py/data/week_sz_taxi/link_single.csv'   # 替换为输入CSV文件的路径
#     output_file = '/data/oydata/MapMatch_py/data/week_sz_taxi/link_single0.csv'  # 替换为输出处理后的CSV文件的路径
#     convert_link_id(input_file, output_file)
