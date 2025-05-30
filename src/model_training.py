'''Classifier training for Churn Prediction project'''
import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from logger import logger

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    criterion='gini'
    )


def model_training(input_data_relative_path: str,
                   model_path: str) -> None:
    '''input_data_relative_path: relative path of the training data
    model_path: complete path where trained model should be saved'''
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        input_data_path = os.path.join(script_dir, input_data_relative_path)
        data = pd.read_csv(input_data_path)
        x_train = data.drop(['Churn'], axis=1, inplace=False)
        y_train = data['Churn']

        model.fit(x_train, y_train)
        logger.info("Model training done.")
        with open(model_path, 'wb') as file:
            joblib.dump(model, file)
        logger.info("Trained model has been saved.")
    except Exception as e:
        logger.info("Exception in model_training.py: %s.", e)
