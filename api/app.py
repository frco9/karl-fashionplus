#api/app.py
import os
import requests
from flask import Flask, current_app, Response, json, jsonify, request, send_from_directory
from flask_cors import CORS


def create_app():
  """
  Create app
  """
  app = Flask(__name__)

  CORS(app, supports_credentials=True)

  def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
      mimetype="application/json",
      response=json.dumps(res),
      status=status_code
    )


  @app.route('/', methods=['GET'])
  def index():
    return 'alive'
  
  
  @app.route('/getFashion', methods=['POST'])
  def get_fashion_suggest():
    data = request.json
    os.system('cd classification/data_dict/shape_and_feature/ && ./scripts/edit_and_visualize_demo.sh 3.jpg shape_and_texture False 0 13 0.25')
    # subprocess.call(['./scripts/edit_and_visualize_demo.sh 2.jpg shape_and_texture True 0 10 0.25'], '../classification/data_dict/shape_and_feature/')
    return send_from_directory('/home/jeremie/FashionPlus/classification/data_dict/shape_and_feature/results/demo/images/', 'reconstructed_3.jpg')

  

  return app