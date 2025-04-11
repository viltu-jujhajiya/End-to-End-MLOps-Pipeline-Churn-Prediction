import pickle
from data_preprocessing import data_preprocessing
from sklearn.metrics import accuracy_score


def eval(model_path, test_datapath):

    results = {'accuracy_score': 0.0}
    with open(model_path, "rb") as file:
        model = pickle.load(file)

    processed_test_data = data_preprocessing(test_datapath)
    X_test = processed_test_data.drop(['Churn'], axis=1, inplace=False)
    y_test = processed_test_data['Churn']
    y_preds = model.predict(X_test)
    results['accuracy_score'] = accuracy_score(y_test, y_preds)

    return results
