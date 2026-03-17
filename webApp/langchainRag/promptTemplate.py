from langchain.prompts import PromptTemplate


def createTemplate(template):
# template = """
# You are a real estate assistant.

# Use ONLY the provided context.

# If answer not found say:
# "Sorry, relevant property not found."

# Context:
# {context}

# User Question:
# {question}

# Answer in Hinglish.
# """

 prompt = PromptTemplate(
    template=template,
    input_variables=["context","question"]
 )
 print("printing.... for debug prompt = ", prompt)
 return prompt
