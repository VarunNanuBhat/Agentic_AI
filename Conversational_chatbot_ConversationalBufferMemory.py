from langchain_community.chat_models import ChatOllama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import tiktoken

# Create chat ollama model instance
model = ChatOllama(model = "llama3")

# Initialize conversationBufferMemory
memory = ConversationBufferMemory(
    memory_key = "history",             # stores the conversation
    return_messages = True                   # keeps messages as HumanMessage/AIMessage objects
)

# Create ConversationChain with memory
conversation = ConversationChain (
    llm = model, 
    memory = memory
)

while True: 
    user_prompt = input("User prompt: ")
    if user_prompt == "exit": 
        break
    response = conversation.run(user_prompt)
    print("Chatbot response: ", response)
