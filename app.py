import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Food Delivery Analytics",
    page_icon="🍔",
    layout="wide"
)


# ============================================================
# 2. TITLE
# ============================================================

st.title("🍔 Food Delivery Analytics Dashboard")

st.write(
    "Analyze orders, revenue, restaurants, customers, "
    "payments and delivery performance."
)


# ============================================================
# 3. LOAD DATA
# ============================================================

df = pd.read_csv(
    "food_delivery_realistic_2000_orders.csv"
)


# ============================================================
# 4. CONVERT ORDER TIMESTAMP TO DATETIME
# ============================================================

df["Order_Timestamp"] = pd.to_datetime(
    df["Order_Timestamp"]
)


# ============================================================
# 5. SIDEBAR FILTERS
# ============================================================

st.sidebar.header("🔍 Filters")


# -----------------------------
# Restaurant Filter
# -----------------------------

restaurants = df["Restaurant"].unique()

selected_restaurants = st.sidebar.multiselect(
    "Select Restaurant",
    restaurants,
    default=restaurants
)


# -----------------------------
# City Filter
# -----------------------------

cities = df["City"].unique()

selected_cities = st.sidebar.multiselect(
    "Select City",
    cities,
    default=cities
)


# -----------------------------
# Payment Method Filter
# -----------------------------

payments = df["Payment_Method"].unique()

selected_payments = st.sidebar.multiselect(
    "Select Payment Method",
    payments,
    default=payments
)


# -----------------------------
# Customer Type Filter
# -----------------------------

customer_types = df["Customer_Type"].unique()

selected_customer_types = st.sidebar.multiselect(
    "Select Customer Type",
    customer_types,
    default=customer_types
)


# ============================================================
# 6. FILTER DATA
# ============================================================

filtered_df = df[
    (df["Restaurant"].isin(selected_restaurants)) &
    (df["City"].isin(selected_cities)) &
    (df["Payment_Method"].isin(selected_payments)) &
    (df["Customer_Type"].isin(selected_customer_types))
]


# ============================================================
# 7. KPI CALCULATIONS
# ============================================================

total_orders = len(filtered_df)

total_revenue = filtered_df["Final_Amount"].sum()

average_order_value = filtered_df["Final_Amount"].mean()

average_rating = filtered_df["Rating"].mean()

average_delivery_time = filtered_df["Actual_Delivery_Min"].mean()


# ============================================================
# 8. DISPLAY KPIs
# ============================================================

st.subheader("📊 Key Performance Indicators")


col1, col2, col3, col4, col5 = st.columns(5)


col1.metric(
    "Total Orders",
    f"{total_orders:,}"
)


col2.metric(
    "Total Revenue",
    f"₹{total_revenue:,.0f}"
)


col3.metric(
    "Average Order Value",
    f"₹{average_order_value:,.0f}"
)


col4.metric(
    "Average Rating",
    f"{average_rating:.2f}"
)


col5.metric(
    "Avg Delivery Time",
    f"{average_delivery_time:.1f} min"
)


# ============================================================
# 9. REVENUE BY RESTAURANT
# ============================================================

st.subheader("💰 Revenue by Restaurant")


restaurant_revenue = (
    filtered_df
    .groupby("Restaurant")["Final_Amount"]
    .sum()
    .sort_values(ascending=False)
)


fig, ax = plt.subplots(figsize=(10, 5))


sns.barplot(
    x=restaurant_revenue.index,
    y=restaurant_revenue.values,
    ax=ax
)


ax.set_title("Revenue by Restaurant")
ax.set_xlabel("Restaurant")
ax.set_ylabel("Revenue")


plt.xticks(rotation=45)

st.pyplot(fig)


# ============================================================
# 10. ORDERS BY RESTAURANT
# ============================================================

st.subheader("📦 Orders by Restaurant")


restaurant_orders = (
    filtered_df
    .groupby("Restaurant")["Order_ID"]
    .count()
    .sort_values(ascending=False)
)


fig, ax = plt.subplots(figsize=(10, 5))


sns.barplot(
    x=restaurant_orders.index,
    y=restaurant_orders.values,
    ax=ax
)


ax.set_title("Number of Orders by Restaurant")
ax.set_xlabel("Restaurant")
ax.set_ylabel("Number of Orders")


plt.xticks(rotation=45)

st.pyplot(fig)


# ============================================================
# 11. REVENUE BY CITY
# ============================================================

st.subheader("🏙️ Revenue by City")


city_revenue = (
    filtered_df
    .groupby("City")["Final_Amount"]
    .sum()
    .sort_values(ascending=False)
)


fig, ax = plt.subplots(figsize=(10, 5))


sns.barplot(
    x=city_revenue.index,
    y=city_revenue.values,
    ax=ax
)


ax.set_title("Revenue by City")
ax.set_xlabel("City")
ax.set_ylabel("Revenue")


plt.xticks(rotation=45)

st.pyplot(fig)


# ============================================================
# 12. ORDERS BY CITY
# ============================================================

st.subheader("📍 Orders by City")


city_orders = (
    filtered_df["City"]
    .value_counts()
)


