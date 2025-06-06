#importing given tools
import pandas as pd

#inserting given csv
df = pd.read_csv(r"C:\Users\Lenovo\Downloads\Titanic-Dataset.csv")

#exploring basic info about the data
print("basic info()")
print(df.info)
print("\n first 5 rows")
print(df.head()) 

#checking for missing values
print("\n missing values per column:")
print(df.isnull().sum())

#


