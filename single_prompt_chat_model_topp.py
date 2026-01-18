from langchain_community.chat_models import ChatOllama


# Create a chat Ollama Model instance
model = ChatOllama(model = "llama3")

# Invoke the model with a prompt
response = model.invoke("Explain generative AI in one line", temperature = 0.7, top_k = 50, top_p = 0.7)

# print the response
print("Complete response: ", response)
print("Response content: ", response.content)