import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("TASK 8.xlsx",sheet_name="Dataset")

## Total Revenue
print("\nTotal_Revenue\n",df["Revenue"].sum())

## Revenue by Plan
print("\nRevenue by Plan\n",df.groupby("Plan")["Revenue"].sum().sort_values(ascending=False))

## Average Retention
print("\nAverage_Retention\n",df.groupby("Plan")["MonthsActive"].mean())

## Device Counts
print("\nDevice_Usage\n",df["Device"].value_counts())

## Revenue by City
print("\nRevenue by City\n",df.groupby("City")["Revenue"].sum().sort_values(ascending=False))

## Revenue by Device
print("\nRevenue by Device\n",df.groupby("Device")["Revenue"].sum().sort_values(ascending=False))

## Visualizations

df.groupby("Device")["Revenue"].sum().plot(kind="pie")
plt.title("Revenue by Device")
plt.show()

df.groupby("JoinDate")["Revenue"].sum().plot(kind="line")
plt.title("Revenue by JoinDate")
plt.show()
