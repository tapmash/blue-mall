import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Get the project root directory (one level up from 'src')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define safe absolute paths
data_path = os.path.join(BASE_DIR, "data", "Customers.csv")
output_csv_path = os.path.join(BASE_DIR, "data", "Customers_Clustered.csv")
output_img_path = os.path.join(BASE_DIR, "images", "customer_segments.png")

# 1. Load the dataset
df = pd.read_csv(data_path)

# 2. Select features for segmentation (Annual Income and Spending Score)
X = df[["Annual Income (k$)", "Spending Score (1-100)"]]

# 3. Apply K-Means Clustering with 5 clusters (standard for this dataset)
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# 4. Save the clustered data
df.to_csv(output_csv_path, index=False)
print("Clustered data saved to data/Customers_Clustered.csv")

# 5. Plot and save the customer segments visualization
plt.figure(figsize=(8, 6))
sns.scatterplot(
    x='Annual Income (k$)', 
    y='Spending Score (1-100)', 
    hue='Cluster', 
    data=df, 
    palette='Set1', 
    s=100, 
    alpha=0.8
)
plt.title('Customer Segments (K-Means)')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend(title='Cluster')
plt.grid(True, linestyle='--', alpha=0.5)

# Save plot to the images folder
plt.savefig(output_img_path, bbox_inches='tight')
plt.close()
print("Cluster plot saved to images/customer_segments.png")