from pydantic import BaseModel
from typing import Optional

class Features(BaseModel):

    ##LIST THEM HERE
    creditScore: float = 0
    geography: str = ""
    gender: str = ""
    age: int = 0
    tenure: float = 0
    balance: float = 0
    numOfProducts: float = 0
    hasCrCard: int = 0
    isActiveMember: int = 0
    estimatedSalary: float = 0


    def __str__(self):
        return f"Features:\n\tCreditScore: {self.creditScore}\n\tGeography: {self.geography}\n\tGender: {self.gender}\n\tAge: {self.age}\n\tTenure: {self.tenure}\n\tBalance: {self.balance}\n\tNumOfProducts: {self.numOfProducts}\n\tHasCrCard: {self.hasCrCard}\n\tIsActiveMember: {self.isActiveMember}\n\tEstimatedSalary: {self.estimatedSalary}"
    
    def __repr__(self):
        return f"Features:\n\tCreditScore: {self.creditScore}\n\tGeography: {self.geography}\n\tGender: {self.gender}\n\tAge: {self.age}\n\tTenure: {self.tenure}\n\tBalance: {self.balance}\n\tNumOfProducts: {self.numOfProducts}\n\tHasCrCard: {self.hasCrCard}\n\tIsActiveMember: {self.isActiveMember}\n\tEstimatedSalary: {self.estimatedSalary}"