

import requests

serviceUrl = "https://shaanSidd-embedder.hf.space/embed"

async def dispatchQuery(query:str) -> list:
    
    
    try:
        
      data = {
                 "text": query
             }

      response = requests.post(serviceUrl, json=data)
      embedding = response.json()["embedding"]
      # print(response.json())
      
      return embedding
    
    except :
        
        pass
        

