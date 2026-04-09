from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a expert {profession}"),
    ("user", "Tell me abount {topic} in brief"),
])

result = prompt.format_messages(profession="Doctor", topic="Kidney Stone")

print(result)



#-------------------------------------------------------
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("user", "Tell me about {topic} in brief")
])

result = prompt.format_messages(
    topic="Kidney Stone"
)

print(result)


#------------------------------------------------------
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

examples = [
    {"input" : "Student has only two months left for the board exam", "output":"class 10"},
    {"input" : "Student has only two years left from getting passed out from school", "output":"class 10"},
    {"input" : "Student has only 1 month left to be ", "output":"class 12"},
    {"input" : "Student has only four months left for the board exam", "output":"class 6"}
]

example_template = """
Ticket:{input}
Category:{output}
"""
example_prompt = PromptTemplate(
    template=example_template,
    input_variables=["input", "output"]
)

fewPrompt = FewShotPromptTemplate(
    example_template=example_template,
    prefix="\nClassify the flowwing",
    examples=examples,
    suffix="\nTicket:{input}\n Category:",
    input_variables=["input"]
)

prompt = fewPrompt.format(input="")