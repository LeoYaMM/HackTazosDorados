
import io as io
import base64

from PIL import Image

# Lector de imágenes
def leer_imagen(image_path):
    image = Image.open(image_path)
    image.save('image.png', format='PNG')  # Guardar la imagen en un archivo .png
    with open('image.png', 'rb') as file:  # Leer el archivo .png como binario
        base64_text = base64.b64encode(file.read()).decode('utf-8')
    return base64_text

image_path = "Images/Edu.jpg"
base64_text = leer_imagen(image_path)

print(base64_text)