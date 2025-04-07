import numpy as np
import pandas as pd
import os
import yaml
from data_preparation import data_preparation
from data_preprocessing import data_preprocessing

with open("param.yaml", "r") as file:
    config = yaml.safe_load(file)

def main():
    data_relative_path = config["data_relative_path"]
    test_data_size = config["test_data_size"]
    train_data_relative_path = config["train_data_relative_path"]
    test_data_relative_path = config["test_data_relative_path"]
    processed_train_relative_path = config["processed_train_relative_path"]

    data_preparation(data_relative_path, test_data_size, train_data_relative_path, test_data_relative_path)
    data_preprocessing(train_data_relative_path, processed_train_relative_path)


if __name__ == "__main__":
    main()