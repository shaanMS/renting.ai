import sqlite3
import pandas as pd

# 1️⃣ Load CSV
csv_path = r"C:\Users\shanU2\Desktop\renting.ai\data\Rentals1.csv"
df = pd.read_csv(csv_path)

# 2️⃣ Connect SQLite
conn = sqlite3.connect("rentals.db")
cursor = conn.cursor()
print()
# 3️⃣ Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS rentals (
    ad_id TEXT PRIMARY KEY,
    property_type TEXT,
    purpose TEXT,
    furnishing_status TEXT,
    area_name TEXT,
    landmark TEXT,
    street_address TEXT,
    city TEXT,
    district TEXT,
    state TEXT,
    pincode TEXT,
    bedrooms INTEGER,
    bathrooms INTEGER,
    balconies INTEGER,
    super_builtup_area_sqft INTEGER,
    carpet_area_sqft INTEGER,
    floor_number INTEGER,
    total_floors INTEGER,
    availability_status TEXT,
    age_of_property TEXT,
    monthly_rent INTEGER,
    security_deposit INTEGER,
    maintenance_charges INTEGER,
    preferred_tenants TEXT,
    facing TEXT,
    amenities TEXT,
    car_parking TEXT,
    bachelors_allowed TEXT,
    non_veg_allowed TEXT,
    gated_security TEXT,
    power_backup TEXT,
    lift TEXT,
    description TEXT,
    posted_date TEXT,
    contact_person TEXT,
    contact_number TEXT,
    views INTEGER,
    status TEXT,
    search_text TEXT
);
""")

# 4️⃣ Insert Data
df.to_sql("rentals", conn, if_exists="append", index=False)

conn.commit()
conn.close()

print("✅ CSV imported successfully into SQLite.")