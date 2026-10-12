from fastapi import FastAPI

from src.backend.api.routes import router 

app = FastAPI(
    title= "AugurHealth Prediction App",
    version="1.0.0",
    description="Multi-disease prediciton backend"
)

app.include_router(router, prefix="/api")
