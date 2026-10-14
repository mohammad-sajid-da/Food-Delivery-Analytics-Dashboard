# Food Delivery Analytics Dashboard

An interactive Streamlit dashboard that analyzes 2,000+ food delivery orders (2025) to track revenue, orders, customer ratings and delivery performance.

## Features
- **Sidebar filters:** restaurant, city, payment method and customer type
- **KPIs:** total orders, total revenue, average order value, average rating, average delivery time
- **Charts:** revenue by restaurant and city, payment method mix, customer type split, delivery time vs rating, and revenue trends over time

## Key Insight
Longer delivery times are linked to lower customer ratings (correlation of about -0.56), so delivery speed is a major driver of customer satisfaction.

## Dataset
`food_delivery_realistic_2000_orders.csv` has 2,000+ orders and 25 columns, including restaurant, city, cuisine, order value, discount, payment method, delivery time, distance, customer type and rating. It covers 12 restaurants and 8 cities.

## Tech Stack
Python, Pandas, Streamlit, Matplotlib, Seaborn

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

![Dashboard](screenshots/dashboard.png)

## Author
Mohammad Sajid | [LinkedIn](https://www.linkedin.com/in/mohammad-sajid-da)
