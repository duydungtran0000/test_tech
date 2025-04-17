from fastapi import FastAPI
from app.routers import router as api_router

app = FastAPI(
    title="RPN Calculator API",
    version="1.0.0"
)

app.include_router(api_router)
