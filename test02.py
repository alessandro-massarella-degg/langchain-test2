from langchain.llms import OpenAI

variables = __import__ ("variables")

llm = OpenAI(api_key=variables.openai_api_key)


# TEST01 SIMPLE RESPONSE
# response = llm.invoke("List the seven wonders of the world.")
# print(response)


# TEST02 STREAM METHOD
for chunk in llm.stream("List the seven wonders of the world."):
    print(chunk, end="", flush=True)
