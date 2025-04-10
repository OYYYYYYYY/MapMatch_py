import pandas as pd
import sys

def select_random_rows(input_file, output_file, num_rows):
    # 读取 CSV 文件
    df = pd.read_csv(input_file)

    # 随机选取指定数量的行
    random_rows = df.sample(n=num_rows, random_state=42)

    # 将随机选取的行保存到新文件
    random_rows.to_csv(output_file, index=False)

    print(f"已随机选取 {num_rows} 行，并保存到 {output_file} 文件中。")

if __name__ == '__main__':
    # 获取命令行参数
    if len(sys.argv) != 4:
        print("用法：python select_random_rows.py <input_file.csv> <output_file.csv> <num_rows>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    num_rows = int(sys.argv[3])

    select_random_rows(input_file, output_file, num_rows)
