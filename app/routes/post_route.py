from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.auth import get_current_user
from app.schemas.post import PostCreate
from app.core.database import get_db
from app.services import post_service

router = APIRouter()

@router.post("/add")
def add_post(post: PostCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    if len(post.text.encode("utf-8")) > 1024 * 1024:
        raise HTTPException(status_code=400, detail="Payload too large")
    return post_service.add_post(db, post, user.id)

@router.get("/")
def get_posts(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return post_service.get_user_posts(db, user.id)

@router.delete("/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    success = post_service.delete_post(db, post_id, user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted"}