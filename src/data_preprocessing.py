'''Data processing unit for Churn Prediction project'''
import pandas as pd
from sklearn.preprocessing import OneHotEncoder


onehotencoder = OneHotEncoder(sparse_output=False)


def data_preprocessing(data: dict) -> pd.DataFrame:
    '''datapath: Complete path of the data to be processed'''
    try:
        processed_data = pd.DataFrame()

        # processed_data["gender"] = data["gender"].map({'Male': 1, 'Female' : 0})
        processed_data["SeniorCitizen"] = data['SeniorCitizen']
        processed_data["Partner"] = data["Partner"].map({'Yes': 1, 'No': 0})
        processed_data["Dependents"] = data["Dependents"].map({'Yes': 1, 'No': 0})
        processed_data["tenure"] = data["tenure"]
        processed_data["MultipleLines"] = data["MultipleLines"].map(
                        {'Yes': 1, 'No': 0, 'No phone service': 0})
        processed_data["InternetService"] = data["InternetService"].map(
                        {'DSL': 1, 'Fiber optic': 2, 'No': 0})
        processed_data["OnlineSecurity"] = data["OnlineSecurity"].map(
                        {'Yes': 1, 'No': 0, 'No internet service': 0})
        processed_data["OnlineBackup"] = data["OnlineBackup"].map(
                        {'Yes': 1, 'No': 0, 'No internet service': 0})
        processed_data["DeviceProtection"] = data["DeviceProtection"].map(
                        {'Yes': 1, 'No': 0, 'No internet service': 0})
        processed_data["TechSupport"] = data["TechSupport"].map(
                        {'Yes': 1, 'No': 0, 'No internet service': 0})
        processed_data["StreamingTV"] = data["StreamingTV"].map(
                        {'Yes': 1, 'No': 0, 'No internet service': 0})
        processed_data["StreamingMovies"] = data["StreamingMovies"].map(
                        {'Yes': 1, 'No': 0, 'No internet service': 0})
        processed_data["Contract"] = data["Contract"].map(
                        {'Month-to-month': 0, 'One year': 1, 'Two year': 2})
        processed_data["PaperlessBilling"] = data["PaperlessBilling"].map(
                        {'Yes': 1, 'No': 0})

        enc_column = "PaymentMethod"
        encoded_paymentmethod = onehotencoder.fit_transform(data[[enc_column]])
        encoded_df = pd.DataFrame(
            encoded_paymentmethod,
            columns=onehotencoder.get_feature_names_out([enc_column]))
        processed_data = pd.concat([processed_data, encoded_df], axis=1)

        processed_data["MonthlyCharges"] = data["MonthlyCharges"].copy()
        processed_data["TotalCharges"] = pd.to_numeric(data["TotalCharges"],
                                                    errors="coerce")
        processed_data["Churn"] = data["Churn"].map({'Yes': 1, 'No': 0})

        # Dropping NULL values
        processed_data.dropna(axis=0, inplace=True)

        # Remove ['gender', 'PhoneService'
        # due to their negligible affect on target variable
        # processed_data.drop(['gender', 'PhoneService'], axis=1, inplace=True)

        return processed_data
    except Exception as e:
        print(e in "data preprocessing")


# with open("param.yaml", "r") as file:
#     config = yaml.safe_load(file)
