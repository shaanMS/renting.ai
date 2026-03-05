import pandas as pd
import json
from pathlib import Path


df = pd.read_csv(r'C:\Users\shanU2\Desktop\renting.ai\data\Rentals1.csv')
def create_search_text(row):
   
    return f"""{row['property_type']} for {row['purpose']} in {row['area_name']}, {row['city']}. {row['bedrooms']} bedrooms, {row['bathrooms']} bathrooms.Rent {row['monthly_rent']} rupees. Furnishing: {row['furnishing_status']}.Facing: {row['facing']}.Amenities: {row['amenities']}.Description: {row['description']}
    """

df["search_text"] = df.apply(create_search_text, axis=1)


df.to_csv(r'C:\Users\shanU2\Desktop\renting.ai\data\Rentals1.csv', index=False)

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Convert a CSV file into a JSON file.

    Parameters:
    ----------
    csv_path : str
        Full path to input CSV file.
    json_path : str
        Full path where JSON file will be saved.

    Returns:
    -------
    None
        Saves JSON file to given location.
    """

    try:
        # Load CSV
        df = pd.read_csv(csv_path)

        # Convert to JSON records format
        records = df.to_dict(orient="records")

        # Save JSON
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(records, f, indent=4, ensure_ascii=False)

        print(f"✅ Successfully converted CSV to JSON → {json_path}")

    except Exception as e:
        print(f"❌ Error: {e}")
        
        


csv_to_json(r'C:\Users\shanU2\Desktop\renting.ai\data\Rentals1.csv',r'C:\Users\shanU2\Desktop\renting.ai\data\Rentals.json')