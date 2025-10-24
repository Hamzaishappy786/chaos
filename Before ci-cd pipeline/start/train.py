import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset
df = pd.read_csv('data/dataset.csv')
X = df[['feature1', 'feature2']]
y = df['label']

model = LogisticRegression()
model.fit(X, y)

# Save model
joblib.dump(model, 'model.pkl')
print("✅ Model trained and saved.")