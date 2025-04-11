'''main file of Churn Prediction project'''
import os
import yaml
from data_preparation import data_preparation
from data_preprocessing import data_preprocessing
from model_training import model_training
from model_eval import model_eval

script_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(script_dir, "..", "param.yaml"), "r", encoding='utf-8') as file:
    config = yaml.safe_load(file)


def main():
    '''Main function'''
    data_relative_path = config["data_relative_path"]
    test_data_size = config["test_data_size"]
    train_data_relative_path = config["train_data_relative_path"]
    test_data_relative_path = config["test_data_relative_path"]
    processed_train_relative_path = config["processed_train_relative_path"]
    model_relative_path = config["model_path"]
    datapath = os.path.join(script_dir, data_relative_path)
    train_datapath = os.path.join(script_dir, train_data_relative_path)
    test_datapath = os.path.join(script_dir, test_data_relative_path)
    processed_train_datapath = os.path.join(script_dir,
                                            processed_train_relative_path)
    model_path = os.path.join(script_dir, model_relative_path)

    # Preparing Data
    data_preparation(datapath, test_data_size, train_datapath, test_datapath)

    # Processing Data
    processed_data = data_preprocessing(datapath)
    processed_data.to_csv(processed_train_datapath, index=False)

    # Fitting model on processed training data
    model_training(processed_train_relative_path, model_path)

    # Evaluating model
    results = model_eval(model_path, test_datapath)
    print(results)


if __name__ == "__main__":
    main()
