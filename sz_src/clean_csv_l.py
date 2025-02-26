####################################################################################################
# # 筛选出初始csv文件中所需列并保存到新文件
# # 提取'on_date', 'on_longitude', 'on_latitude'保存为新文件 on_off-board_2015-XXX.csv
# # 提取'off_date', 'off_longitude', 'off_latitude'保存为新文件 off_off-board_2015-XXX.csv
# # 存在三个月份的文件，需要分别更改input_dir；存在两套数据：on/off，需要分别更改column_to_extract! 
# # 输出的所有的文件都存储在r1_data目录下
# import os
# import pandas as pd

# # 设置目标目录和新列名
# input_dir = '/data/oydata/MapMatch_py/data/large-scale_sz_taxi/raw_data/2015-08'  # 这里替换为你的目录路径
# output_dir = '/data/oydata/MapMatch_py/data/large-scale_sz_taxi/r1_data'  # 输出目录
# columns_to_extract = ['on_date', 'on_longitude', 'on_latitude']  # 需要提取的原始列名
# # columns_to_extract = ['off_date', 'off_longitude', 'off_latitude']  # 需要提取的原始列名
# new_columns = ['date', 'longitude', 'latitude']  # 新列名

# # 创建输出目录（如果不存在的话）
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)

# # 遍历目录中的所有CSV文件
# for filename in os.listdir(input_dir):
#     if filename.endswith('.csv'):  # 只处理CSV文件
#         file_path = os.path.join(input_dir, filename)
        
#         # 读取CSV文件
#         df = pd.read_csv(file_path)
        
#         # 检查是否包含指定的列
#         if all(col in df.columns for col in columns_to_extract):
#             # 提取指定列并重命名
#             df_extracted = df[columns_to_extract]
#             df_extracted.columns = new_columns
            
#             # 生成新的文件路径
#             output_file_path = os.path.join(output_dir, f'on_{filename}')
            
#             # 保存修改后的数据到新的CSV文件
#             df_extracted.to_csv(output_file_path, index=False)
#             print(f"处理完成: {output_file_path}")
#         else:
#             print(f"文件 {filename} 中没有找到所有指定列。")

# print('所有文件处理完成！')

####################################################################################################
# # 换算时间、将原文件的date列进行分割，将日期转换为从0开始的索引，时间仍然为原本的存储方式，将所有的文件都存储在r2_data目录下
# import os
# import pandas as pd


# # def calculate_day(row):
# #     # 提取月份和日期
# #     month = int(row['date'].split('T')[0][5:7])
# #     day = int(row['date'].split('T')[0][8:10])
    
# #     if (month == 8):
# #         return day - 10
# #     elif (month == 9):
# #         return day + 21
# #     elif (month == 10):
# #         return day + 51

# def process_csv_file(input_file, output_file):
#     # Read CSV file into pandas DataFrame
#     df = pd.read_csv(input_file)
    
#     # Convert 'date' field to 'day' and 'time' fields
#     df['day'] = df['date'].apply(lambda x: int(x.split('T')[0][-2:]) - 10)  # Calculate day index from date
#     # df['day'] = df['date'].apply(lambda x: int(x.split('T')[0][-2:]) + 21)  # Calculate day index from date
#     # df['day'] = df['date'].apply(lambda x: int(x.split('T')[0][-2:]) + 51)  # Calculate day index from date
#     # df['day'] = df.apply(calculate_day, axis=1)
   
#     df['time'] = df['date'].apply(lambda x: x.split('T')[1][:-1])  # Extract time without 'Z'
    
#     # Drop the original 'date' column if no longer needed
#     df.drop(columns=['date'], inplace=True)
    
#     # Save modified DataFrame to new CSV file
#     df.to_csv(output_file, index=False)

