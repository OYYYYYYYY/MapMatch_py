#clean link.csv
import pandas as pd
import random
import math

df = pd.read_csv("./data/cd_taxi/link.csv")

# print(type(df))
# 只输出列名
print(df.columns.values)

f=df[['name','link_id','osm_way_id','from_node_id','to_node_id','dir_flag','length','lanes','free_speed','capacity','link_type_name','link_type','geometry','allowed_uses','from_biway','is_link','VDF_fftt1','VDF_cap1']]
# 结果  (行数,列数)
print(df.shape)

# 显示每一列中的缺失值数量
print(df.isnull().sum())

# 返回重复的行数
print(df.duplicated().sum())

# 删除重复值 不改变源数据 临时生成的表
df.drop_duplicates(inplace=True)
df = df.loc[~(df['allowed_uses'] != "auto")]
df = df.loc[~(df['is_link'].eq(0))]


# 删除符合条件的指定行，并替换原始df
print(df.head(10))
print(df.shape)

with open('./data/cd_taxi/link_auto.csv','w+', encoding='utf-8') as f:
    f.write('link_id,from_node_id,to_node_id,geometry\n')
    print("in file\n")
    for line in df.values:
        #str(line[0])：csv中第0列；+','+：csv两列之间保存到txt用逗号（，）隔开；'\n'：读取csv每行后在txt中换行
        f.write((str(line[1])+','+str(line[3])+','+str(line[4])+','+str(line[12])+'\n'))

print("finish")