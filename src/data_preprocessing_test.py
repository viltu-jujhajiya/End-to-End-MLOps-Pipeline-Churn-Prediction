import pandas as pd

def data_preprocessing_test(data: pd.DataFrame) -> pd.DataFrame:
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

        encoded_df = pd.DataFrame([{
            'PaymentMethod_Bank transfer (automatic)': 0,
            'PaymentMethod_Credit card (automatic)': 0,
            'PaymentMethod_Electronic check': 0,
            'PaymentMethod_Mailed check': 0}])
        for c in encoded_df.columns:
            if str(data["PaymentMethod"]) in c:
                encoded_df[c] = 1
                break
        processed_data = pd.concat([processed_data, encoded_df], axis=1)

        processed_data["MonthlyCharges"] = data["MonthlyCharges"].copy()
        processed_data["TotalCharges"] = pd.to_numeric(data["TotalCharges"],
                                                    errors="coerce")

        return processed_data
    except Exception as e:
        print(f"Execption as {e} in data_preprocessing_test.py.")