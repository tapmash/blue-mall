import os
import pandas as pd

# Get the project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "data", "Customers_Clustered.csv")

# Load the clustered dataset
df = pd.read_csv(file_path)

# Group by the cluster and calculate average values
summary = df.groupby('Cluster')[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']].mean()
summary['Count'] = df['Cluster'].value_counts()

print("Cluster Summary (Averages per Group):")
print("=====================================")
print(summary.round(2))
