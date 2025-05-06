######
数据清洗

check_csv.py  检查csv文件中是否有超过维度规模的数据,打印"超过维度规模的行的数据","每个维度超过规模的数据数量";输入为sys一个文件;无输出

check_naninf.py  检查csv文件中的values列(l11可修改)的NaN/inf的数量并输出,再将这些行筛去,剩余的行保存到新文件;输入为sys一个目录;输出为sys一个目录

check_spa.py  检查空间相似矩阵spatial matrix,打印"矩阵的行列","value的最大最小值","大于0.99的值的数量和比例";输入为python文件内绝对路径;无输出

clean_csv.py  对csv文件进行清洗,筛选出需要的数据输出到新文件;输入为sys一个文件;输出为sys一个文件

clean_data.py  对得到的张量数据进行清洗,原来的张量数据在时间片范围为00:00-23:59,实际范围应该为6:00-23:59(time列的数值-360);输入为python文件内绝对路径;输出为python文件内绝对路径

clean_osm.py  清洗osm数据,生成link.csv,node.csv,poi.csv;输入为python文件内绝对路径;输出为python文件内绝对路径

clean_poi.py  对poi.csv进行清洗,只保留poi_id,lng,lat属性;输入为python文件内绝对路径;输出为python文件内绝对路径 ***文件内容过于繁琐可以改进

clean_poilink.py  对link文件进行清洗,筛去from_node_id,to_node_id列,剩下的列保存到新文件;输入为sys一个文件;输出为sys一个文件 ***筛选保存过程可以改进

clean_sinlink.py  对link_single.csv文件进行清洗,去除form_node_id和to_node_id,并对link_id进行重新编号;输入为sys一个文件;输出为sys一个文件

clean_tensor.cpp  对tensor进行清洗的cpp程序 待定

csv_movehead.py  去掉csv文件表头;输入为sys一个文件;输出为sys一个文件 ***可改进

csv2csv_geo.py  对link.csv提取其中的geometry属性,目前已弃用

csv2csv_link.py  对link.csv进行清洗,保留属性link_id, from_node_id, to_node_id, geometry;输入为sys一个文件;输出为sys一个文件

csv2csv_node.py  对node.csv进行清洗,保留属性node_id, x_coord, y_coord;输入为python文件内绝对路径;输出为python文件内绝对路径

csv2csv_poi.py  对poi.csv进行清洗,保留属性poi_id, osm_way_id, geometry, centroid.打印重复值数量;输入为sys一个文件;输出为sys一个文件 ***df1存在问题

csv2csv_samgps.py  对轨迹数据进行清洗,三个模块：1)对time列进行转换(输入为python文件内绝对路径;输出为python文件内绝对路径),2)根据时间间隔对轨迹数据进行采样(输入为python文件内绝对路径;输出为python文件内绝对路径),3)将多个轨迹数据文件合并一个文件(输入为python文件内绝对路径;输出为sys一个文件) ***这部分功能其他py文件好像存在重复

csv2csv_sinlink.py  对link_auto.csv进行简化,对其geometry属性中的坐标取平均值,最终只保留一个平均值;输入为sys一个文件;输出为sys一个文件 ***存在多个临时文件输出,可以进行优化

csv2csv.py  功能与clean_csv.py相同

extract_feature.py  根据link文件B提取link文件A中的指定feature并保存到新文件;输入为sys两个文件A和B;输出为sys一个文件

generate_adjmat.py  生成路网的邻接矩阵;输入为sys一个文件;输出为sys一个文件

generate_noise.py  对csv文件进行缺失操作,mode参数：1-mode1,2-mode2, 3-mode3, 5-random;输入为sys一个文件和mode;输出为sys一个文件

generate_spamat.py  生成空间相似矩阵;输入为sys一个文件;输出为sys一个文件

link_sample.py 对于link文件进行采样,随机选取执行数量的行保存到新文件;输入为sys一个文件和数量;输出为sys一个文件

mergecsv.py  对csv文件进行合并;输入为python文件内绝对路径;输出为python文件内绝对路径和文件的绝对路径 ***可以优化 csv2csv_samgps.py第三个模块功能可以移到这里

mergecsv.py  对txt文件进行合并;输入为python文件内绝对路径;输出为python文件内绝对路径

modify_idcol.py  对csv文件的id列重新标号,从0开始,再递增;输入为sys一个文件;输出为sys一个文件

modify_timecol.py  对csv文件的time列的数据进行相关处理,处理后的结果保存到源文件;输入为sys一个文件;无输出

poi_match.py  通过坐标将poi和link进行匹配 ***其中的输入和处理较为复杂

