# Mall Customer Segmentation

A minimalist local machine learning project that segments mall customers into distinct behavioral groups using K-Means clustering based on annual income and spending score.

## Project Structure
- `data/`: Contains the raw dataset (`Mall_Customers.csv`) and the clustered output (`Mall_Customers_Clustered.csv`).
- `src/`: Core Python scripts:
  - `explore.py`: Loads and verifies the dataset.
  - `segmentation.py`: Applies K-Means clustering and generates the visual plot.
  - `cluster_summary.py`: Generates analytical profile averages for each customer segment.
- `images/`: Saved visualizations (`customer_segments.png`).

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt