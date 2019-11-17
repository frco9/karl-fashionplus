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
    file = data.get('filename')
    step_sz = data.get('step_sz', 0.25)
    max_iter = data.get('max_iter', 10)
    auto_swap = data.get('auto_swap', 'True')
    update_type = data.get('update_type', 'shape_and_texture')
    swapped_partid = data.get('swapped_partid', 0)
    if file not in ['3.jpg', '4.jpg', '18.jpg']:
      return custom_response({'error': 'File not found'}, 404)
    if step_sz < 0 or step_sz > 1 :
        return custom_response({'error': 'step_sz should be between 0 and 1'}, 400)
    if auto_swap not in ['True', 'False'] :
      return custom_response({'error': 'auto_swap must be True or False'}, 400)
    if swapped_partid not in [4, 5, 6, 7, 0]:
          return custom_response({'error': 'swapped_partid must be in 4, 5, 6, 7, 0'}, 400)
    if update_type not in ['shape_and_texture', 'shape_only', 'texture_only']:
      return custom_response({'error': 'update_type must be in shape_and_texture, shape_only, texture_only'}, 400)

    os.system('cd classification/data_dict/shape_and_feature/ && ./scripts/edit_and_visualize_demo.sh ' + file + ' ' + update_type + ' ' + auto_swap + ' ' + str(swapped_partid) + ' ' + str(max_iter) + ' ' + str(step_sz))
    return send_from_directory('/home/jeremie/FashionPlus/classification/data_dict/shape_and_feature/results/demo/images/', 'final_' + file)

  

  return app