import os
from dotenv import load_dotenv
import requests

load_dotenv()




serviceUrl = os.getenv('serviceUrl')

def dispatchQuery(query:str) -> list:
    
    
    try:
        
      data = {
                 "text": query
             }

      response = requests.post(serviceUrl, json=data)
      embedding = response.json()["embedding"]
      # print(response.json())
      print('embedding =====   ' ,embedding)
      return embedding
    
    except :
        
        pass
        

