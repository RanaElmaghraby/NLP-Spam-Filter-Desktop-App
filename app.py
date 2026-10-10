import tkinter as tk
from tkinter import messagebox
import joblib
import os
import sys
import re


# Resource Path
# =========================
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Load trained pipeline
# =========================
model = joblib.load(resource_path("spam_classifier_pipeline.pkl"))

# model = joblib.load("spam_classifier_pipeline.pkl")



# Get model components
# =========================
tfidf = model.named_steps["tfidf"]
nb = model.named_steps["nb"]

words = tfidf.get_feature_names_out()




# Prediction + Explanation
# =========================
def predict_message():

    message = message_entry.get("1.0", tk.END).strip()

    if not message:
        messagebox.showwarning("Warning","Please enter a message.")
        return

    # -------------------------
    # Prediction
    # -------------------------
    prediction = model.predict([message])[0]

    if prediction == 1:
        result_label.config(text="SPAM",fg="#FF5252")
    else:
        result_label.config(text="HAM",fg="#4CAF50")

    # -------------------------
    # Find spam-related words
    # -------------------------

    message_words = set(re.findall(r'[a-zA-Z]+', message.lower()))

    # SPAM probability - HAM probability
    spam_scores = (nb.feature_log_prob_[1] - nb.feature_log_prob_[0])

    # Sort words from most SPAM-related
    spam_words = words[spam_scores.argsort()[::-1]]

    # Find words from this message
    reasons = [ word for word in spam_words if word in message_words][:5]

    # -------------------------
    # Display explanation
    # -------------------------

    if reasons:
        explanation_text = ("Model explanation:\n" + ", ".join(reasons))
    else:
        explanation_text = ( "Model explanation:\n" "No strong spam words found.")

    explanation_label.config(text=explanation_text)


# Create Window
# =========================
root = tk.Tk()

root.title("TeleShield AI - SMS Spam Classifier")
root.geometry("600x500")
root.resizable(True, True)

root.configure(bg="#121212")


# Title
# =========================
title_label = tk.Label(
    root,
    text="TeleShield AI",
    font=("Arial", 24, "bold"),
    bg="#121212",
    fg="white"
)

title_label.pack(pady=(25, 5))


# Subtitle
# =========================
subtitle_label = tk.Label(
    root,
    text="SMS Spam Classification",
    font=("Arial", 13),
    bg="#121212",
    fg="#BDBDBD"
)

subtitle_label.pack(pady=(0, 20))


# Message Label
# =========================
message_label = tk.Label(
    root,
    text="Enter SMS message:",
    font=("Arial", 12, "bold"),
    bg="#121212",
    fg="white"
)

message_label.pack(anchor="w", padx=40)


# Text Box
# =========================
message_entry = tk.Text(
    root,
    height=8,
    width=60,
    font=("Arial", 11),
    bg="#1E1E1E",
    fg="white",
    insertbackground="white",
    relief="flat"
)

message_entry.pack(pady=10)


# Predict Button
# =========================
predict_button = tk.Button(
    root,
    text="Check Message",
    font=("Arial", 12, "bold"),
    command=predict_message,
    padx=20,
    pady=8,
    bg="#333333",
    fg="white",
    activebackground="#444444",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)

predict_button.pack(pady=15)


# Result Title
# =========================
result_title = tk.Label(
    root,
    text="Prediction:",
    font=("Arial", 12),
    bg="#121212",
    fg="#BDBDBD"
)

result_title.pack()


# Result
# =========================
result_label = tk.Label(
    root,
    text="---",
    font=("Arial", 22, "bold"),
    bg="#121212",
    fg="white"
)

result_label.pack(pady=5)


# Explanation
# =========================
explanation_label = tk.Label(
    root,
    text="Model explanation:\n---",
    font=("Arial", 11),
    bg="#121212",
    fg="#BDBDBD",
    wraplength=500,
    justify="left"
)

explanation_label.pack(
    pady=(15, 10)
)


# Run Application
# =========================
root.mainloop()