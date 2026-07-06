# Smart Grocery Price Intelligence Dashboard

##  Project Overview

The Smart Grocery Price Intelligence Dashboard is a data analytics project that analyzes grocery product prices, discounts, availability, and platform-wise trends across multiple online grocery platforms.

The project combines Python for data generation and preprocessing, SQL for querying, and Power BI for interactive dashboard visualization.

---

##  Dashboard Preview

> Add a screenshot of the dashboard below.

![Dashboard](dashboard/dashboard.png)

---

##  Objectives

- Analyze grocery prices across multiple platforms.
- Compare average prices by category.
- Identify platform-wise pricing trends.
- Analyze discounts offered by different platforms.
- Track price trends over time.
- Build an interactive Power BI dashboard.

---

## Technologies Used

- Python
- Pandas
- SQLite
- SQL
- Power BI
- CSV

---

##  Project Structure

```
Smart-Grocery-Price-Intelligence/
│
├── dashboard/
│   ├── Grocery_Price_Intelligence_Dashboard.pbix
│   └── dashboard.png
│
├── data/
│   ├── grocery_prices.csv
│   └── cleaned_grocery_prices.csv
│
├── sql/
│   └── sql_queries.py
│
├── src/
│   ├── generate_dataset.py
│   ├── clean_data.py
│   ├── analysis.py
│   └── database.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

##  Dashboard Features

- Total Products
- Average Price
- Average Discount
- Total Platforms
- Average Price by Platform
- Products by Category
- Products by Platform
- Average Price Trend
- Average Price by Category
- City-wise Filtering

---

##  Dataset

The dataset contains:

- Product ID
- Product Name
- Category
- Platform
- City
- Date
- Price
- MRP
- Discount
- Availability

Total Records: **500**

---

##  How to Run

1. Clone the repository.
2. Install the required libraries.
3. Run the Python scripts inside the `src` folder.
4. Open the Power BI dashboard.
5. Explore the interactive visualizations.

---
