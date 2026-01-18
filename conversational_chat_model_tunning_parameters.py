from langchain_community.chat_models import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# Create a chatOllama Model instance
model = ChatOllama(model="llama3")
messages = [
    SystemMessage(content = "Explain in simple terms"),
]
while True: 
    user_prompt = input("User prompt: ")
    if user_prompt == "exit":
        break
    messages.append(HumanMessage(content = user_prompt))
    response = model.invoke(messages, temperature = 0.7, top_k = 50, top_p = 0.7)
    messages.append(AIMessage(content = response.content))
    print("Chatbot: ", response.content)
    print("Chat history: ")
    print(messages)
    print("Type 'exit' to stop")