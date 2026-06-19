from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from openai import OpenAI

# Router for chat-related endpoints
chat_router = APIRouter()

# Initialize OpenAI client
client = OpenAI()

# Request model for the chat endpoint
class ChatRequest(BaseModel):
    message: str


# Response model for the chat endpoint
class ChatResponse(BaseModel):
    message: str | None


@chat_router.post("/chat")
async def chat_endpoint(payload: ChatRequest) -> ChatResponse:
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": payload.message}],
        )
    except Exception as exc:
        raise HTTPException(status_code=502, detail="Failed to generate chat response") from exc

    text = response.choices[0].message.content

    return ChatResponse(message=text)