from pathlib import Path
import sqlite3
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent

db_path = BASE_DIR / "grocery.db"

df = pd.read_csv("cleaned_grocery_prices.csv")

conn = sqlite3.connect(db_path)

df.to_sql(
    "grocery_prices",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database created successfully!")