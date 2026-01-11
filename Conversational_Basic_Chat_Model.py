from langchain_community.chat_models import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# Create an Ollama chat Model instance
model = ChatOllama(model = "llama3")

messages = [
    SystemMessage(content = "Explain in simple terms"),
]

while True: 
    user_prompt = input("User prompt: ")
    if user_prompt == "exit":
        break
    messages.append(HumanMessage(content = user_prompt))
    response = model.invoke(messages)
    messages.append(AIMessage(content = response.content))
    print("Chatbot response: ",response.content)
    print("Chat history: ")
    print(messages)
    print("Type 'exit' to stop")