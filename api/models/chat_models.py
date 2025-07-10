from pydantic import BaseModel
from typing import Optional, List, Annotated
from fastapi import UploadFile, File


class GetChat(BaseModel):
    id:str

class SendMessage(BaseModel):
    id: str
    message: str

class ChatModel(BaseModel):
    id: str
    chats: List[dict]

class ImageRequestModel(BaseModel):
    message: str
    nivelDetalhe: str
    cores: List[str]

class SendToCNCModel(BaseModel):
    colors: str
    file: Annotated[UploadFile, File(...)]