import sqlite3
import pandas as pd
from pathlib import Path

# Get database path
BASE_DIR = Path(__file__).resolve().parent.parent
db_path = BASE_DIR / "grocery.db"

# Connect to database
conn = sqlite3.connect(db_path)

# ---------------- Query 1 ----------------
print("\n========== Average Price ==========")

query = """
SELECT ROUND(AVG(Price), 2) AS Average_Price
FROM grocery_prices;
"""

print(pd.read_sql_query(query, conn))

# ---------------- Query 2 ----------------
print("\n========== Cheapest Platform ==========")

query = """
SELECT Platform,
       ROUND(AVG(Price), 2) AS AvgPrice
FROM grocery_prices
GROUP BY Platform
ORDER BY AvgPrice ASC;
"""

print(pd.read_sql_query(query, conn))

# ---------------- Query 3 ----------------
print("\n========== Category Wise Price ==========")

query = """
SELECT Category,
       ROUND(AVG(Price), 2) AS AvgPrice
FROM grocery_prices
GROUP BY Category
ORDER BY AvgPrice DESC;
"""

print(pd.read_sql_query(query, conn))

# ---------------- Query 4 ----------------
print("\n========== Top 10 Discounts ==========")

query = """
SELECT Product_Name,
       Platform,
       Discount
FROM grocery_prices
ORDER BY Discount DESC
LIMIT 10;
"""

print(pd.read_sql_query(query, conn))

# ---------------- Query 5 ----------------
print("\n========== Products Per Platform ==========")

query = """
SELECT Platform,
       COUNT(*) AS TotalProducts
FROM grocery_prices
GROUP BY Platform
ORDER BY TotalProducts DESC;
"""

print(pd.read_sql_query(query, conn))

# Close connection
conn.close()

print("\nSQL Analysis Completed Successfully!")