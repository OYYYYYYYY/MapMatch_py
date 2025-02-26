# # extract the spatial features of the links from link.csv to new .csv file
# import pandas as pd
# import random
# import math
# import sys

# def main(argv):
#     input = argv[1]
#     output = argv[2]

#     df = pd.read_csv(input)

#     # 只输出列名
#     print(df.columns.values)
#     df=df[['name','link_id','osm_way_id','from_node_id','to_node_id','dir_flag','length','lanes','free_speed','capacity','link_type_name','link_type','geometry','allowed_uses','from_biway','is_link','VDF_fftt1','VDF_cap1']]
#     # 结果  (行数,列数)
#     print(df.shape)

#     # 显示每一列中的缺失值数量
#     print(df.isnull().sum())
#     # 返回重复的行数
#     print(df.duplicated().sum())

#     # 删除重复值 不改变源数据 临时生成的表 && 删除符合条件的指定行，并替换原始df
#     df.drop_duplicates(inplace=True)
#     df = df.loc[~(df['allowed_uses'] != "auto")]
#     df = df.loc[~(df['is_link'].eq(0))]

#     print(df.head(10))
#     print(df.shape)

#     with open(output,'w+', encoding='utf-8') as f:
#         # f.write('link_id,dir_flag,length,lanes,link_type\n')
#         # for line in df.values:
#         #     f.write((str(line[1])+','+str(line[5])+','+str(line[6])+','+str(line[7])+','+str(line[11])+'\n'))
#         f.write('link_id,length,lanes,link_type\n')
#         for line in df.values:
#             f.write((str(line[1])+','+str(line[6])+','+str(line[7])+','+str(line[11])+'\n'))

#     print("finish")

# if __name__ == '__main__':
#     sys.exit(main(sys.argv))

########################################################################################################################
# extract the spatial features of the links of link_single_noid.csv
import pandas as pd

# 读取文件A和文件B
file_a = pd.read_csv('/data/oydata/MapMatch_py/data/cd_taxi/link_feature.csv')
file_b = pd.read_csv('/data/oydata/MapMatch_py/data/cd_taxi/link_single_noid.csv')

# 根据'link_id'列进行匹配
merged_data = pd.merge(file_a, file_b[['link_id']], on='link_id', how='inner')

# 将匹配成功的结果输出到新的CSV文件C
merged_data.to_csv('/data/oydata/MapMatch_py/data/cd_taxi/link_single_feature.csv', index=False)

print("finish match, output to new file!")

