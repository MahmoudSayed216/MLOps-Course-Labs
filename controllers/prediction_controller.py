import joblib
import pickle
import os
from schemas import Features
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier


class PredictController:

    def __init__(self):
        self.base_dir = "ml"
        self.load_ml_assets()


    def load_ml_assets(self):
        preprocessor_path = os.path.join(self.base_dir, "column_transformer.joblib")
        model_path = os.path.join(self.base_dir, "model.pkl")
        
        self.preprocessor = joblib.load(preprocessor_path)

        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)
    

    def predict(self, features: Features):
        features = pd.DataFrame({
            'CreditScore': [features.creditScore],
            'Geography': [features.geography],
            'Gender': [features.gender],
            'Age': [features.age],
            'Tenure': [features.tenure],
            'Balance': [features.balance],
            'NumOfProducts': [features.numOfProducts],
            'HasCrCard': [features.hasCrCard],
            'IsActiveMember': [features.isActiveMember],
            'EstimatedSalary': [features.estimatedSalary],
        })

        processed = self.preprocessor.transform(features)

        prediction = self.model.predict_proba(processed)

        return prediction
