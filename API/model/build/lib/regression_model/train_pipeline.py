import pathlib
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
from . import pipeline
PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / 'trained_models'
DATASET_DIR = PACKAGE_ROOT / 'datasets'

TESTING_DATA_FILE = DATASET_DIR / 'test.csv'
TRAINING_DATA_FILE = DATASET_DIR / 'train.csv'
TARGET = 'price'
from . import __version__ as _version

def save_pipeline(*,model_to_persist) -> None:
    filename = f'model_{_version}.sav'
    filepath = TRAINED_MODEL_DIR / filename

    pickle.dump(model_to_persist,open(filepath,'wb'))
    print('saved pipline')

def remove_old_pipelines (*, versions_to_keep) -> None:
    for model_file in TRAINED_MODEL_DIR.iterdir():
        if model_file  not in [versions_to_keep, __init__.py]:
            model_file.unlink()

def run_training() -> None:
    """Train the model."""
    data = pd.read_csv(TRAINING_DATA_FILE)
    mask = data['price'].isna() == False
    data = data.loc[mask,:]
    X_train, X_test, y_train, y_test = train_test_split(data,data[TARGET],test_size=0.1, random_state = 0)
    y_train = np.log1p(y_train)
    y_test = np.log1p(y_test)
    pipeline.price_pipe.fit(X_train,y_train)
    save_pipeline(model_to_persist = pipeline.price_pipe)


if __name__ == '__main__':
    run_training()
