from pydantic import BaseModel

class PostCreate(BaseModel):
    text: str

class PostOut(PostCreate):
    id: int
    