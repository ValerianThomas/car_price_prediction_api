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


def get_score(*,input_data) -> None :
  

  data = pd.read_json(input_data)
  y_true = data['price']
  score = pickle.load(open(MODEL_SAV,'rb')).score(data,y_true)
  pickle.dump(score,open('previews_score.sav','wb'))
"""
  if score > previews_score - 0.05 or previews_score == None :
    pickle.dump(score,open('previews_score.sav','wb'))
    return True 
  else :
    return False
"""