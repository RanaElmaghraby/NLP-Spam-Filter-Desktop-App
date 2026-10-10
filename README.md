# 🛡️ TeleShield AI — Explainable SMS Spam Detection System

An end-to-end Machine Learning desktop application designed to detect and filter SMS spam messages with real-time word-level explanations. 

Built with **Scikit-learn**, **TF-IDF Vectorization**, **Multinomial Naive Bayes**, and wrapped in an intuitive dark-themed **Tkinter GUI**.

---

## 🌟 Key Features

- **High-Performance NLP Classification:** Powered by a tuned TF-IDF + Multinomial Naive Bayes pipeline achieving high recall and precision on SMS spam datasets.
- **Explainable AI (XAI):** Unpacks the model's decision by computing log-probability differentials (`feature_log_prob_`) to display top trigger keywords driving the spam verdict.
- **Standalone Windows Executable:** No Python installation or runtime environment required for end users.
- **Dark-Themed GUI:** Minimalist desktop interface designed with Tkinter.

---

## 🚀 Download & Quick Start

### For End-Users (Direct Download)
1. Head over to the [Releases](https://github.com/RanaElmaghraby/NLP-Spam-Filter-Desktop-App/releases/latest) section.
2. Download `TeleShieldAI.exe` under **Assets**.
3. Double-click the file to launch the application.

---

## 🛠️ Project Structure

```text
├── app.py                                         # Main Tkinter desktop application
├── spam_classifier_pipeline.pkl                   # Exported Scikit-Learn TF-IDF + Naive Bayes pipeline
├── teleshield-spam-detection-91-recall-99-p.ipynb # Data preprocessing, EDA, training & evaluation
├── teleShield.ico                                 # Custom application icon
├── TeleShieldAI.spec                              # PyInstaller build specification
└── README.md                                      # Documentation
