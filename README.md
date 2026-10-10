# 🛡️ TeleShield AI — Explainable SMS Spam Detection System

An end-to-end Machine Learning desktop application designed to detect and filter SMS spam messages with real-time word-level explanations. 

Built with **Scikit-learn**, **TF-IDF Vectorization**, **Multinomial Naive Bayes**, and wrapped in an intuitive dark-themed **Tkinter GUI**.

---

## 🔗 Quick Links

- 🎬 **[Watch Demo Video (Google Drive)](https://drive.google.com/file/d/17bL7Q-niDv8ZEOLwayyBXuUGBz8GLYV2/view?usp=sharing)**
- 📓 **[Kaggle Notebook: Training & Evaluation (91% Recall, 99% Precision)](https://www.kaggle.com/code/ranaahmedelmaghraby/teleshield-spam-detection-91-recall-99-p)**
- 💻 **[Download Desktop App (v1.0.0)](https://github.com/RanaElmaghraby/NLP-Spam-Filter-Desktop-App/releases/latest)**

---

## 🌟 Key Features

- **High-Performance NLP Pipeline:** Powered by a tuned TF-IDF + Multinomial Naive Bayes classifier reaching **91% Recall** and **99% Precision**.
- **Explainable AI (XAI):** Unpacks model predictions via log-probability differentials (`feature_log_prob_`), highlighting key trigger words that influenced the spam verdict.
- **Standalone Windows Executable:** Runs out-of-the-box without requiring a local Python runtime.
- **Modern Dark GUI:** Minimalist desktop interface built using Tkinter.

---

## 🎥 Application Demo

Check out the live recording demonstrating real-time message inference and word-level explanation:

👉 **[Click here to watch the Video Demo](https://drive.google.com/file/d/17bL7Q-niDv8ZEOLwayyBXuUGBz8GLYV2/view?usp=sharing)**

---

## 🚀 Download & Quick Start

### For End-Users (Direct Download)
1. Go to the [Releases](https://github.com/RanaElmaghraby/NLP-Spam-Filter-Desktop-App/releases/latest) section.
2. Download `TeleShieldAI.exe` from **Assets**.
3. Double-click the file to launch the application.

---

## 🛠️ Project Structure

```text
├── app.py                                         # Main Tkinter desktop application
├── spam_classifier_pipeline.pkl                   # Exported Scikit-Learn TF-IDF + Naive Bayes pipeline
├── teleshield-spam-detection-91-recall-99-p.ipynb # Data preprocessing, EDA, training & evaluation
├── teleShield.ico                                 # Custom application icon
├── TeleShieldAI.spec                              # PyInstaller build specification
└── README.md                                      # Project documentation
```

---

## 💻 Local Setup & Development

If you prefer to run or build the application from source:

### 1. Clone the repository
```bash
git clone https://github.com/RanaElmaghraby/NLP-Spam-Filter-Desktop-App.git
cd NLP-Spam-Filter-Desktop-App
```

### 2. Install dependencies
```bash
pip install scikit-learn joblib
```

### 3. Run the GUI app
```bash
python app.py
```

### 4. Build Executable via PyInstaller
```powershell
pyinstaller --clean TeleShieldAI.spec
```

---

## 🧠 Model Architecture & Interpretability

1. **Text Vectorization:** Uses `TfidfVectorizer` to extract word and sub-sequence features.
2. **Probabilistic Classification:** Utilizes `MultinomialNB` optimized for spam text classification.
3. **Interpretability Formula:**
   $$\Delta \log P(w) = \log P(w \mid \text{Spam}) - \log P(w \mid \text{Ham})$$
   Words with the highest positive log-likelihood differences are extracted and surfaced to the UI as explicit reasons for the decision.

---

## 👤 Author
- **Rana Ahmed Elmaghraby** — [GitHub](https://github.com/RanaElmaghraby) • [Kaggle](https://www.kaggle.com/ranaahmedelmaghraby)
