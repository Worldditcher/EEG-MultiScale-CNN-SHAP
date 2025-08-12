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
