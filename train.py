import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_score

df = pd.read_csv("heart_anonymized.csv")

X = df.drop(columns=['encrypted_patient_id', 'encrypted_patient_name', 'target'])
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

joblib.dump(scaler, "scaler.pkl")

model = LogisticRegression(penalty='l2', max_iter=1000, random_state=42)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)
precision = precision_score(y_test, y_pred)

print(f"\n✅ Model Training Complete!")
print(f"🎯 Achieved Precision: {precision * 100:.2f}%\n")

joblib.dump(model, "heart_model.pkl")
print("💾 Model saved as 'heart_model.pkl'")