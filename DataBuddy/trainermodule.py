import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load Dataset
dataset_file = "/home/sky/Desktop/DataBuddy/temp_dataset.pkl"
with open(dataset_file, "rb") as f:
    df = pd.read_pickle(f)
print("Dataset loaded successfully!")
print(df.head())

# Preprocess Data
df = df.dropna()  # Drop rows with missing values
categorical_columns = df.select_dtypes(include=["object"]).columns
df = pd.get_dummies(df, columns=categorical_columns, drop_first=True)
print("Data preprocessing completed!")
print(df.head())

# Split Data
X = df.drop("target", axis=1)  # Replace 'target' with the actual target column name
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Data split into training and testing sets!")

# Train Model
model_type = "Random Forest"  # Replace with dynamic selection if needed
if model_type == "Random Forest":
    model = RandomForestClassifier(random_state=42)
elif model_type == "Logistic Regression":
    model = LogisticRegression(random_state=42)

model.fit(X_train, y_train)
print("Model training completed!")

# Evaluate Model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
