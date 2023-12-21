# LangChain's integration with chat models, a specialized variation of language models, 
# is essential for creating interactive chat applications. While they utilize language models internally, 
# chat models present a distinct interface centered around chat messages as inputs and outputs.
from langchain.chat_models import ChatOpenAI
variables = __import__ ("variables")

chat = ChatOpenAI(api_key=variables.openai_api_key)


# Chat models in LangChain work with different message types such as AIMessage, HumanMessage, 
# SystemMessage, FunctionMessage, and ChatMessage 
# (with an arbitrary role parameter). Generally, HumanMessage, AIMessage, and SystemMessage 
# are the most frequently used.
from langchain.schema.messages import HumanMessage, SystemMessage
messages = [
    SystemMessage(content="You are Micheal Jordan."),
    HumanMessage(content="Which shoe manufacturer are you associated with?"),
]
response = chat.invoke(messages)
print(response.content)