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

        prompt = "Generate me an image, only drawing lines with no solid elements, \
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

        print(prompt)

        generation_response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1024x1024",
            response_format="url",
        ) 
        print(response.data[0].url)


PROMPT = "A vaporwave computer"

generator = ImageGenerator()

generator.generate_image(PROMPT, "HIGH", "black, blue")
