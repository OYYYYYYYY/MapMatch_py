####################################################################################################
# # 对每个.csv文件的time列进行转换
# import pandas as pd
# import os

# def convert_time_to_minutes(df, time_column):
#     def time_to_minutes(time_str):
#         # Split time_str into hh:mm:ss and milliseconds
#         time_parts = time_str.split('.')
#         hhmmss = time_parts[0]  # "hh:mm:ss"
        
#         # Extract hh, mm, ss
#         hh, mm, ss = map(int, hhmmss.split(':'))
        
#         # Calculate total minutes
#         total_minutes = hh * 60 + mm
        
#         # Handle milliseconds part if present
#         if len(time_parts) > 1:
#             milliseconds = float(time_parts[1]) / 1000.0  # Convert milliseconds to fraction of minute
#             total_minutes += milliseconds
        
#         return total_minutes
    
#     df[time_column] = df[time_column].apply(time_to_minutes)
#     return df

# def process_directory(input_dir, output_dir, time_column='time'):
#     # Ensure output directory exists
#     os.makedirs(output_dir, exist_ok=True)
    
#     # Iterate over all files in the input directory
#     for filename in os.listdir(input_dir):
#         if filename.endswith('.csv'):  # Check if the file is a CSV file
#             input_file = os.path.join(input_dir, filename)
#             output_file = os.path.join(output_dir, f"converted_{filename}")
            
#             try:
#                 # Read the CSV file into pandas DataFrame
#                 df = pd.read_csv(input_file)
                
#                 # Convert the 'time' column to minutes
#                 df = convert_time_to_minutes(df, time_column)
                
#                 # Save the modified DataFrame back to CSV
#                 df.to_csv(output_file, index=False)
#                 print(f"Converted 'time' column to minutes and saved to {output_file}")
#             except Exception as e:
#                 print(f"Failed to process {input_file}: {e}")

# if __name__ == "__main__":
#     input_dir = '/data/oydata/MapMatch_py/data/cd_taxi/cleaned_data'  # Replace with your input file path
#     output_dir = '/data/oydata/MapMatch_py/data/cd_taxi/cleaned_data/convert_data'  # Replace with your output file path
    
#     # Process all CSV files in the directory
#     process_directory(input_dir, output_dir)

####################################################################################################
# # 根据时间间隔进行采样
# import pandas as pd
# import os

# def filter_rows_by_time(df, time_column='time'):
#     # 保留 time 列值能整除 5 的行
#     filtered_df = df[df[time_column] % 10 == 0]
#     return filtered_df

# def process_directory(input_dir, output_dir, time_column='time'):
#     # 确保输出目录存在
#     os.makedirs(output_dir, exist_ok=True)
    
#     # 遍历输入目录下的所有文件
#     for filename in os.listdir(input_dir):
#         if filename.endswith('.csv'):  # 如果是 CSV 文件
#             input_file = os.path.join(input_dir, filename)
#             output_file = os.path.join(output_dir, f"filtered_{filename}")
            
#             try:
#                 # 读取 CSV 文件到 pandas DataFrame
#                 df = pd.read_csv(input_file)
                
#                 # 过滤符合条件的行
#                 df_filtered = filter_rows_by_time(df, time_column)
                
#                 # 将过滤后的 DataFrame 保存到新的 CSV 文件
#                 df_filtered.to_csv(output_file, index=False)
#                 print(f"Processed {filename} and saved to {output_file}")
#             except Exception as e:
#                 print(f"Failed to process {input_file}: {e}")

# if __name__ == "__main__":
#     input_dir = '/data/oydata/MapMatch_py/data/cd_taxi/cleaned_data/convert_data'  # 输入目录
#     output_dir = '/data/oydata/MapMatch_py/data/cd_taxi/cleaned_data/convert_data/sample_data_10'  # 输出目录
    
#     # 处理目录中的所有 CSV 文件
#     process_directory(input_dir, output_dir)

####################################################################################################

# 合并目录下所有的csv文件为一个大的文件
import os
import pandas as pd

def merge_csv_files(input_directory, output_file):
    # List all CSV files in the input directory
    csv_files = [f for f in os.listdir(input_directory) if f.endswith('.csv')]
    
    # Initialize an empty list to hold all dataframes
    all_dataframes = []
    
    # Read each CSV file and append to the list
    for csv_file in csv_files:
        file_path = os.path.join(input_directory, csv_file)
        df = pd.read_csv(file_path)
        all_dataframes.append(df)
    
    # Concatenate all dataframes into one
    combined_df = pd.concat(all_dataframes, ignore_index=True)
    
    # Save the combined dataframe to a new CSV file
    combined_df.to_csv(output_file, index=False)
    print(f"Combined {len(csv_files)} CSV files into {output_file}")

if __name__ == "__main__":
    # input_directory = '/data/oydata/MapMatch_py/data/cd_taxi/cleaned_data/convert_data/sample_data_10'  # Replace with your input directory
    # output_file = '/data/oydata/MapMatch_py/data/cd_taxi/cleaned_data/convert_data/tra_sample_10.csv'  # Replace with your output directory
    input_directory = '/data/oydata/MapMatch_py/data/cd_taxi/paper2/req_sample_5min'  # Replace with your input directory
    output_file = '/data/oydata/MapMatch_py/data/cd_taxi/paper2/tra_sample_5min_convert.csv'  # Replace with your output directory
    
    # Merge all CSV files in the input directory
    merge_csv_files(input_directory, output_file)

####################################################################################################

# import pandas as pd
# import numpy as np
# import csv
# import math
# import sys


# def main(argv):

#     input_directory = '/data/oydata/MapMatch_py/data/cd_taxi/cleaned_data'  # Replace with your input directory
#     output_file = '/data/oydata/MapMatch_py/data/cd_taxi/cleaned_data/traj_sample_5.csv'  # Replace with your output directory

#     count = 0
#     min = 18 * 3600 + 60 * 60
#     h_min = 24
#     m_min = 61
#     s_min = 61
#     # 读取数据文件
#     # input = argv[1]
#     # output = argv[2]
#     with open(input, 'rt') as f:
#         reader = csv.DictReader(f)
#         lngs = []
#         lats = []
#         times = []
#         days = []
#         for row in reader :
#         # 将经纬度字符串转换为数值
#             temp0 = float(row['lng'])
#             temp1 = float(row['lat'])
#         # 将时间字符串转换为数值
#             h, m, s = row['time'].strip().split(':')
#             temp2 = (int(h) - 6) * 3600 + int(m) * 60 + int(s)
#             temp3 = int(row['day'])
#             # 采样的时间间隔
#             if(int(s) % 60 == 0):
#                 lngs.append(temp0)
#                 lats.append(temp1)
#                 times.append(temp2 / 60)
#                 days.append(temp3)
#             elif(row['time'] == '23:59:59'):
#                 lngs.append(temp0)
#                 lats.append(temp1)
#                 times.append(temp2 / 60 + 1)
#                 days.append(temp3)
#                 count = count + 1
#     print(count)

#     print("read data file")
#     with open(output,'w') as fw:
#         fw.write('lng,lat,time,day\n')
#         for s in range(len(lngs)):
#             fw.write((str(lngs[s])+','+str(lats[s])+','+str(times[s])+','+str(days[s])+'\n'))

# if __name__ == '__main__':
#     sys.exit(main(sys.argv))