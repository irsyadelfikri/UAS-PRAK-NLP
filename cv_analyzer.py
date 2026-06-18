from dotenv import load_dotenv

load_dotenv()

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langsmith import traceable

llm = ChatOllama(
    model="gemma3:4b",
    temperature=0
)

parser = StrOutputParser()


@traceable
def analyze_cv(template, data):
    prompt = PromptTemplate.from_template(template)

    chain = (
        prompt
        | llm
        | parser
    )

    result = chain.invoke(data)

    return result