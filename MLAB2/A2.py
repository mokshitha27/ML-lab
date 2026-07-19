import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def load_data():
    file = "Lab Session Data.xlsx"
    return pd.read_excel(file, sheet_name="Purchase data")

def create_labels(df):
    df["Class"] = df["Payment (Rs)"].apply(
        lambda x: "RICH" if x > 200 else "POOR"
    )
    return df

def train_classifier(X, y):
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(X, y)
    return model

def main():
    df = load_data()
    df = create_labels(df)

    X = df[["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)"]]
    y = df["Class"]

    model = train_classifier(X, y)

    prediction = model.predict(X)

    print("Accuracy:", accuracy_score(y, prediction))

    print("\nConfusion Matrix")
    print(confusion_matrix(y, prediction))

    print("\nClassification Report")
    print(classification_report(y, prediction, zero_division=0))

    df["Predicted Class"] = prediction

    print("\nCustomer Classification")
    print(df[["Customer", "Payment (Rs)", "Class", "Predicted Class"]])

if __name__ == "__main__":
    main()