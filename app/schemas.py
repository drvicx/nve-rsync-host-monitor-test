from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MessageBase(BaseModel):
    text: str

class MessageCreate(MessageBase):
    pass

class MessageResponse(MessageBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class Config:
    from_attributes = True
