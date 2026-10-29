# Mall Customer Segmentation

A modular Python machine learning project that segments mall customers into distinct behavioral groups using K-Means clustering based on their annual income and spending scores.

---

## 📌 Project Charter:

**Blue-Mall Customer Segmentation and Leasing Optimisation**

**1. Project Metadata**
- **Project Title:** Tenant Portfolio Planning and Behavioural Segmentation Analysis
- **Sponsor:** Blue-Mall executive management (on behalf of all stakeholders)
- **Execution:** TMK Data Analytics Consulting
- **Methodology:** Unsupervised machine learning (K-Means clustering) utilising historical customer demographics and behavioural metrics
- **Project Duration:** 6 weeks

**2. Project Objectives**

Despite reliable visitor numbers, Blue-Mall underperforms in commercial yield, revenue per square metre, and in building lasting relationships with high-value tenants. We intend to build an empirical customer segmentation framework that aligns physical leasing strategies and marketing campaigns with the actual purchasing power and spending behaviour of mall visitors.

**Core Objectives**
1. Segment the visitor population into distinct clusters using Annual Income and Spending Scores via K-Means cluster analysis.
2. Provide asset managers with actionable guidance on which retail, dining, and service categories to recruit or relocate to capture high-value customer clusters.
3. Transition general promotional campaigns toward targeted micro-segmentation strategies designed to activate high-income, low-spending visitors and safeguard loyal mid-tier spenders.

**3. Deliverables**
- Normalisation and validation of customer demographic records
- Determination of the optimal number of clusters using K-Means analysis
- A summarised breakdown of demographic means, income thresholds, and behavioural indexes for each identified segment
- An executive briefing mapping each cluster to specific leasing, zoning, and marketing interventions

## Business Problem
Understanding customer behavior is critical for retail businesses to optimize marketing strategies and target specific customer demographics. The goal of this project is to segment mall customers into distinct groups based on their purchasing habits and income levels, allowing management to tailor loyalty programs and marketing campaigns effectively.

## 📊 Dataset Description
The dataset (`Mall_Customers.csv`) contains customer demographic and financial attributes:
- **CustomerID**: Unique ID assigned to the customer.
- **Gender**: Gender of the customer.
- **Age**: Age of the customer.
- **Annual Income (k$)**: Annual income of the customer in thousands of dollars.
- **Spending Score (1-100)**: Score assigned by the mall based on customer behavior and purchasing nature.

---

## 📁 Project Structure
- `data/`: Contains raw and processed datasets (`Mall_Customers.csv`, `Mall_Customers_Clustered.csv`).
- `src/`: Core modular Python scripts:
  - `explore.py`: Loads, inspects, and verifies the dataset.
  - `segmentation.py`: Applies optimal K-Means clustering and generates visualization plots.
  - `cluster_summary.py`: Computes statistical profiles for each customer segment.
- `images/`: Saved visualizations (`customer_segments.png`).

---

## 📈 Customer Segmentation Visualization
The K-Means model successfully groups customers into 5 distinct behavioral segments based on Annual Income vs. Spending Score:

![Customer Segments](images/customer_segments.png)

### Cluster Insights:
1. **Cluster 0 (Moderate Income, Moderate Spending):** Average earners who maintain steady, moderate purchasing behavior.
2. **Cluster 1 (High Income, Low Spending):** Wealthy customers who are cautious and conservative with their spending.
3. **Cluster 2 (High Income, High Spending):** Premium customers/Target demographic representing high earners with high spending scores.
4. **Cluster 3 (Low Income, Low Spending):** Budget-conscious customers with lower income and spending scores.
5. **Cluster 4 (Low Income, High Spending):** Shoppers who spend heavily despite having lower annual incomes.

---

## ⚙️ How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/tapmash/blue-mall.git](https://github.com/tapmash/blue-mall.git)
   cd blue-mall
