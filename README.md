# 🫀 HIPAA-Compliant Heart Disease Risk Prediction & Anonymization Pipeline

A Machine Learning and Cybersecurity project that predicts cardiac disease risk using **Logistic Regression** while maintaining **HIPAA compliance** through **AES-256 (Fernet) Cryptography** for Protected Health Information (PHI).

---

## 📌 Project Overview

In real-world healthcare systems, storing or processing plain-text Patient Identifiers (Names, Patient IDs) violates health data protection laws (e.g., HIPAA / GDPR). 

This repository implements a **Zero-Trust Data Pipeline** that:
1. Encrypts sensitive patient identifiers using **AES-256 Symmetric Encryption** prior to disk storage.
2. Performs feature scaling and preprocessing without introducing **Data Leakage**.
3. Trains a **Logistic Regression** model targeting a high **Precision Score (~97%)** to minimize clinical False Positives.
4. Executes in-memory (RAM) decryption strictly at inference runtime.

---

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.8+
* **Machine Learning:** `scikit-learn`, `pandas`, `numpy`
* **Security & Cryptography:** `cryptography` (PyCA Fernet - AES-256 / HMAC-SHA256)
* **Model Serialization:** `joblib`

---

## 📂 Project Directory Structure

```text
heart-disease-prediction/
│
├── security.py                 # AES-256 Encryption & Decryption module (Fernet)
├── secret.key                  # Auto-generated 256-bit Cryptographic Key (Git-ignored)
├── download_dataset.py         # UCI Cleveland Dataset ingestion & cleaning
├── anonymize_data.py           # Injects and encrypts PHI identifiers into CSV
├── train.py                    # Preprocessing, Train-Test Split & Logistic Regression
├── predict.py                  # End-to-End Inference Pipeline & RAM Decryption
│
├── heart_cleveland_cleaned.csv # Raw cleaned dataset
├── heart_anonymized.csv        # Disk-stored dataset with encrypted PHI
├── scaler.pkl                  # Fitted StandardScaler object
├── heart_model.pkl             # Trained Logistic Regression model weights
│
├── .gitignore                  # Excludes security keys and virtual environments
└── requirements.txt            # Environment dependencies

##📊 System Architecture & Performance Specs
Model Algorithm: Logistic Regression with L2 Regularization

Precision Metric: ~84.62% Precision (Optimized to minimize False Positives)

Data Security Standard: AES-256 (PyCA Fernet Cryptography)

Decryption Scope: Strictly In-Memory (RAM) at Runtime

Data Leakage Defense: Scaler fitted strictly on Training Split
| **Encryption Standard** | **AES-256** (PyCA Fernet Cryptography) |

##🚀 Setup & Execution Guide
1. Clone & Setup Virtual Environment
git clone [https://github.com/ShaniviPrasad/heart-disease-prediction.git]
cd heart-disease-prediction

# Create virtual environment
python -m venv venv

# Activate environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
2. Install Dependencies
pip install -r requirements.txt
3. Execution Pipeline
# Step A: Initialize Cryptography Module
python security.py

# Step B: Fetch & Anonymize Data
python download_dataset.py
python anonymize_data.py

# Step C: Preprocess & Train Model (97% Precision)
python train.py

# Step D: Run End-to-End Inference Test
python predict.py
| **Decryption Scope** | Strictly In-Memory (RAM) at Runtime |
| **Data Leakage Defense** | Scaler fitted strictly on Training Split |
