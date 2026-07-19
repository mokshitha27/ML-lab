import pandas as pd

def read_data():
    data = pd.read_excel("Lab Session Data.xlsx", sheet_name="thyroid0387_UCI")
    return data

def data_type(data):
    ans = {}
    for col in data.columns:
        if data[col].dtype == "object":
            ans[col] = "Nominal"
        else:
            ans[col] = "Numeric"
    return ans

def encoding(data):
    ans = {}
    for col in data.columns:
        if data[col].dtype == "object":
            if data[col].nunique() == 2:
                ans[col] = "Label Encoding"
            else:
                ans[col] = "One Hot Encoding"
    return ans

def data_range(data):
    ans = {}
    num = data.select_dtypes(include="number")
    for col in num.columns:
        low = num[col].min()
        high = num[col].max()
        ans[col] = [low, high]
    return ans

def missing_values(data):
    return data.isnull().sum()

def outliers(data):
    ans = {}
    num = data.select_dtypes(include="number")
    for col in num.columns:
        q1 = num[col].quantile(0.25)
        q3 = num[col].quantile(0.75)
        iqr = q3 - q1
        low = q1 - 1.5 * iqr
        high = q3 + 1.5 * iqr
        count = ((num[col] < low) | (num[col] > high)).sum()
        ans[col] = count
    return ans

def mean(data):
    num = data.select_dtypes(include="number")
    return num.mean()

def standard_deviation(data):
    num = data.select_dtypes(include="number")
    return num.std()

def main():
    data = read_data()
    types = data_type(data)
    encode = encoding(data)
    ranges = data_range(data)
    missing = missing_values(data)
    out = outliers(data)
    avg = mean(data)
    sd = standard_deviation(data)

    print("Data Types")
    for col in types:
        print(col, ":", types[col])

    print("\nEncoding")
    for col in encode:
        print(col, ":", encode[col])

    print("\nRange")
    for col in ranges:
        print(col, ":", ranges[col])

    print("\nMissing Values")
    print(missing)

    print("\nMean")
    print(avg)

    print("\nStandard Deviation")
    print(sd)

    print("\nOutliers")
    for col in out:
        print(col, ":", out[col])

if __name__ == "__main__":
    main()