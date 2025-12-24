from langchain_community.chat_models import ChatOllama

# Create a chat Ollama Model
model = ChatOllama(model = "llama3")

# Invoke the model with a prompt
result = model.invoke("Which continent does India belog too")
print("Result:")
print(result)
print("Content")
print(result.content)
