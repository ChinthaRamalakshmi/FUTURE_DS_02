import pandas as pd

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("Dataset Loaded Successfully")

print("\nTotal Customers:")
print(len(df))

print("\nChurn Count:")
print(df["Churn"].value_counts())

print("\nChurn Percentage:")
print((df["Churn"].value_counts(normalize=True) * 100).round(2))

print("\nGender Wise Churn:")

print(pd.crosstab(df["gender"], df["Churn"]))

print("\nContract Wise Churn:")

print(pd.crosstab(df["Contract"], df["Churn"]))

print("\nInternet Service Wise Churn:")

print(pd.crosstab(df["InternetService"], df["Churn"]))

print("\nPayment Method Wise Churn:")

print(pd.crosstab(df["PaymentMethod"], df["Churn"]))


import matplotlib.pyplot as plt

churn_counts = df["Churn"].value_counts()

colors = ["lightgreen", "tomato"]

plt.figure(figsize=(7,7))

plt.pie(
    churn_counts,
    labels=churn_counts.index,
    autopct="%1.1f%%",
    colors=colors
)

plt.title("Customer Churn Distribution")

plt.show()



contract_churn = pd.crosstab(df["Contract"], df["Churn"])

contract_churn.plot(
    kind="bar",
    figsize=(10,5),
    color=["skyblue","orange"]
)

plt.title("Contract Wise Churn")
plt.xlabel("Contract Type")
plt.ylabel("Customers")
plt.grid(axis="y", linestyle="--")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

internet_churn = pd.crosstab(df["InternetService"], df["Churn"])

internet_churn.plot(
    kind="bar",
    figsize=(10,5),
    color=["green","red"]
)

plt.title("Internet Service Wise Churn")
plt.xlabel("Internet Service")
plt.ylabel("Customers")
plt.grid(axis="y", linestyle="--")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

payment_churn = pd.crosstab(df["PaymentMethod"], df["Churn"])

payment_churn.plot(
    kind="bar",
    figsize=(10,5),
    color=["purple","gold"]
)

plt.title("Payment Method Wise Churn")
plt.xlabel("Payment Method")
plt.ylabel("Customers")
plt.grid(axis="y", linestyle="--")

plt.tight_layout()

plt.show()