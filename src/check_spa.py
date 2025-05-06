def analyze_tns_file(file_path):
    # 初始化变量
    row_count = 0
    col_count = 0
    values = []
    greater_than_099_count = 0

    # 打开文件并读取数据
    with open(file_path, 'r') as file:
        # 读取第一行，获取矩阵的行数和列数
        first_line = file.readline().strip()
        row_count, col_count = map(int, first_line.split())

        # 读取剩余行，提取value值
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:  # 确保是三元组
                value = float(parts[2])  # 提取value值
                values.append(value)
                if value > 0.99:
                    greater_than_099_count += 1

    # 计算统计结果
    if values:
        min_value = min(values)
        max_value = max(values)
        total_values = len(values)
        greater_than_099_ratio = greater_than_099_count / total_values

        # 输出结果
        print(f"Matrix dimensions: {row_count} rows x {col_count} columns")
        print(f"Minimum value: {min_value}")
        print(f"Maximum value: {max_value}")
        print(f"Number of values greater than 0.99: {greater_than_099_count}")
        print(f"Proportion of values greater than 0.99: {greater_than_099_ratio:.4f} ({greater_than_099_ratio * 100:.2f}%)")
    else:
        print("No values found in the file.")

# 示例调用
if __name__ == "__main__":
    file_path = "/data/oydata/MapMatch_py/data/cd_taxi/spa_mat.tns"  # 替换为你的文件路径
    analyze_tns_file(file_path)