remove_req.py  统计经过mapmatch后的tensor数据(csv格式)中的重复行数量并打印,将重复行进行合并,合并后的行的value值等于重复行数量;输入为python文件内绝对路径;输出为python文件内绝对路径

search_poi.py  通过高德/百度API搜寻对应坐标的poi,但API每天可调用的次数太低,已经弃用

search_max.py  查找csv文件每一列的最大值

sort_link.py  对link文件进行某种排序  ***过程复杂,没太懂,可优化

tensor_loss.py  对csv文件进行缺失操作,mode参数：1-mode1,2-mode2, 3-mode3, 5-random;输入为sys一个文件和mode;输出为sys一个文件.同generate_noise.py

tensor_miss.py  对csv文件进行缺失操作,与tensor_loss.py不同,该程序针对列名称进行操作,更加方便简洁

tensor_recover.py  将一个tensor数据的csv文件的索引值都加1;输入为sys一个文件;输出为sys一个文件.这个程序的存在是因为TPCPD的读取tensor文件索引是从1开始的

######
数据转换

csv2mat.py  将csv文件转换为mat文件;输入为sys一个文件;输出为sys一个文件.但mat文件好像不是其他库的相同形式！

csv2npy.py  将csv文件转换为npy文件,两个模块：1)csv文件转换为npy文件,2)额外生成一个binary的npy文件(用来标记npy文件中的元素位置,值都为0或1);输入为sys一个文件;输出为sys一个文件

csv2tns.py  将csv文件转换为tns文件;输入为sys一个目录;输出为sys一个目录

npy2mat.py  将npy文件转换为mat文件;输入为sys一个目录;输出为sys一个目录.但mat文件好像不是其他库的相同形式！

tns2npy.py  将一个tensor数据(csv文件)转换为一个稠密矩阵的npy文件;输入为sys一个文件;输出为sys一个文件

txt2csv.py  将txt文件转换为csv文件并和并保存为一个新文件;输入为python文件内绝对路径;输出为python文件内绝对路径

######
Mapmatch

build_mm.sh  编译mapmatch.cpp >> sin_mapmatch

mm.sh  执行mapmatch的脚本

mapmatch_omp.cpp  路网匹配c++程序openmp版本 //已弃用,openmp部分有错误

mapmatch.cpp  路网匹配c++程序

mapmatch.cu  路网匹配c++程序cuda版本

matchmap.py  路网匹配python程序,速度太慢,已经弃用

omain  mapmatch.cpp的可执行文件

sin_mapmatch  mapmatch.cpp的可执行文件单线程版本,同omain?

sz_matchmap.cpp  mapmatch的shenzhenbei的c++版本

sz_mm_new  sz_matchmap.cpp变成出来的可执行文件

######
数据损坏

tensor_deviation.py  对数据进行按比例的损坏,以及对数值进行按比例的损坏,有两个模块：1)损坏后的数据保存到一个文件中,2)损坏后的数据保存到两个文件,损坏的部分保存一个文件,其余保存到另一个文件;输入为sys一个文件,损坏比例s(0-1),数值损坏比例(0-100的整数);输出为一个sys文件

tensor_deviation.sh 执行tensor_deviation.py的脚本,主要针对不同的deviation rate

tensor_deviation_1.sh 执行tensor_deviation.py的脚本,主要针对不同的deviation rate(mode-1)

tensor_deviation_2.sh 执行tensor_deviation.py的脚本,主要针对不同的deviation rate(mode-2)

tensor_deviation_3.sh 执行tensor_deviation.py的脚本,主要针对不同的deviation rate(mode-3)

tensor_deviation_4.sh 执行tensor_deviation.py的脚本,主要针对不同的deviation rate(random)

tensor_deviation_sz.sh 执行tensor_deviation.py的脚本,主要针对shenzhen数据集的不同的deviation rate,因为数据量小,故只有一个脚本


tensor_deviation_value.sh 执行tensor_deviation.py的脚本,主要针对不同的deviation value rate

tensor_deviation_value_1.sh 执行tensor_deviation.py的脚本,主要针对不同的deviation value rate(mode-1)

tensor_deviation_value_2.sh 执行tensor_deviation.py的脚本,主要针对不同的deviation value rate(mode-2)

tensor_deviation_value_3.sh 执行tensor_deviation.py的脚本,主要针对不同的deviation value rate(mode-3)

tensor_deviation_value_4.sh 执行tensor_deviation.py的脚本,主要针对不同的deviation value rate(random)

tensor_deviation_value_sz.sh 执行tensor_deviation.py的脚本,主要针对shenzhen数据集的不同的deviation value rate,因为数据量小,故只有一个脚本