from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage
import base64

# Load vision-capable model
model = ChatOllama(model="bakllava")

# Load image and convert to base64
def load_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

image_base64 = load_image("texts.jpg")  # replace with your image path

while True:
    question = input("Ask a question about the image (or type exit): ")
    if question == "exit":
        break

    message = HumanMessage(
        content=[
            {"type": "text", "text": question},
            {
                "type": "image_url",
                "image_url": f"data:image/jpeg;base64,{image_base64}"
            }
        ]
    )

    response = model.invoke([message])
    print("AI response:", response.content)
