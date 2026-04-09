from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)


#--------------------------------------------------------------
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import SystemMessage, HumanMessage

# chat_template = ChatPromptTemplate([
#     SystemMessage(content='You are a helpful {domain} expert'),
#     HumanMessage(content='Explain in simple terms, what is {topic}')
# ])

# prompt = chat_template.invoke({'domain' : 'Cricket', 'topic' : 'dusra'})

# print(prompt)


# Output: Problem it doesn't get filled.
# PS C:\Users\vinnu\OneDrive\Desktop\langchain-prompts> python chat_prompt_template.py
# messages=[SystemMessage(content='You are a helpful {domain} expert', additional_kwargs={}, response_metadata={}), 
# HumanMessage(content='Explain in simple terms, what is {topic}', additional_kwargs={}, response_metadata={})]

# Note : Its weird because PromptTemplate works. Solution : Send tuples.

