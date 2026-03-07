import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient

load_dotenv()

QDRANT_URL = "https://0eeb9ef2-55a9-45fe-8bbd-d9b0c6bf83d8.europe-west3-0.gcp.cloud.qdrant.io"
QDRANT_API_KEY = os.getenv("QDRANT_KEY")

COLLECTION_NAME = "rentals"

# client reuse (important for performance)
client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
    check_compatibility=False
)


async def searchInVector(embedding: list, limit: int = 5):

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=embedding,
        limit=limit
    )

    ad_ids = []
    print(type(results))
    print(results)
    print(type(results[0]))
    print(results[0])
    for point,score in results:  
        
        ad_ids.append(point.payload["ad_id"])
         
    return ad_ids         