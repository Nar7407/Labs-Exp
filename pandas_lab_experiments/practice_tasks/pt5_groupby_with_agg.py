"""Practice Task 5: Groupby with multiple aggregations using .agg()"""

import pandas as pd

print("=" * 70)
print("PRACTICE TASK 5: GROUPBY WITH MULTIPLE AGGREGATIONS (.agg())")
print("=" * 70)

sales = pd.DataFrame({
    "Region": ["North", "South", "East", "West", "North",
               "South", "East", "West", "North", "South",
               "East", "West", "North", "South", "East"],
    "Product": ["A", "B", "A", "C", "B",
                "A", "C", "B", "A", "C",
                "B", "A", "C", "B", "A"],
    "Sales_Rep": ["John", "Jane", "Bob", "Alice", "John",
                  "Jane", "Bob", "Alice", "John", "Jane",
                  "Bob", "Alice", "John", "Jane", "Bob"],
    "Units_Sold": [100, 150, 80, 200, 120,
                   90, 180, 110, 95, 140,
                   160, 130, 105, 125, 170],
    "Revenue": [1000, 2250, 800, 3000, 1800,
                1350, 2700, 1650, 950, 2100,
                2400, 1950, 1050, 1875, 2550],
    "Cost": [600, 1500, 500, 2000, 1100,
             900, 1800, 1100, 600, 1400,
             1600, 1300, 700, 1250, 1700]
})

print("\n[Step 1] Sales Dataset:")
print(sales.to_string(index=False))

print("\n" + "=" * 70)
print("[Step 2] Basic Groupby - Total Revenue by Region:")
print("=" * 70)
print(sales.groupby("Region")["Revenue"].sum().to_string())

print("\n" + "=" * 70)
print("[Step 3] Groupby with Multiple Aggregations (list):")
print("=" * 70)
print("Revenue statistics by Region:")
revenue_stats = sales.groupby("Region")["Revenue"].agg([
    "sum", "mean", "min", "max", "std", "count"
]).round(2)
print(revenue_stats.to_string())

print("\n" + "=" * 70)
print("[Step 4] Named Aggregations:")
print("=" * 70)
named_agg = sales.groupby("Region").agg(
    Total_Revenue=("Revenue", "sum"),
    Average_Revenue=("Revenue", "mean"),
    Total_Units=("Units_Sold", "sum"),
    Average_Units=("Units_Sold", "mean"),
    Best_Sales_Rep=("Sales_Rep", "first"),
    Transactions=("Revenue", "count")
).round(2)
print(named_agg.to_string())

print("\n" + "=" * 70)
print("[Step 5] Different Aggregations for Different Columns:")
print("=" * 70)
multi_col_agg = sales.groupby("Region").agg({
    "Revenue": ["sum", "mean", "std"],
    "Units_Sold": ["sum", "mean", "min", "max"],
    "Cost": "sum",
    "Sales_Rep": "nunique"
})
print(multi_col_agg.round(2).to_string())

print("\n" + "=" * 70)
print("[Step 6] Custom Aggregation Functions:")
print("=" * 70)

custom_agg = sales.groupby("Region").agg(
    Total_Revenue=("Revenue", "sum"),
    Average_Revenue=("Revenue", "mean"),
    Median_Revenue=("Revenue", "median"),
    Revenue_Range=("Revenue", lambda x: x.max() - x.min()),
    Revenue_Coefficient_of_Variation=("Revenue", lambda x: x.std() / x.mean() if x.mean() > 0 else 0),
    Total_Profit=("Revenue", lambda x: (x - sales.loc[x.index, "Cost"]).sum()),
    Best_Performing_Rep=("Revenue", lambda x: sales.loc[x.idxmax(), "Sales_Rep"] if len(x) > 0 else None)
).round(2)

print(custom_agg.to_string())

print("\n" + "=" * 70)
print("[Step 7] Groupby with Multiple Keys (Region + Product):")
print("=" * 70)
multi_key = sales.groupby(["Region", "Product"]).agg(
    Total_Revenue=("Revenue", "sum"),
    Avg_Revenue=("Revenue", "mean"),
    Total_Units=("Units_Sold", "sum"),
    Unique_Reps=("Sales_Rep", "nunique")
).round(2)

print(multi_key.to_string())

print("\n" + "=" * 70)
print("[Step 8] Transform - Add Region Average Back to Original Data:")
print("=" * 70)

sales_with_region_avg = sales.copy()
sales_with_region_avg["Region_Avg_Revenue"] = sales.groupby("Region")["Revenue"].transform("mean")
sales_with_region_avg["Region_Total_Revenue"] = sales.groupby("Region")["Revenue"].transform("sum")
sales_with_region_avg["Revenue_vs_Region_Avg"] = (
    sales_with_region_avg["Revenue"] - sales_with_region_avg["Region_Avg_Revenue"]
)

print(sales_with_region_avg.to_string(index=False))

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

summary = """
Key Points about .agg():

1. Single function per column:
   df.groupby("key")["col"].agg(["sum", "mean", "std"])

2. Named aggregations (pandas 0.25+):
   df.groupby("key").agg(
       NewColName=("original_col", "function"),
       AnotherCol=("other_col", "function")
   )

3. Dictionary syntax for different functions per column:
   df.groupby("key").agg({
       "col1": ["func1", "func2"],
       "col2": "func3"
   })

4. Custom functions:
   - Use lambda functions
   - Use named functions
   - Must return a single value per group

5. transform() vs agg():
   - agg() returns one row per group
   - transform() returns same shape as original, broadcasting group values
"""
print(summary)
