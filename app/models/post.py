from sqlalchemy import Column, Integer, String, ForeignKey, TEXT
from app.core.database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(TEXT(1024 * 1024))
    user_id = Column(Integer, ForeignKey("users.id"))