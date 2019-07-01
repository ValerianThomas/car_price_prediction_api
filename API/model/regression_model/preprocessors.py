import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pickle
class MissingPriceRemover(BaseEstimator, TransformerMixin):
    """Remove index with unknown price """


    def fit(self, X: pd.DataFrame, y: pd.Series = None) -> 'masks':
        """Fit statement to accomodate the sklearn pipeline."""
        self.index_mask = X['price'].isna() == False
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """Apply the transforms to the dataframe."""

        X = X.copy()
        return X.loc[self.index_mask,:]

class NumericalNanREplace(BaseEstimator, TransformerMixin):
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
            X[variable] = X[variable].fillna(X[variable].mode()[0])
        return X

class GetDummies(BaseEstimator, TransformerMixin):
    """Remove index with unknown price """

    def __init__(self, variables=None, dummies_to_keep = None , numerical_to_keep = None) -> None:
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

        if not isinstance(dummies_to_keep, list):
            self.dummies_to_keep = [dummies_to_keep]
        else:
            self.dummies_to_keep = dummies_to_keep

        if not isinstance(numerical_to_keep, list):
            self.numerical_to_keep = [numerical_to_keep]
        else:
            self.numerical_to_keep = numerical_to_keep
        
        self.to_keep = [*self.numerical_to_keep,*self.dummies_to_keep]

    def fit(self, X: pd.DataFrame, y: pd.Series = None) -> 'masks':
        """Fit statement to accomodate the sklearn pipeline."""
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """Apply the transforms to the dataframe."""
        X = X.copy()
        for variable in self.variables :
            X[variable] = X[variable].astype('object')

        X = pd.get_dummies(X, drop_first=False)

        for item in self.dummies_to_keep :
            if item not in X.columns :
                X[item] = [0]*len(X.index)

        return X[self.to_keep]
    

