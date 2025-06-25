import pandas as pd
import matplotlib.pyplot as plt

# Load usernames from CSV
df = pd.read_csv("data/usernames.csv")

# Suspicious keyword list
suspicious_keywords = [
    "free", "cash", "win", "hack", "bot", "click", "scam", "tool", "money", "xxx"
]

# Flag usernames based on keywords
def is_suspicious(username):
    username = username.lower()
    return any(word in username for word in suspicious_keywords)

# Apply the function
df["is_suspicious"] = df["username"].apply(is_suspicious)

# Print suspicious accounts
print("\nSuspicious Usernames:")
print(df[df["is_suspicious"] == True])

# Plot Safe vs Suspicious
counts = df["is_suspicious"].value_counts()
plt.bar(["Safe", "Suspicious"], counts)
plt.title("Username Safety Distribution")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()
