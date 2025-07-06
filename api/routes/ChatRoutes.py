from fastapi import APIRouter, Body, HTTPException, UploadFile, File
from models.chat_models import SendMessage, GetChat
from controllers.chat_controller import ChatController
from typing import Annotated


api_chat = APIRouter(prefix="/api/chats")

@api_chat.get("/get")
async def get_chats(
        body: GetChat = Body(...)):
    try:
        response = ChatController.get_chats(body.chat_id)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@api_chat.post("/send")
async def send_chat(file: Annotated[UploadFile, File(...)]):
    try:
        response = await ChatController.send_to_cnc(file)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))