import pandas as pd
import joblib
from security import decrypt_data, encrypt_data

scaler = joblib.load("scaler.pkl")
model = joblib.load("heart_model.pkl")

raw_patient_id = "PATIENT_9999"
encrypted_id = encrypt_data(raw_patient_id)

patient_metrics = pd.DataFrame([{
    'age': 58, 'sex': 1, 'cp': 2, 'trestbps': 140, 'chol': 211,
    'fbs': 1, 'restecg': 0, 'thalach': 165, 'exang': 0,
    'oldpeak': 0.0, 'slope': 2, 'ca': 0, 'thal': 2
}])

patient_scaled = scaler.transform(patient_metrics)


prediction = model.predict(patient_scaled)[0]
probability = model.predict_proba(patient_scaled)[0][1]

decrypted_id = decrypt_data(encrypted_id)

print("="*40)
print("  PATIENT CARDIAC RISK REPORT  ")
print("="*40)
print(f"Encrypted ID Sent : {encrypted_id[:20]}...")
print(f"Decrypted ID (RAM): {decrypted_id}")
print(f"Risk Probability  : {probability * 100:.2f}%")

if prediction == 1:
    print("STATUS            : ⚠️ HIGH RISK (Require Attention)")
else:
    print("STATUS            : ✅ LOW RISK (Healthy)")
print("="*40)