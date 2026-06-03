import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("loan_data.csv")

# Fill missing values
df = df.ffill()

# Convert categorical columns into numbers

df["Gender"] = df["Gender"].map({
    "Male": 1,
    "Female": 0
})

df["Married"] = df["Married"].map({
    "Yes": 1,
    "No": 0
})

df["Education"] = df["Education"].map({
    "Graduate": 1,
    "Not Graduate": 0
})

df["Self_Employed"] = df["Self_Employed"].map({
    "Yes": 1,
    "No": 0
})

df["Loan_Status"] = df["Loan_Status"].map({
    "Y": 1,
    "N": 0
})

# Convert Dependents column

df["Dependents"] = df["Dependents"].replace({
    "3+": 3
})

df["Dependents"] = pd.to_numeric(
    df["Dependents"],
    errors="coerce"
)

# Convert Property Area

df["Property_Area"] = df["Property_Area"].map({
    "Rural": 0,
    "Semiurban": 1,
    "Urban": 2
})

# Remove Loan ID column

df = df.drop("Loan_ID", axis=1)

# Fill remaining missing values

df = df.ffill()

# Split data

X = df.drop("Loan_Status", axis=1)

y = df["Loan_Status"]

# Train model

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# Save model

pickle.dump(
    model,
    open("model.pkl", "wb")
)

print("Model Saved Successfully")