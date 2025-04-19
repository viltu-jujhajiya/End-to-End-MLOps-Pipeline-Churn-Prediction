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
    data_preparation(datapath, test_data_size, train_datapath, test_datapath)

    # Processing Data
    data = pd.read_csv(datapath)
    processed_data = data_preprocessing(data.copy())
    processed_data.to_csv(processed_train_datapath, index=False)

    # Fitting model on processed training data
    model_training(processed_train_relative_path, model_path)

    # Evaluating model
    results = model_eval(model_path, test_datapath)
    print(results)


model_relative_path = config["model_path"]
model_path = os.path.join(script_dir, model_relative_path)
if not os.path.exists(model_path):
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
        processed_data = data_preprocessing(input_data)
        # processed_data = processed_data.values
        result = model.predict(processed_data)
        result = int(result)
        return result
    except (ValueError, TypeError) as e:
        print(f"Exception: {e} in app (predict_churn).")
        return None
