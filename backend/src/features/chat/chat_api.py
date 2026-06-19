from fastapi import APIRouter
from pydantic import BaseModel
from openai import OpenAI

# Router for chat-related endpoints
chat_router = APIRouter()

# Initialize OpenAI client
client = OpenAI()

# Response model for the chat endpoint
class ChatResponse(BaseModel):
    message: str | None

@chat_router.post("/chat")
async def chat_endpoint(message: str) -> ChatResponse:
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": message}],
        )

        text = response.choices[0].message.content

        return ChatResponse(message=text)