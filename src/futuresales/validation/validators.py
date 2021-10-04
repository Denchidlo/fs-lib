import numpy as np
from sklearn.metrics import mean_squared_error as mse

class Validator:
    def __init__(self, model, **kwargs) -> None:
        self.model = model(**kwargs)
        self._train_err = None

    def fit(self, x, y, trained_model=None):
        if trained_model is None:
            self.model.fit(x, y)
            self._train_err = np.sqrt(mse(self.model.predict(x), y))
        else:
            self.model = trained_model

        return self.model

    def validate(self, x, y):
        
        predictions = self.model.predict(x)
        truth = y

        return np.sqrt(mse(predictions, truth)), self._train_err,  predictions, truth

def get_statistics(report):
    stat = report[3]
    stat['residuals'] = report[2].transpose()[0] - report[3].valid_target
    stat['predicted'] = report[2]
    stat['object_id'] = report[3].index
    return stat

def causation_1_percent(residuals):


    giants = (residuals.sort_values('abs_residuals').tail(422))
    totals = (residuals.residuals @ residuals.residuals)

    giants['part'] = (residuals.residuals ** 2) / totals
    print(f'0.1% of objects cause {(giants.residuals @ giants.residuals)/(totals)} of error')
    
    return giants