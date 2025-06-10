from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# Configure the LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Chain-of-thought reasoning step
reason_prompt = PromptTemplate(
    input_variables=["question"],
    template=(
        "You are a helpful agent. "
        "Use step-by-step reasoning to solve the user's question.\n" 
        "Question: {question}"
    ),
)
reason_chain = LLMChain(llm=llm, prompt=reason_prompt, output_key="reason")

# Final answer step that reacts based on the reasoning
answer_prompt = PromptTemplate(
    input_variables=["reason"],
    template="Provide the final answer based on your reasoning:\n{reason}",
)
answer_chain = LLMChain(llm=llm, prompt=answer_prompt, output_key="answer")

# Combine the steps in a sequential chain
agent_chain = SequentialChain(
    chains=[reason_chain, answer_chain],
    input_variables=["question"],
    output_variables=["answer", "reason"],
)

def run_agent(question: str) -> dict:
    """Execute the LangChain agent with the given question."""
    return agent_chain({"question": question})
