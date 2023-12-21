# Prompts are essential in guiding language models to generate relevant and coherent outputs. 
# They can range from simple instructions to complex few-shot examples. 
# In LangChain, handling prompts can be a very streamlined process, 
# thanks to several dedicated classes and functions.

# LangChain's PromptTemplate class is a versatile tool for creating string prompts. 
# It uses Python's str.format syntax, allowing for dynamic prompt generation. 
# You can define a template with placeholders and fill them with specific values as needed.

from langchain.prompts import PromptTemplate

# Simple prompt with placeholders
prompt_template = PromptTemplate.from_template(
    "Tell me a {adjective} joke about {content}."
)

# Filling placeholders to create a prompt
filled_prompt = prompt_template.format(adjective="funny", content="robots")
print(filled_prompt)