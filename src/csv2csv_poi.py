# clean poi.csv
import pandas as pd
import random
import math
 
# print(random.randint(0,9))
df = pd.read_csv("./data/poi.csv")

# print(type(df))
# 只输出列名
print(df.columns.values)

df=df[['name','poi_id','osm_way_id','osm_relation_id','building','amenity','leisure','way','geometry','centroid','area','area_ft2']]
# 结果  (行数,列数)
print(df.shape)

#trip_distance取整

# df['trip_distance']=df['trip_distance'].apply(lambda x: int(math.ceil(10*x)+1))

# 显示每一列中的缺失值数量
print(df.isnull().sum())

# 返回重复的行数
print(df.duplicated().sum())

# 删除重复值 不改变源数据 临时生成的表
df.drop_duplicates(inplace=True)

# 返回重复的行数
# print(df['trip_distance'].duplicated().sum())






# 删除符合条件的指定行，并替换原始df
print(df.head(10))
print(df.shape)

# df.drop(df[df.trip_distance == 0.00].index, inplace=True) 

with open('./data/poi_sample.csv','w+', encoding='utf-8') as f:
    f.write('poi_id,osm_way_id,geometry,centroid\n')
    # f.write((str(max(df.trip_distance))+'\t'+str(max(df.PULocationID))+'\t'+str(max(df.DOLocationID))+'\n'))
    for line in df.values:
        #str(line[0])：csv中第0列；+','+：csv两列之间保存到txt用逗号（，）隔开；'\n'：读取csv每行后在txt中换行
        f.write((str(line[1])+','+str(line[2])+','+str(line[8])+','+str(line[9])+'\n'))