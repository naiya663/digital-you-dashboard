import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

def save_data():
    hours = input("Enter study hours: ")
    subject = input("Enter subject: ")
    mood = input("Enter mood: ")

    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), hours, subject, mood])

    print("Data saved successfully ✅")

def analyze():
    df = pd.read_csv("data.csv", names=["Date", "Hours", "Subject", "Mood"])
    df["Hours"] = pd.to_numeric(df["Hours"], errors="coerce")
    df = df.dropna()

    print("\nTotal Study Hours:", df["Hours"].sum())
    print("\nSubject-wise Study:\n", df.groupby("Subject")["Hours"].sum())

def show_graph():
    df = pd.read_csv("data.csv", names=["Date", "Hours", "Subject", "Mood"])
    df["Hours"] = pd.to_numeric(df["Hours"], errors="coerce")
    df = df.dropna()

    df.groupby("Subject")["Hours"].sum().plot(kind="pie", autopct="%1.1f%%")
    plt.title("Study Distribution")
    plt.show()

# Run flow
save_data()
analyze()
show_graph()