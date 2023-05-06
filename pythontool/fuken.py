import transbigdata as tbd
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv('./data/TaxiData-Sample.csv',header = None)
data.columns = ['VehicleNum','time','lon','lat','OpenStatus','Speed']
data.head()



# 读取研究范围区域信息
sz = gpd.read_file(r'sz/sz.shp')
sz.plot()
plt.show()

# 数据预处理
#剔除研究范围外的数据，计算原理是在方法中先栅格化后栅格匹配研究范围后实现对应。因此这里需要同时定义栅格大小，越小则精度越高
data = tbd.clean_outofshape(data, sz, col=['lon', 'lat'], accuracy=500)

# 剔除出租车数据中载客状态瞬间变化的数据
data = tbd.clean_taxi_status(data, col=['VehicleNum', 'time', 'OpenStatus'])

# 定义研究范围边界
bounds = [113.75, 22.4,114.62, 22.86]

# 通过边界获取栅格化参数
params = tbd.area_to_params(bounds,accuracy = 1000)
params

 #将GPS数据对应至栅格，将生成的栅格编号列赋值到数据表上作为新的两列
data['LONCOL'],data['LATCOL']= tbd.GPS_to_grids(data['lon'],data['lat'],params)

# 聚合集计栅格内数据量
grid_agg=data.groupby(['LONCOL','LATCOL'])['VehicleNum'].count().reset_index()

# 生成栅格的几何图形
grid_agg['geometry']=tbd.grid_to_polygon([grid_agg['LONCOL'],grid_agg['LATCOL']],params)

# 转换为GeoDataFrame
grid_agg=gpd.GeoDataFrame(grid_agg)

# 绘制栅格
grid_agg.plot(column = 'VehicleNum',cmap = 'autumn_r')

fig =plt.figure(1,(8,8),dpi=300)
ax =plt.subplot(111)
plt.sca(ax)

# 添加行政区划边界作为底图
sz.plot(ax=ax,edgecolor=(0,0,0,0),facecolor=(0,0,0,0.1),linewidths=0.5)

# 定义色条位置
cax = plt.axes([0.04, 0.33, 0.02, 0.3])
plt.title('Data count')
plt.sca(ax)

# 绘制数据
grid_agg.plot(column = 'VehicleNum',cmap = 'autumn_r',ax = ax,cax = cax,legend = True)

# 添加指北针和比例尺
tbd.plotscale(ax,bounds = bounds,textsize = 10,compasssize = 1,accuracy = 2000,rect = [0.06,0.03],zorder = 10)
plt.axis('off')
plt.xlim(bounds[0],bounds[2])
plt.ylim(bounds[1],bounds[3])
plt.show()

# 从GPS数据提取OD
oddata=tbd.taxigps_to_od(data,col=['VehicleNum','time','lon','lat','OpenStatus'])
# oddata

# 重新定义栅格，获取栅格化参数
params=tbd.area_to_params(bounds,accuracy = 2000)

# 栅格化OD并集计
od_gdf=tbd.odagg_grid(oddata,params)
od_gdf.plot(column = 'count')

fig =plt.figure(1,(8,8),dpi=300)
ax =plt.subplot(111)
plt.sca(ax)

# 添加行政区划边界作为底图
sz.plot(ax=ax,edgecolor=(0,0,0,1),facecolor=(0,0,0,0),linewidths=0.5)

# 绘制colorbar
cax=plt.axes([0.05, 0.33, 0.02, 0.3])
plt.title('Data count')
plt.sca(ax)

# 绘制OD
# od_gdf.plot(ax = ax,column = 'count',cmap = 'Blues_r',linewidth = 0.5,vmax = 10,cax = cax,legend = True)

# 添加比例尺和指北针
tbd.plotscale(ax,bounds=bounds,textsize=10,compasssize=1,accuracy=2000,rect = [0.06,0.03],zorder = 10)
plt.axis('off')
plt.xlim(bounds[0],bounds[2])
plt.ylim(bounds[1],bounds[3])
plt.show()

print("finish")