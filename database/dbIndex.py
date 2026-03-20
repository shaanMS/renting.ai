import sqlite3
import pandas as pd

print('')
conn = sqlite3.connect("rentals.db")
cursor = conn.cursor()

# Indexes for hybrid filtering
cursor.execute("CREATE INDEX IF NOT EXISTS idx_city ON rentals(city);")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_rent ON rentals(monthly_rent);")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_bedrooms ON rentals(bedrooms);")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_status ON rentals(status);")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_search_text ON rentals(search_text);")
conn.commit()
conn.close()

print("✅ Indexes created successfully.")
