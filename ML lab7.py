import os
import numpy as np
import pandas as pd
from PIL import Image
folder = "images"
files = os.listdir(folder)
rows = []
for file in files:
    if file.endswith(".jpg"):
        path = os.path.join(folder, file)
        img = Image.open(path).convert("RGB")
        img = np.array(img)
        red = img[:, :, 0].mean()
        green = img[:, :, 1].mean()
        blue = img[:, :, 2].mean()
        bright = img.mean()
        std = img.std()
        if "_d" in file:
            label = "d"
        elif "_g" in file:
            label = "g"
        elif "_h" in file:
            label = "h"
        rows.append([
            file,
            red,
            green,
            blue,
            bright,
            std,
            label
        ])
data = pd.DataFrame(
    rows,
    columns=[
        "image",
        "red",
        "green",
        "blue",
        "bright",
        "std",
        "label"
    ]
)
print(data.head())
print("\nNumber of images:", len(data))
print("\nClass count:")
print(data["label"].value_counts())

# A1

def entropy(label):
    values, counts = np.unique(label, return_counts=True)
    total = len(label)
    result = 0
    for count in counts:
        p = count / total
        result = result - p * np.log2(p)
    return result
answer = entropy(data["label"])
print("\nEntropy:", answer)

#A2
def gini(label):
    values, counts = np.unique(label, return_counts=True)
    total = len(label)
    result = 0
    for count in counts:
        p = count / total
        result = result + p ** 2
    gini_value = 1 - result
    return gini_value
gini_answer = gini(data["label"])
print("\nGini Index:", gini_answer)

#A3
def bins(column):
    return pd.cut(column, bins=4)
def info_gain(data, feature, target):
    parent = entropy(data[target])
    groups = data.groupby(feature, observed=True)
    child = 0
    for name, group in groups:
        p = len(group) / len(data)
        child = child + p * entropy(group[target])
    gain = parent - child
    return gain
data["red_bin"] = bins(data["red"])
data["green_bin"] = bins(data["green"])
data["blue_bin"] = bins(data["blue"])
data["bright_bin"] = bins(data["bright"])
data["std_bin"] = bins(data["std"])
features = [
    "red_bin",
    "green_bin",
    "blue_bin",
    "bright_bin",
    "std_bin"
]
gains = {}
for feature in features:
    gains[feature] = info_gain(
        data,
        feature,
        "label"
    )
    print(feature, ":", gains[feature])
root = max(gains, key=gains.get)
print("\nRoot feature:", root)
print("Information gain:", gains[root])

#A4
def binning(column, bins=4, kind="width"):
    if kind == "width":
        result = pd.cut(column, bins=bins)
    else:
        result = pd.qcut(column, q=bins, duplicates="drop")
    return result
data["red_width"] = binning(
    data["red"],
    4,
    "width"
)
data["red_frequency"] = binning(
    data["red"],
    4,
    "frequency"
)
print("\nEqual Width Binning:")
print(data[["red", "red_width"]].head())
print("\nEqual Frequency Binning:")
print(data[["red", "red_frequency"]].head())

#A7
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
x = data[["green", "bright"]]
y = data["label"]
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y
)
tree = DecisionTreeClassifier(
    criterion="entropy",
    max_depth=4,
    random_state=42
)
tree.fit(x_train, y_train)
green_min = x["green"].min() - 1
green_max = x["green"].max() + 1
bright_min = x["bright"].min() - 1
bright_max = x["bright"].max() + 1
xx, yy = np.meshgrid(
    np.linspace(green_min, green_max, 300),
    np.linspace(bright_min, bright_max, 300)
)
grid = pd.DataFrame({
    "green": xx.ravel(),
    "bright": yy.ravel()
})
pred = tree.predict(grid)
numbers = {"d": 0, "g": 1, "h": 2}
pred = pd.Series(pred).map(numbers).values
pred = pred.reshape(xx.shape)
plt.figure(figsize=(10, 7))
plt.contourf(xx, yy, pred, alpha=0.3)
for label in ["d", "g", "h"]:
    points = y == label
    plt.scatter(
        x.loc[points, "green"],
        x.loc[points, "bright"],
        label=label
    )
plt.xlabel("Green")
plt.ylabel("Brightness")
plt.title("Decision Boundary")
plt.legend()
plt.show()

#A8
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
x = data[["green", "bright"]]
y = data["label"]
tree = DecisionTreeClassifier(random_state=42)
params = {
    "criterion": ["gini", "entropy"],
    "max_depth": [2, 3, 4, 5, 6],
    "min_samples_split": [2, 5, 10]
}
search = GridSearchCV(
    tree,
    params,
    cv=5,
    scoring="accuracy"
)
search.fit(x, y)
print("Best Parameters:", search.best_params_)
print("Best Accuracy:", search.best_score_)