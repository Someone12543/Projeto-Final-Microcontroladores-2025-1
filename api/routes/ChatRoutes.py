from fastapi import APIRouter, Body, HTTPException, UploadFile, File, Form
from models.chat_models import SendMessage, GetChat, ImageRequestModel, SendToCNCModel
from controllers.chat_controller import ChatController
from typing import Annotated, List
from fastapi.responses import FileResponse


api_chat = APIRouter(prefix="/api/chats")

@api_chat.get("/get")
async def get_chats(
        body: GetChat = Body(...)):
    try:
        response = ChatController.get_chats(body.chat_id)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@api_chat.post("/request-image")
async def request_image(body: ImageRequestModel = Body(...)):
    try:
        response = await ChatController.request_image(body)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@api_chat.post("/send")
async def send_chat( colors: str = Form(...),file: UploadFile = File(...)):
    try:
        response = await ChatController.send_to_cnc(file, colors)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))