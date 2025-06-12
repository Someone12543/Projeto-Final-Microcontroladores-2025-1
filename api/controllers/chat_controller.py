from models.chat_models import GetChat, SendMessage
from typing import List


class ChatController:

    @classmethod
    def get_chats(cls, chat_id: GetChat) -> List[dict]:

        teste_retorno = {"chat_id": chat_id, "result": "bruh"}

        return teste_retorno