from fastapi import FastAPI
from app.routes import user_route, post_route
from app.core.database import create_db

app = FastAPI()

app.include_router(user_route.router, prefix="/auth", tags=["Auth"])
app.include_router(post_route.router, prefix="/posts", tags=["Posts"])

@app.on_event("startup")
def startup():
    create_db()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Blog API"}