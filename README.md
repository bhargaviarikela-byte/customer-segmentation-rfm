# Customer Segmentation using RFM Analysis and K-Means Clustering

## Project Overview

This project focuses on understanding customer purchasing behavior by using **RFM (Recency, Frequency, Monetary) Analysis** and **K-Means Clustering**.

The customers are segmented into meaningful groups based on their purchasing behavior. These segments can help businesses understand different types of customers and design targeted marketing strategies.

The project also includes an interactive **Streamlit application** for presenting the analysis and customer segments.

---

## Dataset

- Total Transactions: **34,500**
- Unique Customers: **7,903**

The dataset contains customer transaction information that was used to calculate Recency, Frequency, and Monetary values.

---

## RFM Analysis

RFM analysis was used to measure customer purchasing behavior:

- **Recency:** How recently a customer made a purchase.
- **Frequency:** How frequently a customer made purchases.
- **Monetary:** How much a customer spent.

RFM scores from **1 to 5** were assigned to customers based on their purchasing behavior.

---

## Data Preprocessing

The following preprocessing steps were performed:

1. Calculated customer-level Recency, Frequency, and Monetary values.
2. Created RFM scores.
3. Checked the distribution and skewness of RFM features.
4. Applied `log1p` transformation to reduce the effect of highly skewed values.
5. Applied `StandardScaler` to scale the RFM features.
6. Used the transformed and scaled features for K-Means clustering.

---

## K-Means Clustering

K-Means clustering was used to group customers with similar RFM behavior.

Different values of K were evaluated using:

- Elbow Method
- Silhouette Score

Based on the clustering analysis and business interpretation, **4 clusters** were selected.

### Customer Segments

| Segment | Number of Customers |
|---|---:|
| High-Value Frequent Customers | 2,365 |
| Recent Active Customers | 1,405 |
| Moderate Customers | 2,868 |
| Inactive / Low-Value Customers | 1,265 |

**Total Customers: 7,903**

---

## PCA Visualization

**Principal Component Analysis (PCA)** was used to reduce the three-dimensional RFM data into two dimensions for visualizing the customer clusters.

PCA was used for visualization, while the actual customer groups were created using K-Means clustering.

---

## Business Recommendations

### High-Value Frequent Customers

Focus on:
- Loyalty rewards
- Premium offers
- Personalized recommendations

### Recent Active Customers

Focus on:
- Repeat purchase offers
- Personalized product recommendations
- Customer engagement

### Moderate Customers

Focus on:
- Bundles
- Discounts
- Cross-selling
- Increasing purchase frequency

### Inactive / Low-Value Customers

Focus on:
- Re-engagement campaigns
- Limited-time offers
- Promotional campaigns

---

## Streamlit Application

The project includes a Streamlit application with the following sections:

- Project Overview
- RFM Analysis
- K-Means Clustering
- Customer Segments
- PCA Visualization
- Business Recommendations

The application provides an interactive way to present the customer segmentation analysis.

---

## Power BI Dashboard

A Power BI dashboard was also created to visualize:

- Total Customers
- Customer Distribution by Segment
- Average RFM Score
- Average Recency
- Average Frequency
- Average Monetary Value
- Customer Segment filtering

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- K-Means Clustering
- PCA
- Streamlit
- Power BI
- Jupyter Notebook

---

## Project Structure

```text
customer-segmentation/
│
├── app.py
├── dataset.ipynb
├── requirements.txt
├── README.md
│
├── ecommerce_sales_34500.csv
├── RFM.csv
├── RFM_score.csv
└── RFM_customer_segments.csv