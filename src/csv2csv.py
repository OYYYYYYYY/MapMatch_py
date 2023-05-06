# clean csv file to csv file
import pandas as pd
import random
import math
 
# print(random.randint(0,9))
df = pd.read_csv("demand_2016.08.08_510100_.csv")

# print(type(df))
# 只输出列名
print(df.columns.values)

# df=df[['pickup_datetime','pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude']]
f=df[['hour','longitude','latitude']]
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
# print(((str(max(df.trip_distance))+'\t'+str(max(df.PULocationID))+'\t'+str(max(df.DOLocationID))+'\n')))
# df.drop(df[df.trip_distance == 0.00].index, inplace=True) 
# print(df.head(10))
# print(max(df.trip_distance))

with open('chengdu201608.csv','w+', encoding='utf-8') as f:
    f.write('hour,lon,lat\n')
    # f.write((str(max(df.trip_distance))+'\t'+str(max(df.PULocationID))+'\t'+str(max(df.DOLocationID))+'\n'))
    for line in df.values:
        #str(line[0])：csv中第0列；+','+：csv两列之间保存到txt用逗号（，）隔开；'\n'：读取csv每行后在txt中换行
        f.write((str(line[1])+','+str(line[2])+','+str(line[3])+'\n'))