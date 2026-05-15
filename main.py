from fastapi import FastAPI
from routes import base, prediction, health
from logger.logger import setup_logging


logger = setup_logging()


app = FastAPI()

logger.info(msg="App has started")


app.include_router(base.base_router)
app.include_router(prediction.predict_router)
app.include_router(health.health_router)


