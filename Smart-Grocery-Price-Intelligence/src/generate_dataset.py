import pandas as pd
import random
from datetime import datetime, timedelta

products = {
    "Dairy": ["Milk", "Curd", "Butter", "Paneer", "Cheese"],
    "Fruits": ["Apple", "Banana", "Orange", "Mango", "Grapes"],
    "Vegetables": ["Tomato", "Potato", "Onion", "Carrot", "Cabbage"],
    "Snacks": ["Chips", "Biscuits", "Chocolate", "Namkeen", "Cookies"],
    "Beverages": ["Tea", "Coffee", "Juice", "Soft Drink", "Energy Drink"],
    "Grains": ["Rice", "Wheat Flour", "Dal", "Sugar", "Salt"]
}

platforms = [
    "Blinkit",
    "Zepto",
    "BigBasket",
    "Amazon Fresh",
    "Swiggy Instamart"
]

cities = [
    "Hyderabad",
    "Bangalore",
    "Chennai",
    "Mumbai",
    "Delhi"
]

rows = []

start_date = datetime(2025,1,1)

product_id = 1

for i in range(500):

    category = random.choice(list(products.keys()))
    product = random.choice(products[category])

    platform = random.choice(platforms)

    city = random.choice(cities)

    mrp = random.randint(20,300)

    discount = random.randint(0,40)

    price = round(mrp*(100-discount)/100,2)

    availability = random.choice(["In Stock","Out of Stock"])

    date = start_date + timedelta(days=random.randint(0,180))

    rows.append([
        product_id,
        product,
        category,
        platform,
        city,
        date.strftime("%Y-%m-%d"),
        price,
        mrp,
        discount,
        availability
    ])

    product_id += 1

df = pd.DataFrame(rows,columns=[
    "Product_ID",
    "Product_Name",
    "Category",
    "Platform",
    "City",
    "Date",
    "Price",
    "MRP",
    "Discount",
    "Availability"
])

df.to_csv("grocery_prices.csv",index=False)

print("Dataset Generated Successfully!")