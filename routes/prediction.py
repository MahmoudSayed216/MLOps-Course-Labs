from fastapi import FastAPI, APIRouter, Request, status
from fastapi.responses import JSONResponse
from schemas import Features
from controllers import PredictController
from logger.logger import setup_logging


logger = setup_logging()

def validate(features: Features):
    val = lambda x: abs(x) == float("inf")

    floats = [val(x) for x in [features.balance, features.creditScore, features.tenure, features.numOfProducts, features.estimatedSalary]]
    return any(floats)


predict_router = APIRouter(prefix="/api/v1", tags=["api_v1"])

@predict_router.post("/predict")
def predict(request: Request, features: Features):
    
    # preprocessor = request.app.preprocessor
    # model = request.app.model
    if validate(features):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal" : 'request has infinite',
            }
        )

    logger.info("User has sent a request on /predict endpoint")
    logger.info(msg=f"User has sent a request with \n{features}")
    predict_controller = PredictController()
    proba = predict_controller.predict(features)
    logger.info(msg=f"model has predicted {proba}")
    
    return {
        "exit_prediction_proba": f"{proba[0][1]}",
        "status_code": 200
    }