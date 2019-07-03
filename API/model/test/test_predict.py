import math
from ..regression_model.trained_models.predict import make_prediction
import pandas as pd 
import pathlib
import numpy as np 
import requests
test_csv = pathlib.Path.cwd()/'API'/'model'/'regression_model'/'datasets'/'test.csv'  
def test_make_prediction():
  test_data = pd.read_csv(test_csv)
  single_test_json =  test_data[0:1].to_json(orient='records')
  subject = make_prediction(input_data = single_test_json)
  
  # then
  assert subject is not None
  assert isinstance(subject['prediction'][0],float)
  assert np.ceil(subject['prediction'][0]) == 9096.0


def test_make_prediction_full_set():
  test_data = pd.read_csv(test_csv)
  print("len",len(test_data.columns))
  multiple_data_test =  test_data.to_json(orient='records')
  subject = make_prediction(input_data = multiple_data_test)
  
  # then
  assert subject is not None
  assert len(subject['prediction']) == 21

def test_api_health():
  response = requests.get('http://127.0.0.1:5000/health')
  print("data returned",response)

  # then
  assert response.status == 200


def test_api_prediction():
  test_data = pd.read_csv(test_csv)
  multiple_data_test =  test_data.to_json(orient='records')
  response = requests.post('http://127.0.0.1:5000/predict',json = multiple_data_test)
  print("response",response)
  
if __name__ == '__main__':
  test_make_prediction()