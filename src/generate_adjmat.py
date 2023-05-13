import pandas as pd
import random
import math

df = pd.read_csv("/data/oydata/Mapmatch_py/data/link_adj.csv")
print(df.columns.values)
f=df[['name','link_id','osm_way_id','from_node_id','to_node_id','geometry']]

# 显示每一列中的缺失值数量
print(df.isnull().sum())

# 返回重复的行数
print(df.duplicated().sum())

# 删除重复值 不改变源数据 临时生成的表
df.drop_duplicates(inplace=True)
df = df.loc[~(df['allowed_uses'] != "auto")]

with open('./data/adj.mat','w+', encoding='utf-8') as f:
    f.write('2\n')
    f.write('\n')
    for line in df.values:
        f.write((str(line[3])+' '+str(line[4])+' 1\n'))
