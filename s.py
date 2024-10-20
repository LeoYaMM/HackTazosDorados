from PIL import Image
import base64
import os
from groq import Groq
from langchain_groq import ChatGroq
from io import BytesIO
from langchain.document_loaders.image import UnstructuredImageLoader

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

image = Image.open("Images/Edu.jpg") # Abrir imagen
image = image.resize((image.width // 4, image.height // 4))  # Redimensionar la imagen

# Guardar la imagen comprimida
buffered = BytesIO()
image.save(buffered, format="JPEG", quality=30)  # Reducir la calidad a 30%
image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')


messages = [
    ("system", "Saca la CURP de una imagen"),
    ("human", image_base64)  # Enviar la imagen codificada en base64
]
# # Convertir la imagen a base64 para enviarla
# with open("Images/Edu.jpg", "rb") as image_file:
#     image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

# messages = [
#     {"role": "system", "content": "Eres un asistente, vas a sacar la CURP de una imagen."},
#     {"role": "user", "content": "Aquí está la imagen:"},
#     {"role": "user", "content": image}  # Pasar la imagen como un string de base64
# ]



print(response)

# text_msg =  = [
#     (
#         "system",
#         "Eres un asistente. vas a sacar la CURP de tu usuario"
#     )
#     ("human", {"text": ai_msg.content}) 
# ]


