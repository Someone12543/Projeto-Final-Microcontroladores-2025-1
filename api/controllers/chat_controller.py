from models.chat_models import GetChat, SendMessage
from typing import List, Annotated
from fastapi import UploadFile, File
from svg.converter import Svg_converter
from svg.communicator import Svg_communicator
from io import BytesIO
from PIL import Image
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
    async def send_to_cnc(cls, file: Annotated[UploadFile, File(...)]):
        original_filename_base = os.path.splitext(file.filename)[0]
        svg_output_filename = f"{original_filename_base}_{os.urandom(4).hex()}.svg"
        svg_output_path = os.path.join('output/', svg_output_filename)

        try:
            # 1. LER o conteúdo do arquivo enviado NA MEMÓRIA
            image_bytes = await file.read()  # <-- CORREÇÃO: ADICIONAR AWAIT AQUI

            # 2. Criar um stream de bytes em memória para a PIL/Svg_converter
            image_stream = BytesIO(image_bytes)

            # 3. Opcional: Verificar se é uma imagem válida e resetar o stream
            try:
                # A PIL tenta abrir a imagem; se falhar, não é um formato reconhecido
                _ = Image.open(image_stream)
                image_stream.seek(0)
            except Exception as e:
                print(e)
        except Exception as e:
            pass
        conversor = Svg_converter()
        path = 'arquivo.svg'

        try:
            conversor.convert(image_stream, svg_output_path)
        except Exception as e:
            raise e
        communicator = Svg_communicator()

        print('comunicando')
        communicator.communicate(path)



