from PIL import Image
import base64
import os
from groq import Groq
from langchain_groq import ChatGroq


os.environ["GROQ_API_KEY"] = "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"

# Luego crear el cliente
client = Groq(
    api_key=os.environ["GROQ_API_KEY"]
)

# Parametros
llm_text = ChatGroq(
    model="llama3-8b-8192",
    temperature = 0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

llm_vision = ChatGroq(
    model="llama-3.2-90b-vision-preview",
    temperature = 0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

image = Image.open("Images/Edu.jpg") # Abrir ese pedo

# Convertir la imagen a base64 para enviarla
with open("Images/Edu.jpg", "rb") as image_file:
    image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

messages = [
    (
        "system",
        "Eres un asistente, vas a sacar la CURP de una imagen",
    ),
    ("human", image_raw_data),
]
ai_msg = llm_vision.invoke(messages)

print(ai_msg.content)


message_image = [

]

