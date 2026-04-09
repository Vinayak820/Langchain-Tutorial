# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatOpenAI()

# messages=[
#     SystemMessage(content='You are a helpful assistant'),
#     HumanMessage(content='Tell me about LangChain')
# ]

# result = model.invoke(messages)

# messages.append(AIMessage(content=result.content))

# print(messages)



#---------------------------------------------------------------
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1", 
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)