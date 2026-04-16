import pandas as pd

def main():
    clean_df()

def clean_df():
    print("creating data frame")
    df = pd.read_csv('./Sales Dataset.csv')

    clean_df = df[
        ~(df["Category"] == "Furniture")
        & ~(df["Sub-Category"] == "Electronic Games")
        & ~(df["Year-Month"].str[:4].isin(["2020", "2025"]))
        ]

    print("data frame created")
    return clean_df

if __name__ == "__main__":
    main()
