# from qdrant_client import QdrantClient 
# import os
# from dotenv import load_dotenv
# from qdrant_client.models import VectorParams, Distance ,PointStruct
# import numpy as np




# load_dotenv()
# QDRANT_API_KEY = os.getenv("QDRANT_KEY")
# EMBEDDING_PATH = r"C:\Users\shanU2\Desktop\renting.ai\data\rentals_embeddings.npy"
# SQLITE_DB_PATH = r"C:\Users\shanU2\Desktop\renting.ai\rentals.db"
# COLLECTION_NAME = "rentals"




# client = QdrantClient(
#     url="https://0eeb9ef2-55a9-45fe-8bbd-d9b0c6bf83d8.europe-west3-0.gcp.cloud.qdrant.io",
#     api_key=QDRANT_API_KEY
# )

# print("Connected to Qdrant Cloud")



# client.create_collection(
#     collection_name="rentals",
#     vectors_config=VectorParams(
#         size=768,
#         distance=Distance.COSINE
#     )
# )

# print("Collection created")


# embeddings = np.load(EMBEDDING_PATH)
# vector_size = embeddings.shape[1]


# print("Vector size:", vector_size)
# print("Total vectors:", len(embeddings))


# conn = sqlite3.connect(SQLITE_DB_PATH)
# cursor = conn.cursor()

# points = []
# cursor.execute("SELECT ad_id FROM rentals ORDER BY rowid")
# rows = cursor.fetchall()
# conn.close()
# ad_ids = [row[0] for row in rows]

# print('===================================================',ad_ids,'  \n ======================================================')
# assert len(ad_ids) == len(embeddings), "❌ Embedding and DB count mismatch"
# print('********************************************')
# # --------------------------
# # 5️⃣ Prepare Points
# # --------------------------

# for i, vector in enumerate(embeddings):
#     points.append(
#         PointStruct(
#             id=i,
#             vector=vector.tolist(),
#             payload={"ad_id": i}
#         )
#     )






# client.upsert(
#     collection_name=COLLECTION_NAME,
#     points=points
# )

# print("🚀 All embeddings uploaded successfully.")































import os
import sqlite3
import numpy as np
from dotenv import load_dotenv

from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

# -----------------------------
# ENV LOAD
# -----------------------------

load_dotenv()

QDRANT_API_KEY = os.getenv("QDRANT_KEY")

QDRANT_URL = "https://0eeb9ef2-55a9-45fe-8bbd-d9b0c6bf83d8.europe-west3-0.gcp.cloud.qdrant.io"

EMBEDDING_PATH = r"C:\Users\shanU2\Desktop\renting.ai\data\rentals_embeddings.npy"
SQLITE_DB_PATH = r"C:\Users\shanU2\Desktop\renting.ai\rentals.db"

COLLECTION_NAME = "rentals"


# -----------------------------
# CLIENT INIT
# -----------------------------

client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
    check_compatibility=False
)


# -----------------------------
# SERVICE FUNCTION
# -----------------------------

async def upload_embeddings_service():

    print("🔌 Connected to Qdrant Cloud")

    # -----------------------------
    # Load embeddings
    # -----------------------------

    embeddings = np.load(EMBEDDING_PATH)

    vector_size = embeddings.shape[1]

    print("Vector size:", vector_size)
    print("Total vectors:", len(embeddings))

    # -----------------------------
    # Check collection exists
    # -----------------------------

    collections = client.get_collections().collections
    collection_names = [c.name for c in collections]

    if COLLECTION_NAME not in collection_names:

        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE
            )
        )

        print("✅ Collection created")

    else:

        print("⚡ Collection already exists, skipping creation")


    # -----------------------------
    # Load DB ids
    # -----------------------------

    conn = sqlite3.connect(SQLITE_DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT ad_id FROM rentals ORDER BY rowid")

    rows = cursor.fetchall()

    conn.close()

    ad_ids = [row[0] for row in rows]

    assert len(ad_ids) == len(embeddings), "❌ DB and embedding mismatch"


    # -----------------------------
    # Prepare points
    # -----------------------------

    points = []

    for i, vector in enumerate(embeddings):

        points.append(

            PointStruct(
                id=i,
                vector=vector.tolist(),
                payload={
                    "ad_id": ad_ids[i]
                }
            )

        )


    # -----------------------------
    # Batch Upload
    # -----------------------------

    batch_size = 100

    print("🚀 Uploading vectors...")

    for i in range(0, len(points), batch_size):

        batch = points[i:i + batch_size]

        client.upsert(
            collection_name=COLLECTION_NAME,
            points=batch
        )

        print(f"Uploaded {i + len(batch)} / {len(points)}")


    print("🎉 All embeddings uploaded successfully")
    
    
    
    
    
import asyncio

if __name__ == "__main__":
    asyncio.run(upload_embeddings_service())