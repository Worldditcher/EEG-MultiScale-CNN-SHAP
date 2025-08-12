# EEG Classification with Multi-Scale CNN & SHAP

## 📌 Overview
This project classifies EEG signals using a **Multi-Scale Convolutional Neural Network (MSCNN)** and explains predictions with **SHAP** for transparency in healthcare use cases.

- Problem: Movement intention/EEG pattern classification with clinically useful explanations  
- Approach: Clean & segment EEG → extract multi-domain features → train MSCNN → interpret with SHAP  
- Result: **77.92% accuracy** on ~9,258 augmented epochs; MSCNN outperformed SVM/RF baselines by **6–10%**

## 🧠 Dataset
- Source: **PhysioNet EEG** (109 subjects; Sharbrough/64-channel montage)  
- After preprocessing & augmentation: **~9,258 epochs**  
- NOTE: Access dataset directly from PhysioNet (follow their license/terms)

## ⚙️ Pipeline
1. **Preprocessing:**  
   Bandpass (0.5–40 Hz), 50 Hz notch, **ICA** for artifacts, re-referencing, epoching  
2. **Feature extraction (multi-domain):**  
   - **Time:** mean, variance, skewness, kurtosis, Hjorth  
   - **Frequency:** PSD/FFT features, band powers (delta→gamma)  
   - **Wavelet:** DWT energies/statistics  
3. **Models:**  
   - Baselines: **SVM**, **Random Forest**  
   - Main: **Multi-Scale CNN** (parallel conv blocks with different kernel sizes; GAP + dense head)  
4. **Explainability:**  
   - **SHAP** to understand feature contributions per prediction (global + local)

## 📈 Results
- MSCNN test accuracy: **77.92%**  
- Visuals (see `/results`): confusion matrix, accuracy curve, SHAP summary

## 🛠 Tech Stack
**Python**, **MNE**, **NumPy/Pandas**, **Scikit-learn**, **TensorFlow/Keras**, **SHAP**, **Matplotlib**

## 📂 Project Structure

EEG-MultiScale-CNN-SHAP/
├─ notebooks/
│ ├─ 01_preprocess_and_features.ipynb
│ ├─ 02_train_baselines.ipynb
│ └─ 03_train_mscnn_and_shap.ipynb
├─ results/
│ ├─ confusion_matrix.png
│ ├─ accuracy_curve.png
│ └─ shap_summary.png
├─ requirements.txt
└─ README.md

## ▶️ Quick Start
1) Create a virtual env and install deps:

python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

2) Open the notebooks in /notebooks in order (01 → 03).

3) Place your raw data where the notebook expects it (update paths in the first cell).

4) Export plots to /results from the notebooks.

🖼 Key Figures
• results/confusion_matrix.png — test performance overview

• results/accuracy_curve.png — training/validation accuracy vs epochs

• results/shap_summary.png — global feature importance (SHAP)

✅ Notes
• No subject leakage (per-subject splits)

• Reproducible seeds set for training & feature extraction

• Clear separation of Check → Apply → Visualize steps per preprocessing block

📢 Status
• Core pipeline complete.

• TODO: Add cross-validation results & per-class metrics.

• TODO: Upload a minimal sample of preprocessed epochs (if licensing permits) to ease reproduction.

📜 License
This repo is for academic/educational use. Follow PhysioNet terms for original data.

---

# Step 3: Add `requirements.txt`

Create a file named **requirements.txt** with this minimal set:
numpy
pandas
scikit-learn
mne
matplotlib
tensorflow
shap
pywavelets


Commit & push:
```bash
git add requirements.txt README.md
git commit -m "docs: add full README and requirements"
git push


