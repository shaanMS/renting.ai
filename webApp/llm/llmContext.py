
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from langchainRag.promptTemplate import createTemplate
from databases.database import getDescription
from embeddingService.queryDispatcherService import dispatchQuery
# from vectorService.vectorSearch import searchInVector 
from vectorService.vectorSearchService import searchInVector

#   local storage ka use karo frntend m , token ka or koi bhi python se use na kar paaye isliye apu hide karo to hi accha hai or 1 min ka throttle banao 


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def generateResponse(template, query):

  llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2
  )
  
# print(llm.invoke("hello"))
  
  
  # embeddings = dispatchQuery(query)
  
  # vectorResults = searchInVector(embeddings)
  
  
  # results = getDescription(vectorResults)
  
  # prompt = createTemplate(template)


  # 


  
  
  # 1️⃣ query embedding
  embeddings =  dispatchQuery(query)
  
    # 2️⃣ vector search
  vectorResults =  searchInVector(embeddings)

    # 3️⃣ database fetch
  results = getDescription(vectorResults)

    # 4️⃣ prompt
  prompt = createTemplate(template)

  chain = prompt | llm

  context = ""
   
  for r in results:
    context += f"""
  # Property ID: {r['ad_id']}
  Type: {r['property_type']}
  Purpose: {r['purpose']}
  City: {r['city']}
  Area: {r['area_name']}
  Bedrooms: {r['bedrooms']}
  Rent: {r['monthly_rent']}
  Description: {r['description']}
   ---------------------
  """

  print('\n\n\n\n  context    ',context)

  response = chain.invoke({
    "context": context,
    "question": query
    })

  return response.content