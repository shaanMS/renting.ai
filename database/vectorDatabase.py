import numpy as np
import sqlite3
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

# --------------------------
# CONFIG
# --------------------------

EMBEDDING_PATH = r"C:\Users\shanU2\Desktop\renting.ai\data\rentals_embeddings.npy"
SQLITE_DB_PATH = r"C:\Users\shanU2\Desktop\renting.ai\rentals.db"
COLLECTION_NAME = "rentals"

# --------------------------
# 1️⃣ Load Embeddings
# --------------------------

embeddings = np.load(EMBEDDING_PATH)
vector_size = embeddings.shape[1]

print("Vector size:", vector_size)
print("Total vectors:", len(embeddings))

# --------------------------
# 2️⃣ Connect Qdrant
# --------------------------

client = QdrantClient(
    host="localhost",
    port=6333
)

# --------------------------
# 3️⃣ Create Collection
# --------------------------

client.recreate_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=VectorParams(
        size=vector_size,
        distance=Distance.COSINE
    )
)

print("✅ Collection ready")

# --------------------------
# 4️⃣ Get ad_ids from SQLite
# --------------------------

conn = sqlite3.connect(SQLITE_DB_PATH)
cursor = conn.cursor()

cursor.execute("SELECT ad_id FROM rentals ORDER BY rowid")
rows = cursor.fetchall()

conn.close()

ad_ids = [row[0] for row in rows]

print('===================================================',ad_ids,'  \n ======================================================')
assert len(ad_ids) == len(embeddings), "❌ Embedding and DB count mismatch"
print('********************************************')
# --------------------------
# 5️⃣ Prepare Points
# --------------------------

points = []

for idx, vector in enumerate(embeddings):
    points.append(
        PointStruct(
            id=idx,  # 🔥 not using real id without alphanum 
            # id=str(ad_ids[idx]), error arhi hai 
            vector=vector.tolist(),
            payload={
                "ad_id": ad_ids[idx]
            }
        )
    )

# --------------------------
# 6️⃣ Upload
# --------------------------

client.upsert(
    collection_name=COLLECTION_NAME,
    points=points
)

print("🚀 All embeddings uploaded successfully.")