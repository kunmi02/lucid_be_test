from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post import PostCreate
from typing import List

POST_CACHE = {}


def add_post(db: Session, post: PostCreate, user_id: int):
    new_post = Post(text=post.text, user_id=user_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    POST_CACHE.pop(user_id, None)  # Invalidate cache
    return new_post

def get_user_posts(db: Session, user_id: int):
    from datetime import datetime, timedelta
    import time

    cache_entry = POST_CACHE.get(user_id)
    now = time.time()
    if cache_entry and now - cache_entry["time"] < 300:
        return cache_entry["posts"]
    posts = db.query(Post).filter(Post.user_id == user_id).all()
    POST_CACHE[user_id] = {"posts": posts, "time": now}
    return posts

def delete_post(db: Session, post_id: int, user_id: int):
    post = db.query(Post).filter(Post.id == post_id, Post.user_id == user_id).first()
    if post:
        db.delete(post)
        db.commit()
        POST_CACHE.pop(user_id, None)
        return True
    return False
    