from clean import clean_df
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import pearsonr

def main():
    df = clean_df()

    print(get_category_amounts(df))

    print("Electronics correlation between time and revenue")
    electronics_df = df[df["Category"] == "Electronics"]
    print(get_correlation(electronics_df))

    print("Office Supplies correlation between time and revenue")
    office_supplies_df = df[df["Category"] == "Office Supplies"]
    print(get_correlation(office_supplies_df))

    create_line_chart(df)

def get_category_amounts(df):
    subcategory_amounts = (
        df.groupby("Sub-Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 6))
    plt.bar(subcategory_amounts.index, subcategory_amounts.values, color="steelblue")
    plt.title("Summed Amount by Sub-Category")
    plt.xlabel("Sub-Category")
    plt.ylabel("Summed Amount")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("sub_category_bar.png")

    category_amounts = (
        df.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    return category_amounts


def get_correlation(df):
    monthly = get_monthly_revenue(df)
    monthly["MonthNumber"] = range(len(monthly))

    return pearsonr(monthly["Amount"], monthly["MonthNumber"])

def create_line_chart(df):
    plt.figure(figsize=(10, 6))

    for category in ["Electronics", "Office Supplies"]:
        category_df = df[df["Category"] == category]
        monthly = get_monthly_revenue(category_df)
        plt.plot(monthly["Year-Month"], monthly["Amount"], marker="o", label=category)

    plt.title("Monthly Revenue by Category")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45, ha="right")
    plt.legend()
    plt.tight_layout()
    plt.savefig("monthly_revenue_line.png")
    plt.close()

def get_monthly_revenue(df):
    temp = df[["Amount", "Year-Month"]].copy()
    temp["Year-Month"] = pd.to_datetime(temp["Year-Month"], format="%Y-%m")
    temp = temp.dropna()

    return (
        temp.groupby("Year-Month", as_index=False)["Amount"]
        .sum()
        .sort_values("Year-Month")
    )

if __name__ == "__main__":
    main()
