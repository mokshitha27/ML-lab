import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity

def load_data():
    file = "Lab Session Data.xlsx"
    return pd.read_excel(file, sheet_name="Purchase data")

def main():
    df = load_data()

    data = df[["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)", "Payment (Rs)"]]

    binary = (data > 0).astype(int)

    n = len(binary)

    jc = np.zeros((n, n))
    smc = np.zeros((n, n))

    for i in range(n):
        for j in range(n):

            a = binary.iloc[i].values
            b = binary.iloc[j].values

            f11 = np.sum((a == 1) & (b == 1))
            f10 = np.sum((a == 1) & (b == 0))
            f01 = np.sum((a == 0) & (b == 1))
            f00 = np.sum((a == 0) & (b == 0))

            if (f11 + f10 + f01) != 0:
                jc[i][j] = f11 / (f11 + f10 + f01)

            smc[i][j] = (f11 + f00) / (f11 + f10 + f01 + f00)

    cosine = cosine_similarity(data)

    sns.heatmap(jc, annot=True, cmap="Blues")
    plt.title("Jaccard Coefficient")
    plt.show()

    sns.heatmap(smc, annot=True, cmap="Greens")
    plt.title("Simple Matching Coefficient")
    plt.show()

    sns.heatmap(cosine, annot=True, cmap="Reds")
    plt.title("Cosine Similarity")
    plt.show()

if __name__ == "__main__":
    main()