import numpy as np 
import pandas as pd 
import pickle
import pathlib


model = pickle.load(open('model.sav','rb'))

def make_prediction(*,input_data) -> dict :
  data = pd.read_json(input_data)
  print("multi data test", data, len(data.columns))
  prediction = model.predict(data)
  output = np.expm1(prediction)
  response = {'prediction':output}
  
  return response