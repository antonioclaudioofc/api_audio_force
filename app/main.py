from fastapi import FastAPI

from app.routers.router import router

app = FastAPI(
    title="API Audio Forge",
    description="Converte paylist do youtube em músicas",
    version="1.0.0"
)

app.include_router(router)