import pandas as pd
import sys

def extract_data(file_a, file_b, output_file):
    # 读取文件A和文件B
    df_a = pd.read_csv(file_a)
    df_b = pd.read_csv(file_b)
    
    # 只保留文件A中的需要的列
    required_columns_a = ['link_id', 'length', 'lanes', 'link_type']
    df_a_filtered = df_a[required_columns_a]

    # 根据file_b中的link_id提取file_a的相关行
    df_b_link_ids = df_b['link_id'].unique()  # 获取文件B中所有唯一的link_id
    result_df = df_a_filtered[df_a_filtered['link_id'].isin(df_b_link_ids)]
    
    # 保存提取的结果到新的CSV文件
    result_df.to_csv(output_file, index=False)

# 从命令行参数获取输入文件和输出文件
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python extract_data.py <file_a.csv> <file_b.csv> <output_file.csv>")
    else:
        file_a = sys.argv[1]
        file_b = sys.argv[2]
        output_file = sys.argv[3]
        extract_data(file_a, file_b, output_file)
        print(f"提取的结果已经保存到: {output_file}")
