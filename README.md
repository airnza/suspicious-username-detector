# 🚨 Suspicious Username Detector

This project is a lightweight Trust & Safety tool that identifies potentially malicious or spammy usernames using simple rule-based keyword matching.

It simulates a platform's username data and flags accounts likely to be bots, spammers, or abusers based on common patterns (e.g. names like `freecash2024`, `clickherefast`, `scamalert999`).

## 🔍 What It Detects

The script flags usernames that contain any of the following keywords:

free, cash, win, hack, bot, click, scam, tool, money, xxx


These are often used by automated bots or bad actors trying to impersonate, scam, or spam.

## 🧠 Why This Matters (Trust & Safety Use Case)

Trust & Safety teams often need to:
- Detect fake accounts
- Prevent spam and scams
- Automatically flag suspicious patterns

This project is a starting point for such pipelines and can evolve into ML-based detection later.

## 🧾 Dataset

The file `data/usernames.csv` contains sample usernames:

username,
admin123,
user_456,
freecash2025,
xxhacktoolxx,
normal_user,
win_big_now,
botuser2025,
realperson,
clickherefast,
scamalert999,
random_user


## 🧪 How It Works

The script:
1. Loads usernames from a `.csv` file
2. Applies rule-based matching against suspicious keywords
3. Flags usernames as `suspicious` or `safe`
4. Prints flagged results
5. Visualizes safe vs. suspicious distribution in a bar chart


## ⚙️ Installation & Usage

### Requirements

- Python 3.9+
- pandas
- matplotlib

### Setup

```bash
git clone https://github.com/airnza/suspicious-username-detector.git
cd suspicious-username-detector
pip install -r requirements.txt
python suspicious_usernames.py

