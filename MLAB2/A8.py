import pandas as pd

def load_data():
    file = "Lab Session Data.xlsx"
    return pd.read_excel(file, sheet_name="Purchase data")

def main():
    df = load_data()
    df = df.dropna(axis=1, how="all")

    print("Missing Values Before Imputation\n")
    print(df.isnull().sum())

    columns = [
        "Candies (#)",
        "Mangoes (Kg)",
        "Milk Packets (#)",
        "Payment (Rs)"
    ]

    for col in columns:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].mean())

    print("\nMissing Values After Imputation\n")
    print(df.isnull().sum())

    print("\nDataset After Imputation\n")
    print(df)

if __name__ == "__main__":
    main()