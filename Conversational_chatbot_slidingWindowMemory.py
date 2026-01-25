from langchain_community.chat_models import ChatOllama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
import tiktoken

# Create Ollama chat model instance
model = ChatOllama(model = "llama3")

# Initialize Sliding window memory to keep last 4 messages
memory = ConversationBufferWindowMemory(
    k = 4, 
    memory_key = "history",
    return_messages = True
)

# Create conversation chain with sliding window memory
conversation = ConversationChain(
    llm = model, 
    memory = memory 
)

# Initialize token encoding format
token_encode_format = tiktoken.get_encoding("cl100k_base")

while True: 
    user_prompt = input("User prompt: ")
    if user_prompt == "exit": 
        break
    response = conversation.run(user_prompt)
    print("Chatbot response: ", response)
    print("Chat History: ")
    for msg in memory.chat_memory.messages:
        print(msg)
    all_messages = " ".join([msg.content for msg in memory.chat_memory.messages])
    token_ids = token_encode_format.encode(all_messages)
    total_tokens = len(token_ids)
    print("All characters in chat history:", all_messages)
    print("Tokens in above messages:", token_ids)
    print("Token ID : Token text mapping:")
    for token in token_ids:
        text = token_encode_format.decode([token])
        print(token, ":", text)
    print("Total tokens consumed:", total_tokens)