import sqlite3
from qdrant_client import QdrantClient
from embeddingService import queryDispatcherService

DB_PATH = "C:\Users\shanU2\Desktop\renting.ai\rentals.db"

def getDescription(results):

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    try:
        yield conn
    finally:
        conn.close()
        
        
        
    
    cursor = conn.cursor()

    ids = [point.payload["ad_id"] for point in results.points if point.payload]

    placeholders = ",".join(["?"] * len(ids))

    query_sql = f"""
    SELECT *
    FROM rentals
    WHERE ad_id IN ({placeholders})
    """

    cursor.execute(query_sql, ids)

    rows = cursor.fetchall()

    results = [dict(row) for row in rows]

    r = []
    for i in results:
     r.append(i)
   
   
    return r