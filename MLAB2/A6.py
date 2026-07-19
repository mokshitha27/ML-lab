import pandas as pd
import numpy as np

def load_data():
    file = "Lab Session Data.xlsx"
    return pd.read_excel(file, sheet_name="Purchase data")

def cosine_similarity(v1, v2):
    dot = np.dot(v1, v2)
    mag1 = np.linalg.norm(v1)
    mag2 = np.linalg.norm(v2)
    return dot, mag1, mag2, dot / (mag1 * mag2)

def main():
    df = load_data()

    v1 = df.loc[0, ["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)", "Payment (Rs)"]].to_numpy(dtype=float)

    v2 = df.loc[1, ["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)", "Payment (Rs)"]].to_numpy(dtype=float)

    dot, mag1, mag2, cosine = cosine_similarity(v1, v2)

    print("Vector A")
    print(v1)

    print("\nVector B")
    print(v2)

    print("\nDot Product =", dot)
    print("Magnitude of A =", mag1)
    print("Magnitude of B =", mag2)

    print("\nCosine Similarity =", cosine)

if __name__ == "__main__":
    main()