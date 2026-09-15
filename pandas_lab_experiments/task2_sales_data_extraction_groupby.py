"""Experiment: sales-data extraction with boolean filtering, group-by
aggregation and loc/iloc indexing using Pandas."""

import pandas as pd

# Sample sales records: product, region, quantity sold and unit price
sales = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones",
                "USB Cable", "Webcam", "Speaker", "Mouse Pad", "Charger",
                "Tablet", "Printer", "Scanner", "Router", "Modem"],
    "Region": ["East", "West", "East", "West", "East",
               "North", "South", "East", "West", "North",
               "East", "South", "West", "East", "North"],
    "Quantity": [10, 25, 15, 8, 30,
                 50, 20, 12, 40, 35,
                 18, 5, 10, 22, 45],
    "Price": [500, 25, 75, 300, 100,
              10, 80, 150, 20, 25,
              200, 400, 150, 75, 60]
})

print("Initial Sales DataFrame:")
print(sales)
print()

# Derived column: revenue = quantity * unit price
sales["Revenue"] = sales["Quantity"] * sales["Price"]
print("DataFrame after adding Revenue column:")
print(sales)
print()

# Boolean filtering with AND (&) and OR (|) conditions
east_high_revenue = sales[(sales["Region"] == "East") & (sales["Revenue"] > 5000)]
print("Records where Region == 'East' AND Revenue > 5000:")
print(east_high_revenue)
print()

high_value = sales[(sales["Revenue"] > 3000) | (sales["Region"] == "North")]
print("Records where Revenue > 3000 OR Region == 'North':")
print(high_value)
print()

# Group-by aggregation per region
region_total = sales.groupby("Region")["Revenue"].sum()
region_avg = sales.groupby("Region")["Revenue"].mean()

print("Total Revenue per Region:")
print(region_total)
print()

print("Average Revenue per Region:")
print(region_avg)
print()

# Identify the top-performing region by total revenue
top_region = region_total.idxmax()
top_revenue = region_total.max()
print(f"Top-performing region: {top_region} with total revenue of {top_revenue}")
print()

# loc is label-based (end index inclusive); iloc is position-based (exclusive)
print("Using loc (label-based):")
loc_result = sales.loc[0:4, ["Product", "Region", "Revenue"]]
print(loc_result)
print()

print("Using iloc (position-based):")
iloc_result = sales.iloc[0:5, [0, 1, 4]]
print(iloc_result)
print()

print("Note: loc uses label-based indexing (end index inclusive),")
print("while iloc uses position-based indexing (end index exclusive).")
