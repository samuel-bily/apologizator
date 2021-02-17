from flask import Flask, render_template, send_from_directory, request, jsonify, make_response
from flask_cors import CORS, cross_origin
import os
from textgenrnn import textgenrnn

app = Flask(__name__, static_folder='hello-react', static_url_path='')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@cross_origin()
def helloWorld():
    return "Hello, cross-origin-world!"

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')
   
@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/generate', methods=['GET'])
def generate():
    textgen = textgenrnn("textgenrnn_weights_4epochs.hdf5")
    apology = textgen.generate(n=1, return_as_list=True)
    return "/n".join(apology)

@app.route('/params', methods=['POST'])
def parameters():
    text_input = request.form["data"]
    return jsonify({'message': 'Data received sucessfully!'}), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, threaded=False)
