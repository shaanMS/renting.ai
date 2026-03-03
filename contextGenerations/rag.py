from langchain.prompts import PromptTemplate

template = """
You are a concise assistant.
Answer in natural human tone.
Keep response under 50 words.
Question: {question}
Answer:
"""

prompt = PromptTemplate(
    input_variables=["question"],
    template=template
)