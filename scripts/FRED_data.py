import pandas_datareader.data as web
import pandas as pd
import datetime
import os

# 创建 data 文件夹，如果不存在
if not os.path.exists('data'):
    os.makedirs('data')

# 获取当前日期，并计算过去五年的数据时间段
end_date = datetime.datetime.now()
start_date = datetime.datetime(end_date.year - 5, end_date.month, end_date.day)

# 从 FRED 获取 CPI 数据（CPIAUCNS是美国CPI的标识符）
cpi_data = web.DataReader('CPIAUCNS', 'fred', start_date, end_date)

# 将 CPI 数据保存到 data 文件夹
cpi_data.to_csv('data/cpi_data.csv')

# 1. 按季度重采样，计算每季度的最后一天的数据
cpi_quarterly = cpi_data.resample('QE').last()

# 2. 计算季度通货膨胀率：季度变化百分比
cpi_quarterly['Quarterly Inflation Rate'] = cpi_quarterly['CPIAUCNS'].pct_change(periods=1) * 100

# 获取最近四个季度的通货膨胀率
inflation_last_4_quarters = cpi_quarterly['Quarterly Inflation Rate'].tail(4)

# 打印最近四个季度的通货膨胀率
print("Inflation Rates for the Last 4 Quarters:")
print(inflation_last_4_quarters)

# 将计算结果保存到 data 文件夹中的 CSV 文件
inflation_last_4_quarters.to_csv('data/inflation_last_4_quarters.csv', header=True)
