from fastapi import FastAPI
from routes.ChatRoutes import api_chat

app = FastAPI()

app.include_router(api_chat)
