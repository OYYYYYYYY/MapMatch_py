import pandas as pd
import random
import math
import sys


def main(argv):
    input = argv[1]
    output = argv[2]
    # # poi.csv clean code
    # df = pd.read_csv(input)

    # # 只输出列名
    # print(df.columns.values)

    # df=df[['name','poi_id','osm_way_id','osm_relation_id','building','amenity','leisure','way','geometry','centroid','area','area_ft2']]
    # # 结果  (行数,列数)
    # print(df.shape)

    # # 显示每一列中的缺失值数量
    # print(df.isnull().sum())

    # # 返回重复的行数
    # print(df.duplicated().sum())

    # # 删除重复值 不改变源数据 临时生成的表
    # df.drop_duplicates(inplace=True)

    # with open(output,'w+', encoding='utf-8') as f:
    #     f.write('name,poi_id,osm_way_id\n')
    #     for line in df.values:
    #         #str(line[0])：csv中第0列；+','+：csv两列之间保存到txt用逗号（，）隔开；'\n'：读取csv每行后在txt中换行
    #         f.write((str(line[0])+','+str(line[1])+','+str(line[2])+'\n'))

    # df1 = pd.read_csv(output1)

    # # 只输出列名
    # print(df1.columns.values)
    # print(df1.head(10))
    # print(df1.shape)
    # df1 = df1[['name','poi_id','osm_way_id']]
    # df1 = df1.loc[~(df1['name'] == 'blank')]
    # df1.to_csv(output2, index = False)

if __name__ == '__main__':
    sys.exit(main(sys.argv))