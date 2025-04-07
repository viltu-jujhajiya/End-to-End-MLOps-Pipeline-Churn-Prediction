import pandas as pd
import os
from sklearn.preprocessing import OneHotEncoder

onehotencoder = OneHotEncoder(sparse_output=False)

def data_preprocessing(input_relative_path, output_relative_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    datapath = os.path.join(script_dir, input_relative_path)

    data = pd.read_csv(datapath)
    processed_data = pd.DataFrame()

    processed_data["gender"] = data["gender"].map({'Male': 1, 'Female' : 0})
    processed_data["SeniorCitizen"] = data['SeniorCitizen'].copy()
    processed_data["Partner"] = data["Partner"].map({'Yes': 1, 'No': 0})
    processed_data["Dependents"] = data["Dependents"].map({'Yes': 1, 'No': 0})
    processed_data["tenure"] = data["tenure"].copy()
    processed_data["PhoneService"] = data["PhoneService"].map({'Yes': 1, 'No': 0})
    processed_data["MultipleLines"] = data["MultipleLines"].map({'Yes': 1, 'No': 0, 'No phone service': 0})
    processed_data["InternetService"] = data["InternetService"].map({'DSL': 1, 'Fiber optic': 2, 'No': 0})
    processed_data["OnlineSecurity"] = data["OnlineSecurity"].map({'Yes': 1, 'No': 0, 'No internet service': 0})
    processed_data["OnlineBackup"] = data["OnlineBackup"].map({'Yes': 1, 'No': 0, 'No internet service': 0})
    processed_data["DeviceProtection"] = data["DeviceProtection"].map({'Yes': 1, 'No': 0, 'No internet service': 0})
    processed_data["TechSupport"] = data["TechSupport"].map({'Yes': 1, 'No': 0, 'No internet service': 0})
    processed_data["StreamingTV"] = data["StreamingTV"].map({'Yes': 1, 'No': 0, 'No internet service': 0})
    processed_data["StreamingMovies"] = data["StreamingMovies"].map({'Yes': 1, 'No': 0, 'No internet service': 0})
    processed_data["Contract"] = data["Contract"].map({'Month-to-month': 0, 'One year': 1, 'Two year': 2})
    processed_data["PaperlessBilling"] = data["PaperlessBilling"].map({'Yes': 1, 'No': 0})

    encoded_paymentmethod = onehotencoder.fit_transform(data[["PaymentMethod"]])
    processed_data = pd.concat([processed_data, pd.DataFrame(encoded_paymentmethod, columns=onehotencoder.get_feature_names_out(["PaymentMethod"]))], axis=1)

    processed_data["MonthlyCharges"] = data["MonthlyCharges"].copy()
    processed_data["TotalCharges"] = pd.to_numeric(data["TotalCharges"], errors="coerce")
    processed_data["Churn"] = data["Churn"].map({'Yes': 1, 'No': 0})

    processed_data.to_csv(os.path.join(script_dir, output_relative_path), index=False)


# with open("param.yaml", "r") as file:
#     config = yaml.safe_load(file)

# data_preprocessing(config["train_data_relative_path"], config["processed_train_relative_path"])
