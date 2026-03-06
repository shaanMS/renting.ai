

import requests

serviceUrl = "https://shaanSidd-embedder.hf.space/embed"

def dispatchQuery(query:str) -> list:
    
    
    try:
        
      data = {
                 "text": query
             }

      response = requests.post(serviceUrl, json=data)

      print(response.json())
      
      return response.json
    
    except :
        
        pass
        

