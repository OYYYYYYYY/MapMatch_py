import pandas as pd
import sys

def process_file(input_file, output_file):
    # 读取CSV文件
    df = pd.read_csv(input_file)

    # 重新标号 'road_id' 列，新的 road_id 值从 0 开始，递增
    df['link_id'] = range(len(df))

    # 将修改后的数据保存到新文件
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    # 获取命令行参数，输入文件路径和输出文件路径
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # 处理文件
    process_file(input_file, output_file)
    print(f"处理完成，新文件已保存为：{output_file}")
