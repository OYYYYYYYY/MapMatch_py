####################################################################################################
# 筛选出初始csv文件中所需列并保存到新文件
import os
import pandas as pd

# 设置目录路径
directory_path = '/data/oydata/MapMatch_py/data/week_sz_taxi/raw_data'
new_directory_path = '/data/oydata/MapMatch_py/data/week_sz_taxi/r1_data'

# 获取目录下所有csv文件并处理
csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]
for csv_file in csv_files:
    csv_path = os.path.join(directory_path, csv_file)
    
    # 使用Pandas读取CSV文件
    df = pd.read_csv(csv_path)
    
    # 检查是否存在名为'no'的列，并删除
    if 'sequence' in df.columns:
        df.drop(columns=['sequence'], inplace=True)

    if 'off_date' in df.columns:
        df.drop(columns=['off_date'], inplace=True)

    if 'off_longitude' in df.columns:
        df.drop(columns=['off_longitude'], inplace=True)

    if 'off_latitude' in df.columns:
        df.drop(columns=['off_latitude'], inplace=True)
    
    new_csv_path = os.path.join(new_directory_path, f"r1_{csv_file}")
    # 保存修改后的数据回CSV文件
    df.to_csv(csv_path, index=False)

    print(f'文件 {csv_file} 处理完成')

print('所有文件处理完成！')

####################################################################################################

# import os
# import pandas as pd

# def process_csv_file(input_file, output_file):
#     # Read CSV file into pandas DataFrame
#     df = pd.read_csv(input_file)
    
#     # Convert 'on_date' field to 'day' and 'time' fields
#     df['day'] = df['on_date'].apply(lambda x: int(x.split('T')[0][-2:]) - 1)  # Calculate day index from date
#     df['time'] = df['on_date'].apply(lambda x: x.split('T')[1][:-1])  # Extract time without 'Z'
    
#     # Drop the original 'on_date' column if no longer needed
#     df.drop(columns=['on_date'], inplace=True)
    
#     # Save modified DataFrame to new CSV file
#     df.to_csv(output_file, index=False)

# if __name__ == "__main__":
#     input_directory = '/data/oydata/MapMatch_py/data/week_sz_taxi/r_data'  # Replace with your input directory
#     output_directory = '/data/oydata/MapMatch_py/data/week_sz_taxi/r1_data'  # Replace with your output directory
    
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

####################################################################################################

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
#     input_directory = '/data/oydata/MapMatch_py/data/week_sz_taxi/r1_data'  # Replace with your input directory
#     output_file = '/data/oydata/MapMatch_py/data/week_sz_taxi/r1_data/traj.csv'  # Replace with your output directory
    
#     # Merge all CSV files in the input directory
#     merge_csv_files(input_directory, output_file)

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
    input_file = '/data/oydata/MapMatch_py/data/week_sz_taxi/traj.csv'  # Replace with your input file path
    output_file = '/data/oydata/MapMatch_py/data/week_sz_taxi/traj_t.csv'  # Replace with your output file path
    
    # Read CSV file into pandas DataFrame
    df = pd.read_csv(input_file)
    
    # Convert 'time' column to minutes
    df = convert_time_to_minutes(df, 'time')
    
    # Save modified DataFrame back to CSV
    df.to_csv(output_file, index=False)
    print(f"Converted 'time' column to minutes and saved to {output_file}")




