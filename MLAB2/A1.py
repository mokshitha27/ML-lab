import pandas as pd
import numpy as np

def load_data():
    file = "Lab Session Data.xlsx"
    return pd.read_excel(file, sheet_name="Purchase data")

def get_matrices(df):
    X = df[["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)"]].to_numpy()
    y = df["Payment (Rs)"].to_numpy()
    return X, y

def find_cost(X, y):
    return np.linalg.pinv(X) @ y

def main():
    df = load_data()

    X, y = get_matrices(df)

    print("Dataset\n")
    print(df)

    print("\nFeature Matrix (X)\n")
    print(X)

    print("\nOutput Vector (y)\n")
    print(y)

    print("\nDimensionality of Vector Space:", X.shape[1])

    print("Number of Vectors:", X.shape[0])

    rank = np.linalg.matrix_rank(X)
    print("Rank of Feature Matrix:", rank)

    cost = find_cost(X, y)

    print("\nCost of Products")
    print("Candy        :", round(cost[0], 2))
    print("Mango (Kg)   :", round(cost[1], 2))
    print("Milk Packet  :", round(cost[2], 2))

    predicted = X @ cost

    print("\nPredicted Payments")
    print(np.round(predicted, 2))

    print("\nActual Payments")
    print(y)

    result = pd.DataFrame({
        "Actual": y,
        "Predicted": np.round(predicted, 2)
    })

    print("\nComparison")
    print(result)

if __name__ == "__main__":
    main()