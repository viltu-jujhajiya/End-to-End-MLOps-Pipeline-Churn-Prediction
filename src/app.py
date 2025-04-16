from fastapi import FastAPI
from pydantic import BaseModel
from main import predict_churn 

app = FastAPI(title="Churn Prediction API")

class churn_input(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

@app.get("/")
def root():
    return {"Message:", "Churn Prediction API is running."}

@app.post("/predict")
def predict(input_data: churn_input):

    result = predict_churn(input_data)
    print(result)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=1234)
