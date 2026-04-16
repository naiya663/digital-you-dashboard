import tkinter as tk
import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

def save_data():
    hours = entry_hours.get()
    subject = entry_subject.get()
    mood = entry_mood.get()

    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), hours, subject, mood])

    label_status.config(text="✅ Data Saved Successfully!", fg="lightgreen")

def show_graph():
    df = pd.read_csv("data.csv", names=["Date", "Hours", "Subject", "Mood"])
    df["Hours"] = pd.to_numeric(df["Hours"], errors="coerce")
    df = df.dropna()

    df.groupby("Subject")["Hours"].sum().plot(kind="pie", autopct="%1.1f%%")
    plt.title("Study Distribution")
    plt.show()

# Window
root = tk.Tk()
root.configure(bg="#1e1e2f")

tk.Label(root, text="📊 Digital You Dashboard",
         font=("Arial", 18, "bold"),
         bg="#1e1e2f", fg="white").pack(pady=10)
root.title("Digital You Dashboard")
root.geometry("400x400")
root.configure(bg="#1e1e2f")   # Dark background

# Title
tk.Label(root, text="📊 Digital You Dashboard", 
         font=("Arial", 16, "bold"), 
         bg="#1e1e2f", fg="white").pack(pady=10)

# Input Fields
def create_input(label_text):
    tk.Label(root, text=label_text, bg="#1e1e2f", fg="white").pack()
    entry = tk.Entry(root, bg="#2e2e3f", fg="white", insertbackground="white")
    entry.pack(pady=5)
    return entry

entry_hours = create_input("Study Hours")
entry_subject = create_input("Subject")
entry_mood = create_input("Mood")

# Buttons
tk.Button(root, text="Save Data", command=save_data,
          bg="#4CAF50", fg="white", width=20).pack(pady=10)

tk.Button(root, text="Show Graph", command=show_graph,
          bg="#2196F3", fg="white", width=20).pack(pady=5)

# Status Label
label_status = tk.Label(root, text="", bg="#1e1e2f", fg="white")
label_status.pack(pady=10)

tk.Label(root, text="Made by You 🚀",
         bg="#1e1e2f", fg="gray").pack(side="bottom", pady=10)
root.mainloop()

def show_insight():
    df = pd.read_csv("data.csv", names=["Date", "Hours", "Subject", "Mood"])
    df["Hours"] = pd.to_numeric(df["Hours"], errors="coerce")
    df = df.dropna()

    avg = df["Hours"].mean()

    if avg >= 3:
        result = "🔥 You are consistent! Keep it up!"
    else:
        result = "⚠️ Try to study more regularly."

    label_status.config(text=result, fg="yellow")

    tk.Button(root, text="Show Insight", command=show_insight,
          bg="#ff9800", fg="white", width=20).pack(pady=5)
    