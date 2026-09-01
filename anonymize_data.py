import pandas as pd
from security import encrypt_data

df = pd.read_csv("heart_cleveland_cleaned.csv")

encrypted_ids = []
encrypted_names = []

for i in range(len(df)):
    raw_id = f"PATIENT_{1000 + i}"
    raw_name = f"User_{i+1}"

    enc_id = encrypt_data(raw_id)
    enc_name = encrypt_data(raw_name)
    
    encrypted_ids.append(enc_id)
    encrypted_names.append(enc_name)

df.insert(0, 'encrypted_patient_id', encrypted_ids)
df.insert(1, 'encrypted_patient_name', encrypted_names)

df.to_csv("heart_anonymized.csv", index=False)
print("Anonymization Complete: Dataset saved as 'heart_anonymized.csv'")