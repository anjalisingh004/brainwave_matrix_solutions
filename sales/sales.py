import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Sales Data (Assuming CSV File)
file_path = "C:\\Users\\anjal\\OneDrive\\Desktop\\sales\\Sales_Data.csv"
  # Change this to your actual file path
df = pd.read_csv(file_path)

# Convert 'Order Date' to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Monthly Sales Analysis
monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(10, 5))
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker="o", color="b")
plt.title("Total Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales Revenue")
plt.xticks(range(1, 13))
plt.grid()
plt.show()

# Top 10 Best-Selling Products
top_products = df.groupby("Product")["Sales"].sum().nlargest(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.title("Top 10 Best-Selling Products")
plt.xlabel("Total Sales")
plt.ylabel("Product")
plt.show()

# City-Wise Sales Distribution
city_sales = df.groupby("City")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x=city_sales.index, y=city_sales.values, palette="coolwarm")
plt.xticks(rotation=45)
plt.title("Total Sales by City")
plt.xlabel("City")
plt.ylabel("Sales Revenue")
plt.show()

# Hourly Sales Trend
hourly_sales = df.groupby("Hour")["Sales"].sum()

plt.figure(figsize=(10, 5))
sns.lineplot(x=hourly_sales.index, y=hourly_sales.values, marker="o", color="g")
plt.title("Sales Trend by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Sales Revenue")
plt.grid()
plt.show()
