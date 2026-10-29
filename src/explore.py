import pandas as pd

# Load the dataset from the data folder
df = pd.read_csv("data/Mall_Customers.csv")

# Display basic information and first few rows
print("Dataset Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nDataset Info:")
print(df.info())