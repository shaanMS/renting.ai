import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains import LLMChain

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192",  # fast + cheap
    temperature=0.2,              # controlled output
    max_tokens=100                 # minimal generation
)

chain = LLMChain(
    llm=llm,
    prompt=prompt
)