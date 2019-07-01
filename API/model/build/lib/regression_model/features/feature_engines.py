import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

class NumericalLog(BaseEstimator, TransformerMixin):
    """Remove index with unknown price """

    def __init__(self, variables=None) -> None:
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X: pd.DataFrame, y: pd.Series = None) -> 'masks':
        """Fit statement to accomodate the sklearn pipeline."""
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """Apply the transforms to the dataframe."""
        X = X.copy()
        for variable in self.variables :
            X[variable] = np.log1p(X[variable])
        return X