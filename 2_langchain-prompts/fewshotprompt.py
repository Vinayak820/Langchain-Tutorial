from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

# -------------------------
# STEP 1: Few-shot examples
# -------------------------
examples = [
    {
        "input": "I was charged twice for my subscription this month.",
        "output": "Billing Issue"
    },
    {
        "input": "The app crashes every time I try to log in.",
        "output": "Technical Problem"
    },
    {
        "input": "Can you explain how to upgrade my plan?",
        "output": "General Inquiry"
    },
    {
        "input": "I need a refund for a payment I didn’t authorize.",
        "output": "Billing Issue"
    }
]

# --------------------------------------
# STEP 2: Template for each example pair
# --------------------------------------
example_template = """
Ticket: {input}
Category: {output}
"""

example_prompt = PromptTemplate(
    template=example_template,
    input_variables=["input", "output"]
)

# -------------------------------------------------------
# STEP 3: Build the FewShotPromptTemplate (main prompt)
# -------------------------------------------------------
few_shot_prompt = FewShotPromptTemplate(
    example_prompt=example_prompt,
    prefix="Classify the following customer support tickets into one of the categories: 'Billing Issue', 'Technical Problem', or 'General Inquiry'.\n\nExamples:\n",
    examples=examples,
    suffix="\nTicket: {user_input}\nCategory:",
    input_variables=["user_input"]
)

# -------------------------
# STEP 4: Format the prompt
# -------------------------
final_prompt = few_shot_prompt.format(
    user_input="My app keeps freezing when I open the dashboard."
)

print(final_prompt)
