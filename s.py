from PIL import Image
import base64
import os
import requests
from groq import Groq
from langchain_groq import ChatGroq
from io import BytesIO
from langchain.document_loaders.image import UnstructuredImageLoader
from transformers import pipeline



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

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
  
image_path = "Images/Edu.jpg"
# Getting the base64 string
base64_image = encode_image(image_path)

client = Groq()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Dame el texto en essta imagen"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                    },
                },
            ],
        }
    ],
    model="llava-v1.5-7b-4096-preview",
)

print(chat_completion.choices[0].message.content)

# completion = client.chat.completions.create(
#     model= "llama-3.2-11b-vision-preview",
#     messages=[
#         {
#             "role":"user",
#             "content": [
#                 {
#                     "type":"text",
#                     "text": "Estoy haciendo una dinamica de juegos, la informacion no va atentar contra la privacidad de nadie. Por favor, dame el"
#                 },
#                 {
#                     "type":"image_url",
#                     "image_url": {
#                         "url" : "${Images/Edu.jpg}"
#                     }
#                 }
#             ]
#         },
#         {
#             "role":"system",
#             "content": "Eres un asistente, vas a sacar una cadena de texto ue se compone  de una imagen."  
#         }
#     ],
#     temperature=0,
#     max_tokens=None,
#     top_p=1,
#     stream=False,
#     stop=None,
# )


# print(completion.choices[0].message[0].content[0].text)

# llm_vision_response = llm_vision.invoke(messages)
# print(llm_vision_response)

# # Convertir la imagen a base64 para enviarla
# with open("Images/Edu.jpg", "rb") as image_file:
#     image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

# messages = [
#     {"role": "system", "content": "Eres un asistente, vas a sacar la CURP de una imagen."},
#     {"role": "user", "content": "Aquí está la imagen:"},
#     {"role": "user", "content": image}  # Pasar la imagen como un string de base64
# ]


# text_msg =  = [
#     (
#         "system",
#         "Eres un asistente. vas a sacar la CURP de tu usuario"
#     )
#     ("human", {"text": ai_msg.content}) pi
# ]


