import pandas as pd
import numpy as np

house_sales = pd.read_csv("data/house_sales.csv")
house_sales['city'] = house_sales['city'].replace('--', 'Unknown')
house_sales = house_sales[~house_sales['sale_price'].isna()]
house_sales['sale_date'] = house_sales['sale_date'].fillna('2023-01-01')
mean_months = round(house_sales['months_listed'].mean(), 1)
house_sales['months_listed'] = house_sales['months_listed'].fillna(mean_months)
mean_beds = round(house_sales['bedrooms'].mean())
house_sales['bedrooms'] = house_sales['bedrooms'].fillna(mean_beds)
most_common = house_sales['house_type'].mode()[0]
house_sales['house_type'] = house_sales['house_type'].fillna(most_common)
house_sales['house_type'] = house_sales['house_type'].replace({'Det.': 'Detached', 'Semi': 'Semi-detached', 'Terr.': 'Terraced'})
house_sales['area'] = house_sales['area'].astype(str).str.replace('sq.m.', '').astype(float)
mean_area = round(house_sales['area'].mean(), 1)
house_sales['area'] = house_sales['area'].fillna(mean_area)
house_sales['sale_date'] = pd.to_datetime(house_sales['sale_date'])
clean_data = house_sales.reset_index(drop=True)
clean_data.to_csv("clean_data.csv", index=False)
print("Cleaned data saved.")