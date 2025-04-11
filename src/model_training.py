import pandas as pd
import os
import pickle
from sklearn.ensemble import RandomForestClassifier


model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    criterion='gini'
    )


def model_training(input_data_relative_path, model_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data_path = os.path.join(script_dir, input_data_relative_path)
    data = pd.read_csv(input_data_path)
    X_train = data.drop(['Churn'], axis=1, inplace=False)
    y_train = data['Churn']

    model.fit(X_train, y_train)
    with open(model_path, 'wb') as file:
        pickle.dump(model, file)
