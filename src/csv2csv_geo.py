# clean link.csv to get simple geometry information
import pandas as pd
import random
import math
import csv

df = pd.read_csv("./data/link.csv")

f=df[['name','link_id','osm_way_id','from_node_id','to_node_id','dir_flag','length','lanes','free_speed','capacity','link_type_name','link_type','geometry','allowed_uses','from_biway','is_link','VDF_fftt1','VDF_cap1']]

# 显示每一列中的缺失值数量
print(df.isnull().sum())

# 返回重复的行数
print(df.duplicated().sum())

# 删除重复值 不改变源数据 临时生成的表
df.drop_duplicates(inplace=True)
df = df.loc[~(df['allowed_uses'] != "auto")]
df = df.loc[~(df['is_link'].eq(0))]

with open('./data/link_geo.csv','w+', encoding='utf-8') as f:
    for line in df.values:
        f.write((str(line[12])+'\n'))

# 清洗字符"LINSESTRING ("
with open('./data/link_geo.csv','r') as fr:
    lines = fr.readlines()
with open('./data/link_geo_temp1.csv','w') as fw:
    for line in lines:
        fw.write(line.replace('LINESTRING (',''))

# 清洗字符")"
with open('./data/link_geo_temp1.csv','r') as fr1:
    lines1 = fr1.readlines()
with open('./data/link_geo_temp2.csv','w') as fw1:
    for line1 in lines1:
        fw1.write(line1.replace(')',''))

# 清洗字符", "
with open('./data/link_geo_temp2.csv','r') as fr2:
    lines2 = fr2.readlines()
with open('./data/link_geo_temp3.csv','w') as fw2:
    for line2 in lines2:
        fw2.write(line2.replace(', ',','))

# 根据","对经纬度进行拆分,使得每一行只有一个经纬度
with open('./data/link_geo_temp3.csv', 'r') as infile, open('./data/link_geo_temp4.csv', 'w') as outfile:
    stripped = (line.strip() for line in infile)
    lines = ([sent] for para in (line.split(",") for line in stripped if line) for sent in para)
    writer = csv.writer(outfile)
    writer.writerows(lines)

# 添加字符",",使得文件成为两列,一列为lon,一列为lat
with open('./data/link_geo_temp4.csv','r') as fr3:
    lines3 = fr3.readlines()
with open('./data/link_geo_new.csv','w') as fw3:
    fw3.write('lon,lat\n')
    for line3 in lines3:
        fw3.write(line3.replace(' ',','))
