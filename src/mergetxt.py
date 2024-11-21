import os

# 设置目标文件夹和合并后的文件名
folder_path = '/data/oydata/MapMatch_py/data/san_taxi/raw_data'
output_file = '/data/oydata/MapMatch_py/data/san_taxi/raw_data/merged.csv'

# 获取目标文件夹中所有txt文件的文件名列表
file_list = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

# 打开合并后的文件，使用 'a' 模式追加写入
with open(os.path.join(folder_path, output_file), 'a', encoding='utf-8') as outfile:
    # 遍历每个txt文件并逐行写入合并后的文件
    for file_name in file_list:
        with open(os.path.join(folder_path, file_name), 'r', encoding='utf-8') as infile:
            outfile.write(infile.read())
            # outfile.write('\n')  # 可选：在每个文件内容后加入换行符，使得合并后的内容更易读