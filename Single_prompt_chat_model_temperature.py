from langchain_community.chat_models import ChatOllama

# Create a chat Ollama Model instance
model = ChatOllama(model = "llama3")

# Invoke the model with a prompt
response = model.invoke("Explain generative AI", temperature = 0.1)

# Print the result
print("Complete response: ", response)
print("Response Content: ", response.content)
