import pandas_datareader.data as web
import pandas as pd
import datetime
import os

# Create 'data' folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Get the current date and calculate the date range for the last 5 years
end_date = datetime.datetime.now()
start_date = datetime.datetime(end_date.year - 5, end_date.month, end_date.day)

# Fetch the US CPI data (CPIAUCNS is the identifier for US CPI)
cpi_data = web.DataReader('CPIAUCNS', 'fred', start_date, end_date)

# Save the fetched CPI data to a CSV file in the 'data' folder
cpi_data.to_csv('data/cpi_data.csv')

# 1. Resample the data by quarter and get the last day of each quarter
cpi_quarterly = cpi_data.resample('QE').last()

# 2. Calculate the quarterly inflation rate: percentage change from the previous quarter
cpi_quarterly['Quarterly Inflation Rate'] = cpi_quarterly['CPIAUCNS'].pct_change(periods=1) * 100

# Get the inflation rates for the last 4 quarters
inflation_last_4_quarters = cpi_quarterly['Quarterly Inflation Rate'].tail(4)

# Print the inflation rates for the last 4 quarters
print("Inflation Rates for the Last 4 Quarters:")
print(inflation_last_4_quarters)

# Save the inflation rates for the last 4 quarters to a CSV file in the 'data' folder
inflation_last_4_quarters.to_csv('data/inflation_last_4_quarters.csv', header=True)