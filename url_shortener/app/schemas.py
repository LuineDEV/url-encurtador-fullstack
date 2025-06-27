from pydantic import BaseModel, Field
from typing import Optional 

class URLBase(BaseModel):
    long_url: str

class URLCreate(URLBase):

    short_code: Optional[str] = Field(None, min_length=3, max_length=10)

class URL(URLBase):
    id: int
    short_code: str | None = None
    clicks: int

    class Config:
        from_attributes = True