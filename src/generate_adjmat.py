import pandas as pd
import random
import math

df = pd.read_csv("link_sample.csv")
print(df.columns.values)
f=df[['name','link_id','osm_way_id','from_node_id','to_node_id','dir_flag','length','lanes','free_speed','capacity','link_type_name','link_type','geometry','allowed_uses','from_biway','is_link','VDF_fftt1','VDF_cap1']]

# 显示每一列中的缺失值数量
print(df.isnull().sum())

# 返回重复的行数
print(df.duplicated().sum())

# 删除重复值 不改变源数据 临时生成的表
df.drop_duplicates(inplace=True)
df = df.loc[~(df['allowed_uses'] != "auto")]

with open('./sz/adj.mat','w+', encoding='utf-8') as f:
    f.write('2\n')
    f.write('\n')
    for line in df.values:
        f.write((str(line[3])+' '+str(line[4])+' 1\n'))
