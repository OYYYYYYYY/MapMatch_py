import pandas as pd
import os
import re

def merge_csv():
    # 待处理的目录
    input_path = r'/data/oydata/MapMatch_py/data/cd_taxi/sample_data_60s/'
    result_path = r'/data/oydata/MapMatch_py/data/cd_taxi/sample_data_60s/'
    result_name = r'trajectory_cdc08.csv'
    # 进入工作目录
    os.chdir(input_path)
    # 获取该目录下所有文件的名字
    file_list = os.listdir()
    print(file_list)
    # file_list.sort(key=lambda x:int(x[:-4]))   # x[:-4]文件名从右往左数，去掉后缀.csv，只进行数字的排序
	# file_list.sort()
    # print(file_list) 
    # 读取第一个CSV文件并包含表头
    df = pd.read_csv(input_path + file_list[0], encoding= 'gbk')  # 编码默认UTF-8,根据需要需改
    # 将读取的第一个CSV文件写入合并后的文件保存
    df.to_csv(result_path + result_name, index=False)
    # 循环遍历列表中各个CSV文件名，并追加到合并后的文件
    for i in range(1, len(file_list)):
        # 过滤隐藏文件
        if not file_list[i].startswith("."):
            # 根据文件名读取文件
            df = pd.read_csv(input_path + file_list[i])
            # index=True 在最左侧新增索引列；header=True  保留 表头, 后面的文件不保留表头
            df.to_csv(result_path + result_name, index=False, header=False, mode='a+')

if __name__ == '__main__':
    merge_csv()