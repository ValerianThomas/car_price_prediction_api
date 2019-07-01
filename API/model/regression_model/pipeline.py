from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from . import preprocessors as pp
from .features import feature_engines as features
NUMERICAL_FEATURES_TO_KEEP = ['wheel-base', 'length', 'width', 'curb-weight','engine-size', 'horsepower', 'highway-mpg', 'price']
FEATURE_2_LOG = ['curb-weight','horsepower', 'length', 'width','price']
DUMMIES_TO_KEEP = ['drive-wheels_rwd', 'num-of-cylinders_four', 'fuel-system_mpfi']
NUMBERS_TO_CATEGORY = ['num-of-cylinders']
ALL_FEATURES = [*NUMERICAL_FEATURES_TO_KEEP,*DUMMIES_TO_KEEP]
PIPELINE_NAME = 'random_forest_regressor'

price_pipe = Pipeline(
    [
         ('numerical_nan_replacer',
         pp.NumericalNanREplace(variables = NUMERICAL_FEATURES_TO_KEEP)),
         ('numerical_to_log',
         features.NumericalLog(variables = FEATURE_2_LOG)),
         ('get_dummies',
         pp.GetDummies(variables = NUMBERS_TO_CATEGORY, dummies_to_keep = DUMMIES_TO_KEEP, numerical_to_keep = NUMERICAL_FEATURES_TO_KEEP)),
         ('model_creation',
         RandomForestRegressor(bootstrap=False,max_depth=93,max_features='sqrt',min_samples_leaf=1,min_samples_split=3, n_estimators=667, random_state = 0 )
         )
         
    ]
    )
