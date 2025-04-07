import numpy as np
import pandas as pd
import os
import yaml
from sklearn.model_selection import train_test_split

def data_preparation(data_relative_path=r"..\data\raw\Telco-Customer-Churn.csv", test_data_size=0.2):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    datapath = os.path.join(script_dir, data_relative_path)
    data = pd.read_csv(datapath)
    train, test = train_test_split(data, test_size=test_data_size, random_state=42)
    # print(train.shape, test.shape)
    train.to_csv(os.path.join(script_dir, "../data/raw/train.csv"), index=False)
    test.to_csv(os.path.join(script_dir, "../data/raw/test.csv"), index=False)


with open("param.yaml", "r") as file:
    config = yaml.safe_load(file)
    
data_preparation(data_relative_path=config["data_relative_path"], test_data_size=config["test_data_size"])