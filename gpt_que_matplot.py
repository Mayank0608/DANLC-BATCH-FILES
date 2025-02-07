import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample sales data
data = {
    'SalesDate': pd.date_range(start='2024-01-01', periods=12, freq='ME'),  # Fixed FutureWarning (use 'ME' instead of 'M')
    'ProductName': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'] * 2 + ['Product A', 'Product B'],
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'SalesQuantity': np.random.randint(50, 200, 12),
    'Price': np.random.randint(500, 2000, 12)
}

# Creating DataFrame
df = pd.DataFrame(data)

# Calculate total sales amount per product
df['TotalSales'] = df['SalesQuantity'] * df['Price']
product_sales = df.groupby('ProductName')['TotalSales'].sum()

# Calculate total sales by region
region_sales = df.groupby('Region')['TotalSales'].sum()

# Total sales over time
sales_over_time = df.groupby('SalesDate')['TotalSales'].sum()

# Create bar chart - Total Sales per Product
plt.figure(figsize=(8, 5))
sns.barplot(x=product_sales.index, y=product_sales.values, hue=product_sales.index, palette='viridis', legend=False)  # Fixed FutureWarning
plt.xlabel("Product Name")
plt.ylabel("Total Sales ($)")
plt.title("Total Sales by Product")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Create pie chart - Sales Distribution by Region
plt.figure(figsize=(7, 7))
plt.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%', colors=['blue', 'green', 'red', 'purple'], startangle=140)
plt.title("Sales Distribution by Region")
plt.show()

# Create line chart - Sales Over Time
plt.figure(figsize=(8, 5))
plt.plot(sales_over_time.index, sales_over_time.values, marker='o', color='b', linestyle='-')
plt.xlabel("Sales Date")
plt.ylabel("Total Sales ($)")
plt.title("Total Sales Trend Over Time")
plt.grid()
plt.xticks(rotation=45)
plt.show()

# Conclusion
print("Insights:")
print("- The bar chart shows which products generate the highest revenue.")
print("- The pie chart highlights the strongest sales regions.")
print("- The line chart helps track revenue trends over time, showing growth or decline patterns.")
