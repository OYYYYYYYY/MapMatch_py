import pandas as pd
import sys

def process_csv(input_file, output_file):
    # 读取 CSV 文件
    df = pd.read_csv(input_file)

    # 删除 'from_node_id' 和 'to_node_id' 列
    df = df.drop(columns=['from_node_id', 'to_node_id'])

    # 将 'link_id' 列的值重新命名为从0开始递增的数字
    df['link_id'] = range(len(df))

    # 保存处理后的数据到新的文件
    df.to_csv(output_file, index=False)

    print(f"已处理并保存到 {output_file} 文件中。")

if __name__ == '__main__':
    # 获取命令行参数
    if len(sys.argv) != 3:
        print("用法：python process_csv.py <input_file.csv> <output_file.csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    process_csv(input_file, output_file)
