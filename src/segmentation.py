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
X = df[["Annual Income (R)", "Spending Score (1-100)"]]

# 3. Apply K-Means Clustering with 5 clusters (standard for this dataset)
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# 4. Save the clustered data
df.to_csv(output_csv_path, index=False)
print("Clustered data saved to data/Customers_Clustered.csv")

# 5. Plot and save the customer segments visualization with distinct markers and a fancy bluish background
fig, ax = plt.subplots(figsize=(8, 6))

# Set a fancy dark bluish background for the plot axes
ax.set_facecolor('#0f172a')  # Deep modern slate-blue
fig.patch.set_facecolor('#1e293b')  # Slightly lighter blue-gray for the outer figure

# Scatter plot with different markers and colors per cluster
sns.scatterplot(
    x='Annual Income (R)',
    y='Spending Score (1-100)',
    hue='Cluster',
    style='Cluster',  # Assigns a unique marker shape to each cluster
    markers=['o', 's', '^', 'D', 'X'],  # Circle, Square, Triangle, Diamond, X
    data=df,
    palette='Set1',
    s=110,
    alpha=0.9,
    ax=ax,
)

# Styling labels, title, and legend for high visibility on a dark background
plt.title(
    'Customer Segments (K-Means)',
    color='white',
    fontsize=14,
    fontweight='bold',
    pad=12,
)
plt.xlabel('Annual Income (R)', color='white', fontsize=11)
plt.ylabel('Spending Score (1-100)', color='white', fontsize=11)

# Customize ticks and grid lines for readability
ax.tick_params(colors='white', labelsize=10)
plt.grid(True, linestyle='--', alpha=0.3, color='#94a3b8')

# Format spines (borders)
for spine in ax.spines.values():
  spine.set_edgecolor('#334155')

# Style the legend to look clean against the dark background
legend = plt.legend(
    title='Cluster', facecolor='#1e293b', edgecolor='#334155', labelcolor='white'
)
legend.get_title().set_color('white')

# Save plot to the images folder with matching background color
plt.savefig(
    output_img_path,
    bbox_inches='tight',
    facecolor=fig.get_facecolor(),
    edgecolor='none',
)
plt.close()
print('Cluster plot saved to images/customer_segments.png')