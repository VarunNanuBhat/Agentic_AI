from langchain_community.chat_models import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# Create an Ollama chat Model instance
model = ChatOllama(model = "llama3")

messages = [
    SystemMessage(content = "Explain in simple terms"),
    HumanMessage(content = "Which continent does India belong too"),  
    AIMessage(content = "India is part of the continent called Asia."),
    HumanMessage(content = "How many states does it have")
]

response = model.invoke(messages)
print(response.content)