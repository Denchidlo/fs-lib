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