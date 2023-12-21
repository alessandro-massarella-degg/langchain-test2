from langchain.output_parsers.json import SimpleJsonOutputParser
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

variables = __import__ ("variables")
# Initialize the language model
model = OpenAI(api_key=variables.openai_api_key, model_name="text-davinci-003", temperature=0.0)


# Create a JSON prompt
json_prompt = PromptTemplate.from_template(
    "Return a JSON object with `birthdate` and `birthplace` key that answers the following question: {question}"
)

# Initialize the JSON parser
json_parser = SimpleJsonOutputParser()

# Create a chain with the prompt, model, and parser
json_chain = json_prompt | model | json_parser

# Stream through the results
result_list = list(json_chain.stream({"question": "When and where was Elon Musk born?"}))

# The result is a list of JSON-like dictionaries
print(result_list)