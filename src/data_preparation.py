'''Py file to prepare data for Churn Prediction project'''
import pandas as pd
from sklearn.model_selection import train_test_split
from logger import logger


def data_preparation(datapath: str,
                     test_size: str,
                     train_datapath: str,
                     test_datapath: str) -> None:
    '''datapath: complete datapath for raw data
    test_size: test data size after spliting
    train_datapath: complete path where training data should be stored
    test_datapath: complete path where test data should be stored'''
    try:
        data = pd.read_csv(datapath)
        train, test = train_test_split(data,
                                       test_size=test_size,
                                       random_state=42)
        # print(train.shape, test.shape)
        train.to_csv(train_datapath, index=False)
        test.to_csv(test_datapath, index=False)
        logger.info("Train and Test data has been saved.")
    except Exception as e:
        logger.info("Exception in data_preparation.py: %s.", e)


# with open("param.yaml", "r") as file:
#     config = yaml.safe_load(file)
# data_relative_path = config["data_relative_path"]
# test_data_size = config["test_data_size"]
# train_data_relative_path = config["train_data_relative_path"]
# test_data_relative_path = config["test_data_relative_path"]
