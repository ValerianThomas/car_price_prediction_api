from flask import Flask 
from .controller import prediction_app
def create_app () :
  flask_app = Flask('ml_api')
  flask_app.register_blueprint(prediction_app)
  return flask_app
  