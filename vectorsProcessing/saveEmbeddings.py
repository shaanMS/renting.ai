# from qdrant_client import QdrantClient
# from qdrant_client import QdrantClient
# from qdrant_client.models import VectorParams, Distance
# from qdrant_client.models import PointStruct
# import json



# client = QdrantClient("http://localhost:6333")

# # print("Connected:", client.get_collections())   # checking collections
# # client.delete_collection("my_collection")




# with open(r"C:\Users\shanU2\Desktop\renting.ai\dataGeneration\embeddings_with_text3.jsonl", "r", encoding="utf-8") as f:
#     first_line = f.readline()
#     data = json.loads(first_line)

# print("Embedding size:", len(data["embedding"]))





# print(len(data["embedding"]))





from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
import json

# Connect
client = QdrantClient("http://localhost:6333")

# Recreate collection (safe reset)
client.recreate_collection(
    collection_name="properties",
    vectors_config=VectorParams(
        size=768,
        distance=Distance.COSINE
    )
)

print("Collection ready")

BATCH_SIZE = 100
points = []

with open(r"C:\Users\shanU2\Desktop\renting.ai\dataGeneration\embeddings_with_text3.jsonl", "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        data = json.loads(line)

        points.append(
            PointStruct(
                id=int(data["chunk_id"]),
                vector=data["embedding"],
                payload={
                    "parent_id": data["parent_id"],
                    "text": data["text"]
                }
            )
        )

        if len(points) >= BATCH_SIZE:
            client.upsert(
                collection_name="properties",
                points=points
            )
            print(f"Uploaded batch till index {i}")
            points = []

    # last batch
    if points:
        client.upsert(
            collection_name="properties",
            points=points
        )

print("✅ All embeddings stored successfully")