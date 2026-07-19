import pandas as pd

def load_data():
    return pd.read_excel("Lab Session Data.xlsx", sheet_name="Purchase data")

def binary_vector(vector):
    return [1 if x > 0 else 0 for x in vector]

def similarity(v1, v2):
    f11 = f10 = f01 = f00 = 0
    for i in range(len(v1)):
        if v1[i] == 1 and v2[i] == 1:
            f11 += 1
        elif v1[i] == 1 and v2[i] == 0:
            f10 += 1
        elif v1[i] == 0 and v2[i] == 1:
            f01 += 1
        else:
            f00 += 1
    jc = f11 / (f11 + f10 + f01)
    smc = (f11 + f00) / (f11 + f10 + f01 + f00)
    return f11, f10, f01, f00, jc, smc

def main():
    data = load_data()
    v1 = data.loc[0, ["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)"]]
    v2 = data.loc[1, ["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)"]]
    b1 = binary_vector(v1)
    b2 = binary_vector(v2)
    f11, f10, f01, f00, jc, smc = similarity(b1, b2)

    print("Binary Vector 1:", b1)
    print("Binary Vector 2:", b2)
    print("\nf11 =", f11)
    print("f10 =", f10)
    print("f01 =", f01)
    print("f00 =", f00)
    print("\nJaccard Coefficient =", jc)
    print("Simple Matching Coefficient =", smc)

if __name__ == "__main__":
    main()