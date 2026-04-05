import sqlite3
import pandas as pd

# 1️⃣ Load CSV
csv_path = r"C:\Users\shanU2\Desktop\renting.ai\data\Rentals1.csv"
df = pd.read_csv(csv_path)

# 2️⃣ Connect SQLite
print()
print()
conn = sqlite3.connect("rentals.db")
cursor = conn.cursor()

cursor.execute("SELECT ad_id, monthly_rent FROM rentals;")
print(cursor.fetchall())
print()
conn.close()