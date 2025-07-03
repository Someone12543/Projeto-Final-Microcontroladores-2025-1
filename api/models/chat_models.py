from pydantic import BaseModel
from typing import Optional, List


class GetChat(BaseModel):
    id:str

class SendMessage(BaseModel):
    id: str
    message: str

class ChatModel(BaseModel):
    id: str
    chats: List[dict]