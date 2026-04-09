from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate(
    template="You are a expert {profession}. Tell me about {topic}",
    input_variables=["profession", "topic"]
)

result = prompt.invoke({"profession":"Doctor","topic":"USG"})

print(result.text)

