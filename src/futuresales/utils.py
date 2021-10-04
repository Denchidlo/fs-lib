import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error as mse
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
from sklearn.preprocessing import StandardScaler


def hyperopt_objective(model, train_data, test_data):

    train_x, train_y = train_data
    test_x, test_y = test_data

    def _loss(kwargs):
        _m_instance = model(**kwargs)
        _m_instance.fit(train_x, train_y)
        result = {
            'loss': np.sqrt(mse(_m_instance.predict(test_x), test_y)),
            'status': STATUS_OK,
            'other_stuff': {
                'kwargs': kwargs,
                'train_rmse': np.sqrt(mse(_m_instance.predict(train_x), train_y)),
            },
        }
        return result

    return _loss


def make_scaled(df_origin):
    def standartize(dataset):
        scaler = StandardScaler()
        try:
            return scaler.fit_transform(dataset.to_numpy())
        except:
            return scaler.fit_transform(dataset)

    df = pd.DataFrame(
        data=standartize(df_origin), 
        index=df_origin.index, 
        columns=df_origin.columns
    )
    return df

def load_credentials(path):
    from json import load
    with open(path, 'r') as reader:
        return load(reader)