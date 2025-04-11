'''model testing file for Churn Prediction before deployment'''
import pickle
from sklearn.metrics import accuracy_score
from data_preprocessing import data_preprocessing


def model_eval(model_path, test_datapath):
    '''model_path: complete path where model is stored
    test_datapath: complete path of the data to be tested'''

    results = {'accuracy_score': 0.0}
    with open(model_path, "rb") as file:
        model = pickle.load(file)

    processed_test_data = data_preprocessing(test_datapath)
    x_test = processed_test_data.drop(['Churn'], axis=1, inplace=False)
    y_test = processed_test_data['Churn']
    y_preds = model.predict(x_test)
    results['accuracy_score'] = accuracy_score(y_test, y_preds)

    return results
