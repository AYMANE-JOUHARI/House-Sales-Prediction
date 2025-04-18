import pandas as pd

house_sales = pd.read_csv('data/house_sales.csv')
missing_city = house_sales[house_sales['city'] == "--"]['city'].count()
print("Missing city count:", missing_city)