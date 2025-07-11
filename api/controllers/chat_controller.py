from models.chat_models import GetChat, SendMessage, ImageRequestModel
from typing import List, Annotated
from fastapi import UploadFile, File
from fastapi.responses import FileResponse, StreamingResponse
from svg.converter import Svg_converter
from svg.communicator import Svg_communicator
from chatgpt.images import ImageGenerator
from io import BytesIO
from PIL import Image
import httpx
import os

class ChatController:

    @classmethod
    def get_chats(cls, chat_id: GetChat) -> List[dict]:

        teste_retorno = {"chat_id": chat_id, "result": []}

        return teste_retorno

    # @classmethod
    # def get_chats(cls, chat_id: GetChat) -> List[dict]:
    #     teste_retorno = {"chat_id": chat_id, "result": []}
    #
    #     return teste_retorno

    @classmethod
    async def request_image(cls, image_request: ImageRequestModel):
        path = 'svg/maca.svg'
        generator = ImageGenerator()
        res = generator.generate_image(image_request.message, image_request.nivelDetalhe, ",".join(image_request.cores))
        async with httpx.AsyncClient() as client:
            response = await client.get(res)
            response.raise_for_status()

            image_bytes = BytesIO(response.content)

            return StreamingResponse(image_bytes, media_type="image/png")


    @classmethod
    async def send_to_cnc(cls, file: Annotated[UploadFile, File(...)], colors: str):
        original_filename_base = os.path.splitext(file.filename)[0]
        svg_output_filename = f"{original_filename_base}.svg"
        svg_output_path = os.path.join('output/', svg_output_filename)

        if file.content_type != 'image/svg+xml':
            try:
                image_bytes = await file.read()

                image_stream = BytesIO(image_bytes)

                try:
                    _ = Image.open(image_stream)
                    image_stream.seek(0)
                except Exception as e:
                    print(e)
            except Exception as e:
                raise e
            conversor = Svg_converter()
            path = 'arquivo.svg'

            try:
                conversor.convert(image_stream, svg_output_path, colors)
            except Exception as e:
                raise e
        communicator = Svg_communicator()

        print('comunicando')
        communicator.communicate(svg_output_path)
