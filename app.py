import streamlit as st
import matplotlib.pyplot as plt


# --------------------------------------------------
# PAGE TITLE
# --------------------------------------------------

st.title("RFM Customer Segmentation")

st.write("Customer analysis using RFM and K-Means Clustering")


# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------

st.sidebar.title("Navigation")

option = st.sidebar.selectbox(
    "Choose a section",
    [
        "Overview",
        "RFM Analysis",
        "K-Means Clustering",
        "Customer Segments",
        "PCA Visualization",
        "Business Recommendations"
    ]
)

st.write("You selected:", option)


# --------------------------------------------------
# OVERVIEW
# --------------------------------------------------

if option == "Overview":

    st.header("Project Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Customers", "7,903")
    col2.metric("Total Transactions", "34,500")
    col3.metric("Number of Segments", "4")

    st.subheader("Project Objective")

    st.write(
        "The objective of this project is to understand customer "
        "purchasing behavior using RFM analysis and K-Means clustering "
        "and divide customers into meaningful segments."
    )

    st.subheader("Project Workflow")

    st.write(
        "Data → RFM Analysis → RFM Scoring → Log Transformation → "
        "Standard Scaling → K-Means Clustering → PCA Visualization → "
        "Customer Segmentation"
    )


# --------------------------------------------------
# RFM ANALYSIS
# --------------------------------------------------

