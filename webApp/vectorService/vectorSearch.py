from qdrant_client import QdrantClient
from embeddingService import queryDispatcherService


def searchInVector(embedding:list):
    

 client = QdrantClient(
    url="http://localhost:6333"
    )
 
 
 results = client.query_points(
    collection_name="rentals",
    query=embedding,
    limit=5
   )
 
 
 
 
 
 
 return results