# if __name__ == "__main__":
#     input_directory = '/data/oydata/MapMatch_py/data/large-scale_sz_taxi/r1_data/2015-08'  # Replace with your input directory
#     output_directory = '/data/oydata/MapMatch_py/data/large-scale_sz_taxi/r2_data/2015-08'  # Replace with your output directory
    
#     # Ensure output directory exists
#     os.makedirs(output_directory, exist_ok=True)
    
#     # Process each CSV file in the input directory
#     for filename in os.listdir(input_directory):
#         if filename.endswith('.csv'):
#             input_file = os.path.join(input_directory, filename)
#             output_file = os.path.join(output_directory, filename)
            
#             # Process and save each CSV file
#             process_csv_file(input_file, output_file)
#             print(f"Processed {filename} and saved as {output_file}")

#     print('所有文件处理完成！')

####################################################################################################
# 合并目录下所有的csv文件为一个大的文件。在此，现将三个月的文件分别合并，再合并为一个大文件。
# import os
# import pandas as pd

# def merge_csv_files(input_directory, output_file):
#     # List all CSV files in the input directory
#     csv_files = [f for f in os.listdir(input_directory) if f.endswith('.csv')]
    
#     # Initialize an empty list to hold all dataframes
#     all_dataframes = []
    
#     # Read each CSV file and append to the list
#     for csv_file in csv_files:
#         file_path = os.path.join(input_directory, csv_file)
#         df = pd.read_csv(file_path)
#         all_dataframes.append(df)
    
#     # Concatenate all dataframes into one
#     combined_df = pd.concat(all_dataframes, ignore_index=True)
    
#     # Save the combined dataframe to a new CSV file
#     combined_df.to_csv(output_file, index=False)
#     print(f"Combined {len(csv_files)} CSV files into {output_file}")

# if __name__ == "__main__":
#     # input_directory = '/data/oydata/MapMatch_py/data/large-scale_sz_taxi/r2_data/2015-08'  # Replace with your input directory
#     # output_file = '/data/oydata/MapMatch_py/data/large-scale_sz_taxi/r2_data/combine/traj-08.csv'  # Replace with your output directory

#     input_directory = '/data/oydata/MapMatch_py/data/large-scale_sz_taxi/r2_data/combine'  # Replace with your input directory
#     output_file = '/data/oydata/MapMatch_py/data/large-scale_sz_taxi/r2_data/combine/traj.csv'  # Replace with your output directory
    
#     # Merge all CSV files in the input directory
#     merge_csv_files(input_directory, output_file)

####################################################################################################
# 对合并后的数据集的time列进行转换
import pandas as pd

def convert_time_to_minutes(df, time_column):
    def time_to_minutes(time_str):
        # Split time_str into hh:mm:ss and milliseconds
        time_parts = time_str.split('.')
        hhmmss = time_parts[0]  # "hh:mm:ss"
        
        # Extract hh, mm, ss
        hh, mm, ss = map(int, hhmmss.split(':'))
        
        # Calculate total minutes
        total_minutes = hh * 60 + mm
        
        # Handle milliseconds part if present
        if len(time_parts) > 1:
            milliseconds = float(time_parts[1]) / 1000.0  # Convert milliseconds to fraction of minute
            total_minutes += milliseconds
        
        return total_minutes
    
    df[time_column] = df[time_column].apply(time_to_minutes)
    return df

if __name__ == "__main__":
    input_file = '/data/oydata/MapMatch_py/data/large-scale_sz_taxi/r2_data/combine/traj.csv'  # Replace with your input file path
    output_file = '/data/oydata/MapMatch_py/data/large-scale_sz_taxi/r2_data/combine/traj_convert.csv'  # Replace with your output file path
    
    # Read CSV file into pandas DataFrame
    df = pd.read_csv(input_file)
    
    # Convert 'time' column to minutes
    df = convert_time_to_minutes(df, 'time')
    
    # Save modified DataFrame back to CSV
    df.to_csv(output_file, index=False)
    print(f"Converted 'time' column to minutes and saved to {output_file}")




