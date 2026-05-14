from controllers import PredictController
from schemas import Features
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict_controller():
    features = Features(creditScore=549, geography="Spain", gender="Female", age=24, tenure=9, balance=0, numOfProducts=2, hasCrCard=1, isActiveMember=1, estimatedSalary=14406.41)
    pre_cont = PredictController()
    ret = pre_cont.predict(features)
    assert ret[0][1] - 0.06468354458866729 <= 0.0001

def test_predict_endpoint():
    response1 = client.post("/api/v1/predict", json={
        "creditScore": 549,
        "geography": "Spain",
        "gender": "Female",
        "age": 24,
        "tenure": 9,
        "balance": 0,
        "numOfProducts": 2,
        "hasCrCard": 1,
        "isActiveMember": 1,
        "estimatedSalary": 14406.41
    })

    response2 = client.post("/api/v1/predict", json={
        "creditScore": "inf",
        "geography": "Spain",
        "gender": "Female",
        "age": 24,
        "tenure": 9,
        "balance": 0,
        "numOfProducts": 2,
        "hasCrCard": 1,
        "isActiveMember": 1,
        "estimatedSalary": 14406.41
    })

    assert response1.status_code == 200
    assert "exit_prediction_proba" in response1.json()
    assert response2.status_code == 400
    
