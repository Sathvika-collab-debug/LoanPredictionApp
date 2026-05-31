import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("loan_data.csv")
df = df.dropna()

# Encode
df["Gender"] = df["Gender"].map({"Male": 1, "Female": 0})
df["Married"] = df["Married"].map({"Yes": 1, "No": 0})
df["Education"] = df["Education"].map({"Graduate": 1, "Not Graduate": 0})
df["Loan_Status"] = df["Loan_Status"].map({"Y": 1, "N": 0})

# Features
X = df.drop("Loan_Status", axis=1)
y = df["Loan_Status"]

# IMPORTANT FIX: stratify keeps balance
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# IMPORTANT FIX: stronger model control
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=3,
    min_samples_leaf=1,
    class_weight="balanced",   # 🔥 KEY FIX
    random_state=42
)

model.fit(X_train, y_train)

pickle.dump(model, open("model.pkl", "wb"))

print("Fixed model created successfully!")
print(df["Loan_Status"].value_counts())