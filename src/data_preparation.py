import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split

def data_preparation(datapath, test_data_size, train_datapath, test_datapath):
    data = pd.read_csv(datapath)
    train, test = train_test_split(data, test_size=test_data_size, random_state=42)
    # print(train.shape, test.shape)
    train.to_csv(train_datapath, index=False)
    test.to_csv(test_datapath, index=False)


# with open("param.yaml", "r") as file:
#     config = yaml.safe_load(file)
# data_relative_path = config["data_relative_path"]
# test_data_size = config["test_data_size"]
# train_data_relative_path = config["train_data_relative_path"]
# test_data_relative_path = config["test_data_relative_path"]
# data_preparation(data_relative_path, test_data_size, train_data_relative_path, test_data_relative_path)