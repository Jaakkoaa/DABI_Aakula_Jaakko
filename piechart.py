import pandas as pd
import matplotlib.pyplot as plt


def create_category_pie_chart():
    df = pd.read_csv('./Sales Dataset.csv')
    category_amounts = (
        df.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(8, 8))
    plt.pie(
        category_amounts.values,
        labels=category_amounts.index,
        autopct="%1.1f%%",
        startangle=90,
    )
    plt.title("Summed Amount by Category")
    plt.tight_layout()
    plt.savefig("category_pie_chart.png")
    plt.close()


if __name__ == "__main__":
    create_category_pie_chart()
