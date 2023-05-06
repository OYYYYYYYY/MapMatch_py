import pandas as pd
import random
import math
import csv

# df = pd.read_csv("./sz/link_geo_p.csv")

# # print(type(df))
# # 只输出列名
# print(df.columns.values)

# f=df[['name','link_id','osm_way_id','from_node_id','to_node_id','dir_flag','length','lanes','free_speed','capacity','link_type_name','link_type','geometry','allowed_uses','from_biway','is_link','VDF_fftt1','VDF_cap1']]

# #筛选出IP字段
# ip = info_1['geometry']
# #将idcip列以‘,’分开，分成多列
# ipdf = ip.str.split(',',expand = True)
# #将列转换为行
# ip = ipdf.stack()
# #将最后一级索引删除
# ip = ip.reset_index(drop=True,level=-1)
# #再调用一次reset_index，会自动进行笛卡尔乘积
# ipdf = ip.reset_index()
# #将自动生成的0列进行重命名
# ipdf = ipdf.rename(columns={0:'idcip'})
# print(ipdf)

with open('./sz/link_geo_p.csv', 'r') as infile, open('./sz/link_geo_t.csv', 'w') as outfile:
       stripped = (line.strip() for line in infile)
       lines = ([sent] for para in (line.split(",") for line in stripped if line) for sent in para)
       writer = csv.writer(outfile)
       writer.writerows(lines)

# with open('./sz/link_geo_t.csv','w+', encoding='utf-8') as f:
#     # f.write('geometry\n')
#     for line in ipdf.values:
#         f.write((str(line[12])+'\n'))


# # 显示每一列中的缺失值数量
# print(df.isnull().sum())

# # 返回重复的行数
# print(df.duplicated().sum())

# # 删除重复值 不改变源数据 临时生成的表
# df.drop_duplicates(inplace=True)
# df = df.loc[~(df['allowed_uses'] != "auto")]

# # 删除符合条件的指定行，并替换原始df
# print(df.head(10))
# print(df.shape)

# with open('./sz/link_geo.csv','w+', encoding='utf-8') as f:
#     # f.write('geometry\n')
#     for line in df.values:
#         f.write((str(line[12])+'\n'))

# with open('./sz/link_geo.csv','r') as fr:
#     lines = fr.readlines()
# with open('./sz/link_geo_new.csv','w') as fw:
#     for line in lines:
#         fw.write(line.replace('LINESTRING (',''))

# with open('./sz/link_geo_new.csv','r') as fr1:
#     lines1 = fr1.readlines()
# with open('./sz/link_geo_p.csv','w') as fw1:
#     for line1 in lines1:
#         fw1.write(line1.replace(')',''))



