from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

variables = __import__ ("variables")

# llm = OpenAI(api_key=openai_api_key, temperature=0.9)

llm1 = OpenAI(api_key=variables.openai_api_key, temperature=0.9)
llm2 = OpenAI(api_key=variables.openai_api_key, temperature=0.7)


# prompt = PromptTemplate(
#  input_variables=["product"],
#  template="Qual è un buon nome per un'azienda che produce {product}?",
# )

# chain = LLMChain(llm=llm, prompt=prompt)

chain = SequentialChain(
    chains={"llms": [llm1, llm2]},
    input_variables=["product"],
    prompt={"template": "Qual è un buon nome per un'azienda che produce {product}?"}
)
print(chain.run("scarpe"))  