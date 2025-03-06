# import pandas as pd
# import sys
# import random
# import numpy as np

# def increase_random_rows(input_file, output_file, s, t):
#     # 读取CSV文件
#     df = pd.read_csv(input_file)
    
#     # 检查values列是否包含非有限值（NaN或inf）
#     if df['values'].isnull().any() or np.isinf(df['values']).any():
#         print("Warning: 'values' column contains NaN or inf values. These rows will be skipped.")
    
#     # 计算需要选取的行数
#     num_rows = len(df)
#     num_to_select = int(num_rows * s)
    
#     # 随机选择要增加的行索引
#     rows_to_increase = random.sample(range(num_rows), num_to_select)
    
#     # 增加选定行的values列的值，并确保结果为整数
#     # 使用pd.to_numeric处理非有限值
#     df['values'] = pd.to_numeric(df['values'], errors='coerce')  # 将非数值转换为NaN
#     df.loc[rows_to_increase, 'values'] = (df.loc[rows_to_increase, 'values'] * (1 + t / 100)).round().astype('Int64')  # 使用可空整数类型
    
#     # 保存结果到新的CSV文件
#     df.to_csv(output_file, index=False)

# if __name__ == "__main__":
#     if len(sys.argv) != 5:
#         print("Usage: python script.py input.csv output.csv s t")
#     else:
#         input_file = sys.argv[1]
#         output_file = sys.argv[2]
#         s = float(sys.argv[3])
#         t = float(sys.argv[4])
        
#         if s < 0 or s > 1:
#             print("Error: s should be between 0 and 1")
#         elif t < 0:
#             print("Error: t should be a non-negative number")
#         else:
#             increase_random_rows(input_file, output_file, s, t)
#             print(f"Randomly selected {s * 100}% of rows, increased their 'values' by {t}%, rounded to integers, and saved to {output_file}")

##########################################################################################################################################################
# # New version: generate two file, one store the error values, other values in another file
# import pandas as pd
# import sys
# import random
# import numpy as np

# def increase_random_rows(input_file, output_file_a, output_file_b, s, t):
#     # 读取CSV文件
#     df = pd.read_csv(input_file)
    
#     # 检查values列是否包含非有限值（NaN或inf）
#     if df['values'].isnull().any() or np.isinf(df['values']).any():
#         print("Warning: 'values' column contains NaN or inf values. These rows will be skipped.")
    
#     # 计算需要选取的行数
#     num_rows = len(df)
#     num_to_select = int(num_rows * s)
    
#     # 随机选择要增加的行索引
#     rows_to_increase = random.sample(range(num_rows), num_to_select)
    
#     # 创建两个DataFrame，一个用于存储修改过的行，一个用于存储未修改的行
#     df_a = pd.DataFrame()
#     df_b = pd.DataFrame()
    
#     # 增加选定行的values列的值，并确保结果为整数
#     # 使用pd.to_numeric处理非有限值
#     df['values'] = pd.to_numeric(df['values'], errors='coerce')  # 将非数值转换为NaN
    
#     for index, row in df.iterrows():
#         if index in rows_to_increase:
#             row['values'] = (row['values'] * (1 + t / 100)).round().astype('Int64')  # 使用可空整数类型
#             df_a = pd.concat([df_a, row.to_frame().T], ignore_index=True)
#         else:
#             df_b = pd.concat([df_b, row.to_frame().T], ignore_index=True)
    
#     # 保存结果到新的CSV文件
#     df_a.to_csv(output_file_a, index=False)
#     df_b.to_csv(output_file_b, index=False)

# if __name__ == "__main__":
#     if len(sys.argv) != 6:
#         print("Usage: python script.py input.csv output.csv.A output.csv.B s t")
#     else:
#         input_file = sys.argv[1]
#         output_file_a = sys.argv[2]
#         output_file_b = sys.argv[3]
#         s = float(sys.argv[4])
#         t = float(sys.argv[5])
        
#         if s < 0 or s > 1:
#             print("Error: s should be between 0 and 1")
#         elif t < 0:
#             print("Error: t should be a non-negative number")
#         else:
#             increase_random_rows(input_file, output_file_a, output_file_b, s, t)
#             print(f"Randomly selected {s * 100}% of rows, increased their 'values' by {t}%, rounded to integers, and saved to {output_file_a}")
#             print(f"The remaining rows are saved to {output_file_b}")
##########################################################################################################################################################
import pandas as pd
import random
import sys

def modify_csv(input_file, output_file_A, output_file_B, s, t):
    # 读取原始 CSV 文件
    df = pd.read_csv(input_file)

    # 随机选取百分之 s 的行
    total_rows = len(df)
    selected_indices = random.sample(range(total_rows), int(total_rows * s))

    # 对选中的行进行修改
    df_selected = df.loc[selected_indices].copy()
    df_selected['values'] = df_selected['values'] * (1 + t / 100)

    # 未修改的行
    df_unselected = df.drop(selected_indices)

    # 保存修改后的数据到新文件 A 和 B
    df_selected.to_csv(output_file_A, index=False)
    df_unselected.to_csv(output_file_B, index=False)

if __name__ == '__main__':
    # 从命令行获取参数
    if len(sys.argv) != 6:
        print("Usage: python script.py <input_file> <output_file_A> <output_file_B> <s> <t>")
        sys.exit(1)

    input_file = sys.argv[1]  # 原始文件路径
    output_file_A = sys.argv[2]  # 输出文件 A 路径
    output_file_B = sys.argv[3]  # 输出文件 B 路径
    s = float(sys.argv[4])  # 百分比 s
    t = int(sys.argv[5])  # 增加的百分比 t

    # 确保参数合法
    if not (0 <= s <= 1):
        print("Error: s must be between 0 and 1.")
        sys.exit(1)
    if not (0 <= t <= 100):
        print("Error: t must be between 0 and 100.")
        sys.exit(1)

    # 运行修改 CSV 的函数
    modify_csv(input_file, output_file_A, output_file_B, s, t)
    print(f"Process completed. Files '{output_file_A}' and '{output_file_B}' have been created.")

