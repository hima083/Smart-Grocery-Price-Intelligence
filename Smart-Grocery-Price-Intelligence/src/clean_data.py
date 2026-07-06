import pandas as pd

# Load the dataset
df = pd.read_csv("grocery_prices.csv")

print("========== ORIGINAL DATA ==========")
print(df.head())

print("\nShape of Dataset:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Convert Date column into datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Convert data types
df["Price"] = df["Price"].astype(float)
df["MRP"] = df["MRP"].astype(float)
df["Discount"] = df["Discount"].astype(int)

print("\n========== CLEANED DATA ==========")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# Save cleaned dataset
df.to_csv("cleaned_grocery_prices.csv", index=False)

print("\n Cleaned dataset saved successfully!")