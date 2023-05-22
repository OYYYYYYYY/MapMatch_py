# clean node.csv
import pandas as pd
import random
import math

df = pd.read_csv("./data/node.csv")

# 只输出列名
print(df.columns.values)

df=df[['name','node_id','osm_node_id','osm_highway','zone_id','ctrl_type','node_type','activity_type','is_boundary','x_coord','y_coord','intersection_id','poi_id','notes']]
# 结果  (行数,列数)
print(df.shape)

# 显示每一列中的缺失值数量
print(df.isnull().sum())

# 返回重复的行数
print(df.duplicated().sum())

# 删除重复值 不改变源数据 临时生成的表
df.drop_duplicates(inplace=True)


# 删除符合条件的指定行，并替换原始df
print(df.head(10))
print(df.shape)

# df.drop(df[df.trip_distance == 0.00].index, inplace=True) 

with open('./data/node_sample.csv','w+', encoding='utf-8') as f:
    f.write('node_id,osm_node_id,x_coord,y_coord,intersection_id,poi_id\n')
    for line in df.values:
        #str(line[0])：csv中第0列；+','+：csv两列之间保存到txt用逗号（，）隔开；'\n'：读取csv每行后在txt中换行
        f.write((str(line[1])+','+str(line[2])+','+str(line[9])+','+str(line[10])+','+str(line[11])+','+str(line[12])+'\n'))