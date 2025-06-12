from fastapi import APIRouter, Body, HTTPException
from models.chat_models import SendMessage, GetChat
from controllers.chat_controller import ChatController

api_chat = APIRouter(prefix="/api/chats")

@api_chat.get("/get")
async def get_chats(
        body: GetChat = Body(...)):
    try:
        response = ChatController.get_chats(body.chat_id)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

