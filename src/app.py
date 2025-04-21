'''app file to run entire project flow'''
import webbrowser
import threading
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from main import predict_churn
from logger import logger

app = FastAPI(title="Churn Prediction API")
templates = Jinja2Templates(directory="src/templates")

logger.info("Execution started.....")


class ChurnInput(BaseModel):
    '''Class for input value's datatypes'''
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

# @app.get("/")
# def root():
#     return {"Message:", "Churn Prediction API is running."}


@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    '''Function to run .html file and build UI.'''
    logger.info("Waiting for feature inputs")
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
async def predict(request: Request):
    '''Function to get data'''
    try:
        uiuiu
        logger.info("Successfully got feature values")
        form_data = await request.form()
        input_data = {
            "gender": form_data.get('gender'),
            "SeniorCitizen": int(str(form_data.get('senior_citizen'))),
            "Partner": form_data.get('partner'),
            "Dependents": form_data.get('dependents'),
            "tenure": float(str(form_data.get('tenure'))),
            "PhoneService": form_data.get('phone_service'),
            "MultipleLines": form_data.get('multiple_lines'),
            "InternetService": form_data.get('internet_service'),
            "OnlineSecurity": form_data.get('online_security'),
            "OnlineBackup": form_data.get('online_backup'),
            "DeviceProtection": form_data.get('device_protection'),
            "TechSupport": form_data.get('tech_support'),
            "StreamingTV": form_data.get('streaming_tv'),
            "StreamingMovies": form_data.get('streaming_movies'),
            "Contract": form_data.get('contract'),
            "PaperlessBilling": form_data.get('paperless_billing'),
            "PaymentMethod": form_data.get('payment_method'),
            "MonthlyCharges": float(str(form_data.get('monthly_charges'))),
            "TotalCharges": float(str(form_data.get('total_charges')))
            }
        logger.info("Main prediction function called")
        result = predict_churn(input_data)
        prediction = f"Customer is likely to \
        {'leave (churn)' if result == 1 else 'stay'}."

        return templates.TemplateResponse("index.html",
                                          {"request": request,
                                           "prediction": prediction})
    except Exception as e:
        logger.info("Exception in app.py(predict): %s.", e)


def open_browser():
    '''Open browser window for UI.'''
    webbrowser.open("http://localhost:1234")


if __name__ == "__main__":
    logger.info("Opening browser!")
    threading.Timer(1.0, open_browser).start()
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=1234)  # nosec
