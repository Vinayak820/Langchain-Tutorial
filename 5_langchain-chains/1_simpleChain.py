from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

template = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)
parser = StrOutputParser()
chain = template | model | parser
result = chain.invoke({'topic':'cricket'})
print(result)

chain.get_graph().print_ascii()
