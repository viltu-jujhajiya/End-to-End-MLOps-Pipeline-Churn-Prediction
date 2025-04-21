'''main file of Churn Prediction project'''
import os
from typing import Optional, BinaryIO
import pandas as pd
import yaml
import joblib
from data_preparation import data_preparation
from data_preprocessing import data_preprocessing
from model_training import model_training
from model_eval import model_eval
from logger import logger

script_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(script_dir, "..", "param.yaml"),
          "r", encoding='utf-8') as f:
    config = yaml.safe_load(f)


def main() -> None:
    '''Main function'''
    data_relative_path = config["data_relative_path"]
    test_data_size = config["test_data_size"]
    train_data_relative_path = config["train_data_relative_path"]
    test_data_relative_path = config["test_data_relative_path"]
    processed_train_relative_path = config["processed_train_relative_path"]
    datapath = os.path.join(script_dir, data_relative_path)
    train_datapath = os.path.join(script_dir, train_data_relative_path)
    test_datapath = os.path.join(script_dir, test_data_relative_path)
    processed_train_datapath = os.path.join(script_dir,
                                            processed_train_relative_path)

    # Preparing Data
    logger.info("Preparing data.")
    data_preparation(datapath, test_data_size, train_datapath, test_datapath)
    logger.info("Done preparing data.")

    # Processing Data
    data = pd.read_csv(datapath)
    logger.info("Processing data.")
    processed_data = data_preprocessing(data.copy())
    logger.info("Done processing data")
    processed_data.to_csv(processed_train_datapath, index=False)
    logger.info("Saved processed data.")

    # Fitting model on processed training data
    logger.info("Started model training.")
    model_training(processed_train_relative_path, model_path)
    logger.info("Model training done.")

    # Evaluating model
    logger.info("Testing model on test data.")
    results = model_eval(model_path, test_datapath)
    logger.info(results)

model_relative_path = config["model_path"]
model_path = os.path.join(script_dir, model_relative_path)
if not os.path.exists(model_path):
    logger.info("Couldn't find trained model!!!")
    main()

file: BinaryIO
with open(model_path, "rb") as file:
    model = joblib.load(file)


def predict_churn(input_data) -> Optional[int]:
    '''Fun to do prediction.'''
    try:
        if isinstance(input_data, dict):
            input_data = pd.DataFrame([input_data])
        else:
            input_data = pd.DataFrame([input_data.dict()])

        logger.info("Processing input data.")
        processed_data = data_preprocessing(input_data)
        logger.info("Done processing input data.")
        # processed_data = processed_data.values
        logger.info("Predicting.....")
        result = model.predict(processed_data)
        logger.info("Successfull!!!")
        result = int(result)
        return result
    except Exception as e:
        print(f"Exception: {e} in app (predict_churn).")
        return None
