from fastapi import FastAPI, APIRouter
from logger.logger import setup_logging

logger = setup_logging()

base_router = APIRouter(prefix="/api/v1", tags=["api_v1"])

@base_router.get("/")
def home():
    
    logger.info(msg="User has sent a request on / endpoint")
    app_name = "Churn Prediction"
    app_version = "0.0.1"

    return {
        "app_name": app_name,
        "app_version": app_version
    }

