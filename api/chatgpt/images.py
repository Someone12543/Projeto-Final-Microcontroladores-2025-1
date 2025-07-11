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

        #le_prompt = "Generate me an image, only drawing lines with no solid elements, following the given structure, where 'Subject' is the main idea being drawn; 'Detail' includes LOW, MEDIUM, and HIGH, where LOW is the minimum amount of detail to have it be identified as the subject, MEDIUM is a reasonable amount of detail, but not much, and HIGH is a little more detail than MEDIUM, making sure it's not too realistic; 'Colors' is the selection of colors to generate the image with, having the lines be colored where you believe the colors should go. Make sure to not fill in any elements when coloring, limiting the image to only lines. Make sure the lines are not too dense in general, no 2 color lines pass over eachother, and guarante any non-drawn part of the image is purely white. Make sure to use as little ink as possible to convey the general shape of the prompt\nSubject: " + user_prompt + "\n Detail: " + quality + "\nColors: " + colors + "\n"


        le_prompt = "Generate me an image following the given structure, where 'Subject' is the main idea being drawn \
and 'Detail' includes LOW, MEDIUM, and HIGH, where LOW is the minimum amount of detail to have it be \
identified as the subject, MEDIUM is a reasonable amount of detail, but not much, and HIGH is a little more \
detail than MEDIUM, making sure it's not too realistic. Always guarantee the image only has black lines, that they \
only exist if they are necessary details of the image, and to not draw them too close to each other too often. \
Ensure the lines are not too dense in general, that no 2 lines cross over eachother \
and that any non-drawn part of the image is purely white. Make \
sure to use as little ink as possible to convey the prompt. No drawing multiple lines \
over each other to reinforce them or make them appear thicker. DO NOT DRAW A SINGLE \
CONTINUOUS LINE.\n\
Subject: " + user_prompt + "\n\
Detail: " + quality + "\n"
        prompt = (
            f"Minimalist black line art of {user_prompt}, drawn with under 100 separate lines. "
            f"Avoid overlapping or looping lines. Use as little ink as possible. "
            "The drawing should be sparse, on a white background, without shading. "
            "Only include lines that are strictly necessary to recognize the subject. "
            f"No thickening or reinforcing lines, only making the drawing with {quality} level of detail."
            f"Use only lines of width of 2 pixels"
        )
#         le_prompt = f"Generate a minimalist black line drawing of the subject below. Use as few lines as possible, no more than 100 total. Lines should be thin, never overlapped or repeated. Only draw lines that are essential to identify the subject. Leave all other areas pure white. Avoid dense or closely packed lines. Do not add shading, textures, or extra stylistic elements. \
#             Subject: {user_prompt}\
#             Level of detail:  {quality}(but still minimalist)"


        # teste = "A vaporwave computer"
        # try:


        try:
            #     response = self.client.images.generate(
            #         model="gpt-4.1-mini",
            #         prompt=le_prompt, # Trocar 'user_prompt' para 'le_prompt' quando funcionar.
            #         n=1,
            #         size="1024x1024"
            #    )

            # response = self.client.responses.create(
            #     model="gpt-4.1-mini",
            #     input=le_prompt,
            #     tools=[{"type": "image_generation"}],
            # )

            # # Save the image to a file
            # image_data = [
            #     output.result
            #     for output in response.output
            #     if output.type == "image_generation_call"
            # ]
            # print('oioi')
            # if image_data:
            #     image_base64 = image_data[0]
            #     with open("image.png", "wb") as f:
            #         f.write(base64.b64decode(image_base64))

            # print('a')

            response = self.client.images.generate(
                model="dall-e-2",
                prompt=prompt, # Trocar 'user_prompt' para 'le_prompt' quando funcionar.
                n=1,
                size="1024x1024",
                response_format="url"
            )

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