if option == "RFM Analysis":

    st.header("RFM Analysis")

    st.write(
        "RFM analysis helps us understand customer purchasing behavior "
        "using Recency, Frequency and Monetary values."
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("R", "Recency")
    col2.metric("F", "Frequency")
    col3.metric("M", "Monetary")

    st.write(
        "**R – Recency:** How recently did the customer purchase?"
    )

    st.write(
        "**F – Frequency:** How frequently does the customer purchase?"
    )

    st.write(
        "**M – Monetary:** How much money does the customer spend?"
    )

    st.subheader("RFM Scoring")

    st.write(
        "Customers were assigned RFM scores from 1 to 5 based on "
        "their purchasing behavior."
    )

    st.write(
        "A higher RFM score generally represents more valuable "
        "and active customer behavior."
    )

    st.subheader("Data Transformation")

    st.write(
        "Log transformation was applied to reduce skewness in the "
        "RFM features, especially Monetary values."
    )

    st.write(
        "StandardScaler was then used to bring the RFM features "
        "to a comparable scale before applying K-Means clustering."
    )


# --------------------------------------------------
# K-MEANS CLUSTERING
# --------------------------------------------------

if option == "K-Means Clustering":

    st.header("K-Means Clustering")

    st.write(
        "K-Means clustering groups customers based on similar "
        "RFM behavior."
    )

    st.subheader("Choosing the Number of Clusters")

    st.write(
        "Different values of K from 2 to 10 were evaluated using "
        "the Elbow Method and Silhouette Score."
    )

    st.write(
        "Based on the clustering analysis and business interpretation, "
        "4 clusters were selected for customer segmentation."
    )

    st.subheader("Clusters")

    st.write("**Cluster 0:** Recent Active Customers")

    st.write("**Cluster 1:** Inactive / Low-Value Customers")

    st.write("**Cluster 2:** High-Value Frequent Customers")

    st.write("**Cluster 3:** Moderate Customers")


# --------------------------------------------------
# CUSTOMER SEGMENTS
# --------------------------------------------------

if option == "Customer Segments":

    st.header("Customer Segments")

    st.write(
        "Customers are divided into four segments based on "
        "their RFM behavior."
    )

    # Segment information

    segment_names = [
        "High-Value Frequent Customers",
        "Recent Active Customers",
        "Moderate Customers",
        "Inactive / Low-Value Customers"
    ]

    segment_counts = [
        2365,
        1405,
        2868,
        1265
    ]

    # --------------------------------------------------
    # Customer Distribution
    # --------------------------------------------------

    st.subheader("1. Customer Distribution by Segment")

    fig, ax = plt.subplots()

    ax.bar(
        segment_names,
        segment_counts,
        width=0.5
    )

    ax.set_title("Customer Distribution by Segment")
    ax.set_xlabel("Segment")
    ax.set_ylabel("Number of Customers")

    ax.tick_params(
        axis="x",
        labelrotation=20
    )

    st.pyplot(fig)


    # --------------------------------------------------
    # Average Recency
    # --------------------------------------------------

    st.subheader("2. Average Recency by Segment")

    recency_values = [
        55,
        25,
        95,
        180
    ]

    fig, ax = plt.subplots()

    ax.bar(
        segment_names,
        recency_values,
        width=0.5
    )

    ax.set_title("Average Recency by Segment")
    ax.set_xlabel("Segment")
    ax.set_ylabel("Average Recency")

    ax.tick_params(
        axis="x",
        labelrotation=20
    )

    st.pyplot(fig)


    # --------------------------------------------------
    # Average Frequency
    # --------------------------------------------------

    st.subheader("3. Average Frequency by Segment")

    frequency_values = [
        7,
        6,
        4,
        2
    ]

    fig, ax = plt.subplots()

    ax.bar(
        segment_names,
        frequency_values,
        width=0.5
    )

    ax.set_title("Average Frequency by Segment")
    ax.set_xlabel("Segment")
    ax.set_ylabel("Average Frequency")

    ax.tick_params(
        axis="x",
        labelrotation=20
    )

    st.pyplot(fig)


    # --------------------------------------------------
    # Average Monetary
    # --------------------------------------------------

    st.subheader("4. Average Monetary Value by Segment")

    monetary_values = [
        1200,
        850,
        650,
        300
    ]

    fig, ax = plt.subplots()

    ax.bar(
        segment_names,
        monetary_values,
        width=0.5
    )

    ax.set_title("Average Monetary Value by Segment")
    ax.set_xlabel("Segment")
    ax.set_ylabel("Average Monetary Value")

    ax.tick_params(
        axis="x",
        labelrotation=20
    )

    st.pyplot(fig)


# --------------------------------------------------
# PCA VISUALIZATION
# --------------------------------------------------

if option == "PCA Visualization":

    st.header("PCA Visualization")

    st.write(
        "PCA (Principal Component Analysis) is used to reduce "
        "the dimensionality of the RFM data from three dimensions "
        "to two dimensions so that the customer clusters can be "
        "visualized in a 2D plot."
    )

    st.subheader("Customer Clusters in 2D")

    # Example PCA coordinates
    pca_x = [
        -2.1, -1.8, -1.5, -1.2, -0.9,
        0.2, 0.5, 0.8, 1.1, 1.4,
        1.7, 2.0, 2.3, 2.6
    ]

    pca_y = [
        1.5, 1.2, 1.8, 1.0, 1.4,
        -0.5, -0.2, -0.8, -0.4, -0.7,
        1.0, 0.6, 0.9, 0.4
    ]

    cluster_labels = [
        0, 0, 0, 0, 0,
        1, 1, 1, 1, 1,
        2, 2, 2, 2
    ]

    fig, ax = plt.subplots()

    scatter = ax.scatter(
        pca_x,
        pca_y,
        c=cluster_labels
    )

    ax.set_title("PCA Visualization of Customer Clusters")
    ax.set_xlabel("Principal Component 1")
    ax.set_ylabel("Principal Component 2")

    st.pyplot(fig)

    st.write(
        "PCA is used only for visualization. The customer clusters "
        "were created using K-Means clustering."
    )


# --------------------------------------------------
# BUSINESS RECOMMENDATIONS
# --------------------------------------------------

if option == "Business Recommendations":

    st.header("Business Recommendations")

    st.write(
        "Business recommendations are actions a company can take "
        "based on the customer segments identified through RFM "
        "analysis and K-Means clustering."
    )

    st.subheader("High-Value Frequent Customers")

    st.write(
        "These customers purchase frequently and have high spending. "
        "Recommendation: Focus on loyalty rewards, premium offers "
        "and personalized recommendations."
    )

    st.subheader("Recent Active Customers")

    st.write(
        "These customers have purchased recently and are currently "
        "active. Recommendation: Encourage repeat purchases through "
        "personalized offers and product recommendations."
    )

    st.subheader("Moderate Customers")

    st.write(
        "These customers show moderate purchasing behavior. "
        "Recommendation: Increase their purchase frequency and "
        "spending through bundles, discounts and cross-selling."
    )

    st.subheader("Inactive / Low-Value Customers")

    st.write(
        "These customers have relatively high Recency and lower "
        "purchasing activity/value. Recommendation: Use re-engagement "
        "campaigns and limited-time offers to bring them back."
    )