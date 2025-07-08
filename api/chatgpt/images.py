'''
import openai
from dotenv import load_dotenv
import base64
import os

class ImageGenerator():
    def __init__(self):
        pass

    def generate_image(self, user_prompt, quality, colors):
        load_dotenv()

        openai.api_key = os.getenv("OPENAI_API_KEY")

        client = openai.OpenAI()
        
        
        le_prompt = "Generate me an image, only drawing lines with no solid elements, \
following the given structure, where 'Subject' is the main idea being drawn; \
'Detail' includes LOW, MEDIUM, and HIGH, where LOW is the minimum amount of \
detail to have it be identified as the subject, MEDIUM is a reasonable amount \
of detail, but not much, and HIGH is a little more detail than MEDIUM, making \
sure it's not too realistic; 'Colors' is the selection of colors to generate \
the image with, having the lines be colored where you believe the colors should go. \
Make sure to not fill in any elements when coloring, limiting the image to only lines. \
Make sure the lines are not too dense in general, no 2 color lines pass over \
eachother, and guarante any non-drawn part of the image is purely white.\n\
Subject: " + user_prompt + "\n\
Detail: " + quality + "\n\
Colors: " + colors + "\n"


        le_prompt = "Generate me an image of a vaporwave computer"

        generation_response = client.images.generate(
            model="dall-e-3",
            prompt=le_prompt,
            n=1,
            size="1024x1024",
            response_format="url",
        ) 
        print(response.data[0].url)


PROMPT = "A vaporwave computer"

generator = ImageGenerator()

generator.generate_image(PROMPT, "HIGH", "black, blue")
'''

from openai import OpenAI
from dotenv import load_dotenv
import os

class ImageGenerator:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def generate_image(self, user_prompt, quality, colors):

        # Esse é o texto final para depois que for garantido que a API funciona e a imagem é gerada.
        # É só tirar as aspas triplas antes e depois da linha de código e trocar o nome dentro da 'response'.

        le_prompt = "Generate me an image, only drawing lines with no solid elements, following the given structure, where 'Subject' is the main idea being drawn; 'Detail' includes LOW, MEDIUM, and HIGH, where LOW is the minimum amount of detail to have it be identified as the subject, MEDIUM is a reasonable amount of detail, but not much, and HIGH is a little more detail than MEDIUM, making sure it's not too realistic; 'Colors' is the selection of colors to generate the image with, having the lines be colored where you believe the colors should go. Make sure to not fill in any elements when coloring, limiting the image to only lines. Make sure the lines are not too dense in general, no 2 color lines pass over eachother, and guarante any non-drawn part of the image is purely white.\nSubject: " + user_prompt + "\n Detail: " + quality + "\nColors: " + colors + "\n"

        # teste = "A vaporwave computer"
        try:
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=le_prompt, # Trocar 'user_prompt' para 'le_prompt' quando funcionar.
                n=1,
                size="1024x1024",
                quality="standard",
                style="natural",
                response_format="url"
            )
            # response = self.client.images.generate(
            #     model="dall-e-3",
            #     prompt=teste,
            # )

            # Por enquanto, se a imagem for gerada corretamente, tudo que ele faz é
            # imprimir o url da imagem. Se quiser que eu resolva depois, me manda mensagem.
            # Mas se quiser resolver sozinho, é so pesquisar como converter url de imagem pra png.
            return response.data[0].url
        except Exception as e:
            print("Error:", e)

if __name__ == '__main__':
    PROMPT = "A red apple on a wooden table"
    generator = ImageGenerator()
    generator.generate_image(PROMPT, "HIGH", "black, blue")
    print('oi')

'''
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    models = client.models.list()
    for model in models:
        print(model.id)
except Exception as e:
    print("Auth test error:", e)
'''
