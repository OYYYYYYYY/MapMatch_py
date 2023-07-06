import pandas as pd
import random
import math
 
df = pd.read_csv("/data/oydata/Mapmatch_py/data/cd_taxi/cd_0625.csv")


# 只输出列名
print(df.columns.values)

df=df[['road','time','days','values']]

print(df.shape)

with open('/data/oydata/Mapmatch_py/data/cd_taxi/cd_0625_c.csv','w+', ) as f:
    f.write('3\n')
    f.write('7471 1080 28\n')
    for line in df.values:
        #str(line[0])：csv中第0列；+','+：csv两列之间保存到txt用逗号（，）隔开；'\n'：读取csv每行后在txt中换行
        f.write((str(int(line[1])))+' '+(str(int(line[1] - 360))+' '+str(int(line[2]))+' '+str(line[3] * 1.0000)+'\n'))