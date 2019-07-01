from flask import Blueprint, request, jsonify
from ..model.regression_model.trained_models.predict import make_prediction

prediction_app = Blueprint('prediction_app',__name__)

@prediction_app.route('/health',methods = ['GET'])
def health () :
  if request.method == 'GET' :
    return 'ok'

@prediction_app.route('/predict',methods = ['POST'])
def predict () :
  if request.method == 'POST':
    json_data = request.get_json()
    result = make_prediction(input_data = json_data)
    prediction = result.get('prediction')[0]
    print('prediction',prediction)

    return jsonify({'success':True, 'prediction':prediction})

