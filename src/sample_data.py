import pandas as pd
import sys

def process_file(input_file, output_file):
    # 读取CSV文件
    df = pd.read_csv(input_file)

    # 修改表头
    df.columns = ['longitude', 'latitude', 'day', 'time']
    
    # 交换 'day' 列和 'time' 列的位置
    df = df[['longitude', 'latitude', 'time', 'day']]

    # 对 'time' 列进行采样：保留 'time' 能整除5的行，并修改 'time' 列的值为原来的值整除5
    df_filtered = df[df['time'] % 5 == 0].copy()
    df_filtered['time'] = df_filtered['time'] // 5

    # 修改表头为新的格式
    df_filtered.columns = ['lng', 'lat', 'time', 'day']

    # 将修改后的数据保存到新文件
    df_filtered.to_csv(output_file, index=False)

if __name__ == "__main__":
    # 获取命令行参数，输入文件路径和输出文件路径
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # 处理文件
    process_file(input_file, output_file)
    print(f"处理完成，新文件已保存为：{output_file}")
