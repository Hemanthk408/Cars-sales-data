#To Opening the file pandas package is import
import pandas as pd
df=pd.read_csv("https://github.com/Hemanthk408/Cars-sales-data/blob/main/Car_sales.csv")
#print(df) or only type df for showing the table
df

# Check the first few rows for columns title
print(df.head())

# Summary of the dataset
print(df.info())

# Check for missing values if any 0 or NAN value are in the data this code will show the count of that
print(df.isnull().sum())

# Fill missing values with a default value
df['ColumnName'] = df['ColumnName'].fillna('DefaultValue')

# Drop rows with missing values
df = df.dropna()

# Data is have any duplicates this code will drop the duplicate in this code keep=first is keep the first duplicte with out droping
df = df.drop_duplicates(keep="first")

#after drop the null values checking the table
df.info()
