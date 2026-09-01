import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"

columns = [
    'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 
    'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 
    'ca', 'thal', 'target'
]

df = pd.read_csv(url, names=columns, na_values='?')

df = df.dropna()

df['target'] = df['target'].apply(lambda x: 1 if x > 0 else 0)

df.to_csv("heart_cleveland_cleaned.csv", index=False)
print("Data Downloaded & Cleaned Successfully!")