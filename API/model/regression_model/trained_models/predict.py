import numpy as np 
import pandas as pd 
import pickle
import pathlib
from .. import __version__ as _version
PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent
MODEL_SAV = PACKAGE_ROOT/f'model_{_version}.sav'


def make_prediction(*,input_data) -> None :
  data = pd.read_json(input_data)
  prediction = pickle.load(open(MODEL_SAV,'rb')).predict(data)
  output = np.expm1(prediction)
  response = {'prediction':output}
  return response