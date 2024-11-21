# import pandas as pd

# # 读取原始的CSV文件
# df = pd.read_csv('/data/oydata/MapMatch_py/data/week_sz_taxi/poi.csv')

# # 提取lng和lat信息并创建新的DataFrame
# # df['lng'] = df['centroid'].str.extract(r'POINT \((\d+.\d+) \d+.\d+\)').astype(float)
# # df['lat'] = df['centroid'].str.extract(r'POINT \(\d+.\d+ (\d+.\d+)\)').astype(float)

# # 只保留lng和lat两列，创建新的DataFrame
# df_result = df[['centroid']]

# # 保存处理后的结果为新的CSV文件
# df_result.to_csv('/data/oydata/MapMatch_py/data/week_sz_taxi/poi_c.csv', index=False)


import pandas as pd

def clean_centroid_column(csv_file):
    # 读取CSV文件
    df = pd.read_csv(csv_file)

    # 处理centroid列
    df['centroid'] = df['centroid'].str.replace('POINT ', '')  # 去掉 'POINT '
    df['centroid'] = df['centroid'].str.replace('(', '')  # 去掉括号和空格
    df['centroid'] = df['centroid'].str.replace(')', '')  # 去掉括号和空格
    df['centroid'] = df['centroid'].str.replace(' ', '')  # 去掉括号和空格

    # 保存处理后的文件
    df.to_csv('/data/oydata/MapMatch_py/data/week_sz_taxi/poi_c0.csv', index=False)

if __name__ == "__main__":
    csv_file = '/data/oydata/MapMatch_py/data/week_sz_taxi/poi_c.csv'  # 替换为实际的CSV文件路径
    clean_centroid_column(csv_file)

