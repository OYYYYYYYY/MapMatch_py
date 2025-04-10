import pandas as pd
import os

def process_file(file_path, output_dir):
    # 读取CSV文件
    df = pd.read_csv(file_path)
    
    # 检查是否包含"road", "time", "days", "values"四列
    if not all(col in df.columns for col in ['road', 'time', 'days', 'values']):
        print(f"文件 {file_path} 缺少必要的列")
        return
    
    # 统计重复行的数量
    duplicate_rows = df.duplicated(subset=['road', 'time', 'days'], keep=False).sum()
    
    # 统计每一行的重复次数，计算合并的"values"
    df['count'] = df.groupby(['road', 'time', 'days'])['values'].transform('size')
    
    # 删除重复行，只保留唯一的组合，并将"values"更新为重复的数量
    df_unique = df.drop_duplicates(subset=['road', 'time', 'days']).reset_index(drop=True)
    
    # 将"values"更新为重复的数量
    df_unique['values'] = df_unique['count']
    
    # 删除中间计算的"count"列
    df_unique = df_unique.drop(columns=['count'])
    
    # 生成输出文件的路径
    output_path = os.path.join(output_dir, os.path.basename(file_path))
    
    # 输出结果到新的CSV文件
    df_unique.to_csv(output_path, index=False)
    
    # 输出重复行的数量
    print(f"文件 {file_path} 存在 {duplicate_rows} 行重复数据，已处理并保存为 {output_path}")

def process_directory(directory_path, output_dir):
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 遍历目录中的所有CSV文件
    for filename in os.listdir(directory_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory_path, filename)
            process_file(file_path, output_dir)

# 设置目录路径
input_directory = '/data/oydata/MapMatch_py/data/large-scale_sz_taxi/after_mm'
output_directory = '/data/oydata/MapMatch_py/data/large-scale_sz_taxi/after_req'

# 处理目录下的所有CSV文件
process_directory(input_directory, output_directory)
