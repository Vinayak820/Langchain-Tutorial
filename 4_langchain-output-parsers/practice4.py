from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv
load_dotenv() 

model = ChatOpenAI()

schema = [
    ResponseSchema(name="fact1", description="Fact 1 about teh topic"),
    ResponseSchema(name="fact2", description="Fact 2 about teh topic"),
    ResponseSchema(name="fact3", description="Fact 3 about teh topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give 5 facts about {topic} \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={'format_instruction' : parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic' : 'Black Hole'})

print(result)