from fastapi import FastAPI, APIRouter


health_router = APIRouter(prefix="/api/v1", tags=["api_v1"])

@health_router.get("/health")
def health():
    
    
    return {
        "status": "I'm Alive Broski"
    }
