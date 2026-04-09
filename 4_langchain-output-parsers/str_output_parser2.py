from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

template1 = PromptTemplate(
    template="Generate a Score Card of India vs Australia {Test} Match",
    input_variables=["Test"]
)


template2 = PromptTemplate(
    template="Who scored highest runs among both teams  & both innings from a score card {Score}",
    input_variables=["Score"]
)

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"Test" : "ICC Men Final Cricker World Cup 2023"})

print(result)

