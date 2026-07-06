import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_grocery_prices.csv")

print("\n========== GROCERY PRICE ANALYSIS ==========\n")

# 1. Average Price
print("Average Grocery Price")
print(round(df["Price"].mean(),2))

# 2. Cheapest Platform
print("\nAverage Price by Platform")
print(df.groupby("Platform")["Price"].mean().sort_values())

# 3. Category Wise Average Price
print("\nCategory Wise Average Price")
print(df.groupby("Category")["Price"].mean())

# 4. City Wise Average Price
print("\nCity Wise Average Price")
print(df.groupby("City")["Price"].mean())

# 5. Top 10 Highest Discounts
print("\nTop 10 Discounted Products")
print(df.sort_values(by="Discount",ascending=False)[
    ["Product_Name","Platform","Discount"]
].head(10))

# 6. Platform Product Count
print("\nProducts Available on Each Platform")
print(df["Platform"].value_counts())

# 7. Highest Price Product
highest=df.loc[df["Price"].idxmax()]
print("\nMost Expensive Product")
print(highest)

# Save summary
summary=df.groupby("Platform")["Price"].mean().reset_index()

summary.to_csv("price_summary.csv",index=False)

print("\nSummary saved successfully!")