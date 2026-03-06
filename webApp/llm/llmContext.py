
import os
from langchain_groq import ChatGroq

# os.environ[] = ""



llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2
)

# print(llm.invoke("hello"))





chain = prompt | llm






context = ""

for r in results:
    context += f"""
Property ID: {r['ad_id']}
Type: {r['property_type']}
Purpose: {r['purpose']}
City: {r['city']}
Area: {r['area_name']}
Bedrooms: {r['bedrooms']}
Rent: {r['monthly_rent']}
Description: {r['description']}
---------------------
"""



response = chain.invoke({
    "context": context,
    "question": query
})

print(response.content)