import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
import warnings
warnings.filterwarnings('ignore')

# Load data
df = pd.read_csv('bank.csv')

# Show columns (debug)
print("Columns found:", df.columns.tolist())

# Target: poutcome = success (1) vs others (0)
df['target'] = (df['poutcome'] == 'success').astype(int)

# YOUR EXACT COLUMNS from screenshot
features = ['age', 'job', 'marital', 'education', 'default', 'housing',
           'loan', 'campaign', 'pdays', 'previous', 'month']

# Encode categoricals
le = LabelEncoder()
for col in ['job', 'marital', 'education', 'default', 'housing', 'loan', 'month']:
    df[col] = le.fit_transform(df[col].astype(str))

# Prepare data (safe columns only)
available_features = [f for f in features if f in df.columns]
X = df[available_features]
y = df['target']

print(f"Using features: {available_features}")

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression
model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# Results
print("\nBank Marketing Prediction Model")
print("="*50)
print(classification_report(y_test, y_pred))
print(f"Accuracy: {model.score(X_test, y_test):.1%}")

# Export predictions
results = X_test.copy()
results['actual_success'] = y_test
results['predicted_success'] = y_pred
results['success_probability'] = y_prob
results.to_csv('bank_predictions.csv', index=False)

print("\n✅ Saved: bank_predictions.csv")
