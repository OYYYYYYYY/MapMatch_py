import pandas as pd
import random
import sys

def missing_data(file_path, output_path, missing_type, rate):
    # 读取 CSV 文件
    df = pd.read_csv(file_path)

    if missing_type == 'road':
        # 第一个维度：road缺失
        road_values = df['road'].unique()  # 获取所有road的值
        # 随机选取rate%的road值
        num_road_to_remove = int(len(road_values) * rate / 100)
        roads_to_remove = random.sample(list(road_values), num_road_to_remove)
        
        # 过滤掉这些road值对应的行
        df_filtered = df[~df['road'].isin(roads_to_remove)]
    
    elif missing_type == 'time':
        # 第二个维度：time缺失
        time_values = df['time'].unique()  # 获取所有time的值
        # 随机选取rate%的time值
        num_time_to_remove = int(len(time_values) * rate / 100)
        time_to_remove = random.sample(list(time_values), num_time_to_remove)
        
        # 过滤掉这些time值对应的行
        df_filtered = df[~df['time'].isin(time_to_remove)]
    
    elif missing_type == 'days':
        # 第三个维度：days缺失
        days_values = df['days'].unique()  # 获取所有days的值
        # 随机选取rate%的days值
        num_days_to_remove = int(len(days_values) * rate / 100)
        days_to_remove = random.sample(list(days_values), num_days_to_remove)
        
        # 过滤掉这些days值对应的行
        df_filtered = df[~df['days'].isin(days_to_remove)]
    
    elif missing_type == 'random':
        # 随机缺失：随机丢弃rate%的行
        num_rows_to_remove = int(len(df) * rate / 100)
        rows_to_remove = random.sample(range(len(df)), num_rows_to_remove)
        
        # 过滤掉这些行
        df_filtered = df.drop(rows_to_remove)

    # 保存到新的文件
    df_filtered.to_csv(output_path, index=False)

    print(f"缺失处理完成，保存到 {output_path}")

def main():
    # 从命令行参数获取输入
    if len(sys.argv) != 5:
        print("Usage: python script_name.py <input_csv> <output_csv> <missing_type> <rate>")
        sys.exit(1)

    file_path = sys.argv[1]
    output_path = sys.argv[2]
    missing_type = sys.argv[3].strip().lower()
    rate = int(sys.argv[4])

    if missing_type not in ['road', 'time', 'days', 'random']:
        print("缺失类型无效。有效类型为：road, time, days, random")
        sys.exit(1)

    if rate < 0 or rate > 100:
        print("缺失比例无效。比例应该在 0 到 100 之间。")
        sys.exit(1)

    # 调用函数处理缺失
    missing_data(file_path, output_path, missing_type, rate)

if __name__ == "__main__":
    main()
