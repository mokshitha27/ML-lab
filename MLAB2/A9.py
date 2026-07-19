import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_data():
    file = "Lab Session Data.xlsx"
    return pd.read_excel(file, sheet_name="Purchase data")

def normalize(df):
    scaler = MinMaxScaler()

    cols = [
        "Candies (#)",
        "Mangoes (Kg)",
        "Milk Packets (#)",
        "Payment (Rs)"
    ]

    df[cols] = scaler.fit_transform(df[cols])

    return df

def main():
    df = load_data()

    df = df[[
        "Customer",
        "Candies (#)",
        "Mangoes (Kg)",
        "Milk Packets (#)",
        "Payment (Rs)"
    ]]

    df = normalize(df)

    print("Normalized Dataset\n")
    print(df)

if __name__ == "__main__":
    main()