from fastapi import FastAPI
from features.middleware.security_cors import CORS_ORIGINS
from features.chat.chat_api import chat_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add the CORS middleware to your FastAPI application
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,          # Allows specified origins
    allow_credentials=True,         # Allows cookies and headers
    allow_methods=["*"],            # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],            # Allows all request headers
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Include routers
app.include_router(chat_router, prefix="/api")
