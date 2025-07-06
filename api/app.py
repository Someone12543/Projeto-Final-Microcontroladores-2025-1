from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.ChatRoutes import api_chat

app = FastAPI()

origins = [
    "*"  # This is the key: allows all origins
    # You could also list specific origins like:
    # "http://localhost",
    # "http://localhost:8000",
    # "http://localhost:3000", # Example for a React/Vue/Angular dev server
    # "https://your-frontend-domain.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True, # Allow cookies to be included in cross-origin requests
    allow_methods=["*"],    # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],    # Allow all headers in the request
)

app.include_router(api_chat)
