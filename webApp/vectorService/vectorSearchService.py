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


def searchInVector(embedding: list, limit: int = 5):

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=embedding,
        limit=limit
    )

    # ad_ids = []
    # print(type(results.points))
    # print(results)
    # print('====   ',  results.points[0])
    # print('-------------   ',type(results.point[0]))
    # print(type(results[0]))
    # print(results[0])
    # for point in results.points:  
    
    #     # a d_ids.append(point.payload["ad_id"])
    #     ad_ids.append({
    #     "ad_id": point.payload["ad_id"],
    #     "score": point.score
    # })

    print(results)    
    return results        