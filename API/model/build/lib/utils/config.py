
NUMERICAL_FEATURES_TO_KEEP = ['wheel-base', 'length', 'width', 'curb-weight','engine-size', 'horsepower', 'highway-mpg', 'price']
FEATURE_2_LOG = ['curb-weight','horsepower', 'length', 'width','price']
DUMMIES_TO_KEEP = ['drive-wheels_rwd', 'num-of-cylinders_four', 'fuel-system_mpfi']
NUMBERS_TO_CATEGORY = ['num-of-cylinders']
ALL_FEATURES = [*NUMERICAL_FEATURES_TO_KEEP,*DUMMIES_TO_KEEP]

