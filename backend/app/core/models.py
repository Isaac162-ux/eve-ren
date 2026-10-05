from datetime import datetime, timezone
from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=12000)
    conversation_id: str = "default"
class ChatResponse(BaseModel):
    response: str
    conversation_id: str
    provider: str
    model: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
class MemoryCreate(BaseModel):
    content: str = Field(min_length=1, max_length=10000)
    category: str = Field(default="general", max_length=80)
class MemoryItem(BaseModel):
    id: int
    content: str
    category: str
    created_at: str
class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    priority: int = Field(default=5, ge=1, le=10)
class PatchRequest(BaseModel):
    path: str = Field(min_length=1, max_length=240)
    content: str = Field(min_length=1, max_length=100000)
class PatchProposal(BaseModel):
    path: str
    summary: str
    content: str
    requires_approval: bool = True
