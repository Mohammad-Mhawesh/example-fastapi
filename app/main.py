from fastapi import FastAPI
from .database import engine
from . import models
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# only needed when not using alembic (using SQLALCHEMY)
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()
# update to match the web app's domain only
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello World"}
