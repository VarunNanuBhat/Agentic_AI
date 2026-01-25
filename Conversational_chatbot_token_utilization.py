from langchain_community.chat_models import ChatOllama
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
import tiktoken

# Create chat ollama model instance
model = ChatOllama(model = "llama3")

# Create list to store messages
messages = [
    SystemMessage(content = "Explain in simple terms")
]

# Initialize token encoding format
token_encode_format = tiktoken.get_encoding("cl100k_base")

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
    all_messages = " ".join([msg.content for msg in messages])
    print("All characters: ", all_messages)
    token_ids = token_encode_format.encode(all_messages)
    print("Tokens in above set of messages: ", token_ids)
    print("Token ID : Token text mapping: ")
    for token in token_ids: 
        text = token_encode_format.decode([token])
        print(token , ":" , text)
    total_tokens = len(token_ids)
    print("Tokens consumed to process all the messages: ", total_tokens)
    print("Type 'exit' to stop")
