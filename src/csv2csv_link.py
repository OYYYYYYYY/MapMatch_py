#clean link.csv
import pandas as pd
import random
import math
import sys

def main(argv):
    input = argv[1]
    output = argv[2]

    df = pd.read_csv(input)

    # 只输出列名
    print(df.columns.values)
    df=df[['name','link_id','osm_way_id','from_node_id','to_node_id','dir_flag','length','lanes','free_speed','capacity','link_type_name','link_type','geometry','allowed_uses','from_biway','is_link','VDF_fftt1','VDF_cap1']]
    # 结果  (行数,列数)
    print(df.shape)

    # 显示每一列中的缺失值数量
    print(df.isnull().sum())
    # 返回重复的行数
    print(df.duplicated().sum())

    # 删除重复值 不改变源数据 临时生成的表 && 删除符合条件的指定行，并替换原始df
    df.drop_duplicates(inplace=True)
    df = df.loc[~(df['allowed_uses'] != "auto")]
    df = df.loc[~(df['is_link'].eq(0))]

    print(df.head(10))
    print(df.shape)

    with open(output,'w+', encoding='utf-8') as f:
        f.write('link_id,osm_way_id,from_node_id,to_node_id,geometry\n')
        for line in df.values:
            f.write((str(line[1])+','+str(line[2])+','+str(line[3])+','+str(line[4])+','+str(line[12])+'\n'))

    print("finish")

if __name__ == '__main__':
    sys.exit(main(sys.argv))


####################################################################################################

# import pandas as pd

# def remove_columns_and_save(input_file, output_file, columns_to_remove):
#     # Read CSV file into pandas DataFrame
#     df = pd.read_csv(input_file)
    
#     # Remove specified columns
#     df.drop(columns=columns_to_remove, inplace=True, errors='ignore')
    
#     # Save modified DataFrame back to CSV
#     df.to_csv(output_file, index=False)
#     print(f"Saved modified DataFrame to {output_file}")

# if __name__ == "__main__":
#     input_file = '/data/oydata/MapMatch_py/data/week_sz_taxi/link_single.csv'  # Replace with your input file path
#     output_file = '/data/oydata/MapMatch_py/data/week_sz_taxi/link_single_rm.csv'  # Replace with your output file path
#     columns_to_remove = ['to_node_id', 'from_node_id']  # List of columns to remove
    
#     # Remove specified columns and save to new file
#     remove_columns_and_save(input_file, output_file, columns_to_remove)
