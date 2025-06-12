from pydantic import BaseModel


class GetChat(BaseModel):
    id:str

class SendMessage(BaseModel):
    id: str
    message: str