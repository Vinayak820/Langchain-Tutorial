from langchain_openai import OpenAI
from dotenv import load_dotenv # It loads the secret keys from .env file in the current file.

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("What is the capital of India")
# invoke() is very important function in langchain.

print(result)