fig, ax = plt.subplots(figsize=(10, 5))


sns.barplot(
    x=city_orders.index,
    y=city_orders.values,
    ax=ax
)


ax.set_title("Orders by City")
ax.set_xlabel("City")
ax.set_ylabel("Number of Orders")


plt.xticks(rotation=45)

st.pyplot(fig)


# ============================================================
# 13. PAYMENT METHOD ANALYSIS
# ============================================================

st.subheader("💳 Payment Method Analysis")


payment_counts = (
    filtered_df["Payment_Method"]
    .value_counts()
)


fig, ax = plt.subplots(figsize=(8, 5))


sns.barplot(
    x=payment_counts.index,
    y=payment_counts.values,
    ax=ax
)


ax.set_title("Orders by Payment Method")
ax.set_xlabel("Payment Method")
ax.set_ylabel("Number of Orders")


plt.xticks(rotation=30)

st.pyplot(fig)


# ============================================================
# 14. ORDER STATUS
# ============================================================

st.subheader("📋 Order Status")


status_counts = (
    filtered_df["Order_Status"]
    .value_counts()
)


fig, ax = plt.subplots(figsize=(8, 5))


sns.barplot(
    x=status_counts.index,
    y=status_counts.values,
    ax=ax
)


ax.set_title("Order Status Distribution")
ax.set_xlabel("Order Status")
ax.set_ylabel("Number of Orders")


plt.xticks(rotation=30)

st.pyplot(fig)


# ============================================================
# 15. CUSTOMER TYPE
# ============================================================

st.subheader("👥 Customer Type")


customer_type_counts = (
    filtered_df["Customer_Type"]
    .value_counts()
)


fig, ax = plt.subplots(figsize=(8, 5))


sns.barplot(
    x=customer_type_counts.index,
    y=customer_type_counts.values,
    ax=ax
)


ax.set_title("Orders by Customer Type")
ax.set_xlabel("Customer Type")
ax.set_ylabel("Number of Orders")


st.pyplot(fig)


# ============================================================
# 16. DELIVERY TIME DISTRIBUTION
# ============================================================

st.subheader("🚚 Delivery Time Distribution")


fig, ax = plt.subplots(figsize=(10, 5))


sns.histplot(
    data=filtered_df,
    x="Actual_Delivery_Min",
    bins=10,
    kde=True,
    ax=ax
)


ax.set_title("Actual Delivery Time Distribution")
ax.set_xlabel("Delivery Time (Minutes)")
ax.set_ylabel("Number of Orders")


st.pyplot(fig)


# ============================================================
# 17. DELIVERY TIME VS RATING
# ============================================================

st.subheader("⭐ Delivery Time vs Customer Rating")


fig, ax = plt.subplots(figsize=(10, 5))


sns.scatterplot(
    data=filtered_df,
    x="Actual_Delivery_Min",
    y="Rating",
    hue="Restaurant",
    ax=ax
)


ax.set_title("Delivery Time vs Customer Rating")
ax.set_xlabel("Actual Delivery Time (Minutes)")
ax.set_ylabel("Customer Rating")


st.pyplot(fig)


# ============================================================
# 18. REVENUE OVER TIME
# ============================================================

st.subheader("📈 Revenue Over Time")


daily_revenue = (
    filtered_df
    .groupby(
        filtered_df["Order_Timestamp"].dt.date
    )["Final_Amount"]
    .sum()
)


fig, ax = plt.subplots(figsize=(12, 5))


ax.plot(
    daily_revenue.index,
    daily_revenue.values
)


ax.set_title("Daily Revenue")
ax.set_xlabel("Date")
ax.set_ylabel("Revenue")


plt.xticks(rotation=45)

st.pyplot(fig)


# ============================================================
# 19. ORDERS BY MEAL PERIOD
# ============================================================

st.subheader("🍽️ Orders by Meal Period")


meal_counts = (
    filtered_df["Meal_Period"]
    .value_counts()
)


fig, ax = plt.subplots(figsize=(8, 5))


sns.barplot(
    x=meal_counts.index,
    y=meal_counts.values,
    ax=ax
)


ax.set_title("Orders by Meal Period")
ax.set_xlabel("Meal Period")
ax.set_ylabel("Number of Orders")


plt.xticks(rotation=30)

st.pyplot(fig)


# ============================================================
# 20. TOP RESTAURANTS TABLE
# ============================================================

st.subheader("🏆 Restaurant Performance")


restaurant_summary = (
    filtered_df
    .groupby("Restaurant")
    .agg(
        Total_Orders=("Order_ID", "count"),
        Total_Revenue=("Final_Amount", "sum"),
        Average_Order_Value=("Final_Amount", "mean"),
        Average_Rating=("Rating", "mean"),
        Average_Delivery_Time=("Actual_Delivery_Min", "mean")
    )
    .sort_values(
        "Total_Revenue",
        ascending=False
    )
)


st.dataframe(
    restaurant_summary,
    use_container_width=True
)


# ============================================================
# 21. RAW DATA
# ============================================================

st.subheader("📋 Order Data")


st.dataframe(
    filtered_df,
    use_container_width=True
)