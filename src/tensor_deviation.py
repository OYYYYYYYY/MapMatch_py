import pandas as pd
import sys
import random
import numpy as np

def increase_random_rows(input_file, output_file, s, t):
    # 读取CSV文件
    df = pd.read_csv(input_file)
    
    # 检查values列是否包含非有限值（NaN或inf）
    if df['values'].isnull().any() or np.isinf(df['values']).any():
        print("Warning: 'values' column contains NaN or inf values. These rows will be skipped.")
    
    # 计算需要选取的行数
    num_rows = len(df)
    num_to_select = int(num_rows * s)
    
    # 随机选择要增加的行索引
    rows_to_increase = random.sample(range(num_rows), num_to_select)
    
    # 增加选定行的values列的值，并确保结果为整数
    # 使用pd.to_numeric处理非有限值
    df['values'] = pd.to_numeric(df['values'], errors='coerce')  # 将非数值转换为NaN
    df.loc[rows_to_increase, 'values'] = (df.loc[rows_to_increase, 'values'] * (1 + t / 100)).round().astype('Int64')  # 使用可空整数类型
    
    # 保存结果到新的CSV文件
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py input.csv output.csv s t")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        s = float(sys.argv[3])
        t = float(sys.argv[4])
        
        if s < 0 or s > 1:
            print("Error: s should be between 0 and 1")
        elif t < 0:
            print("Error: t should be a non-negative number")
        else:
            increase_random_rows(input_file, output_file, s, t)
            print(f"Randomly selected {s * 100}% of rows, increased their 'values' by {t}%, rounded to integers, and saved to {output_file}")