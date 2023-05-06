from fastparquet import ParquetFile
datadir = r'./data/'
filename = datadir + r'fhvhv_tripdata_2021-01.parquet'
pf = ParquetFile(filename)
dF = pf.to_pandas()
outfile = datadir + r'fhvhv_tripdata_2021-01.parquet'
dF.to_csv(outfile,encoding='gbk')