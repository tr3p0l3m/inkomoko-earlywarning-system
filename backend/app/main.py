from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Production FastAPI")

app.include_router(router)
