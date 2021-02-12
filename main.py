from flask import Flask
from flask_cors import CORS, cross_origin
import os
from flask import render_template, send_from_directory
from textgenrnn import textgenrnn




app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@cross_origin()
def helloWorld():
  return "Hello, cross-origin-world!"

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['GET'])
def generate():
    textgen = textgenrnn("model_weights.hdf5")
    apology = textgen.generate(n=1, return_as_list=True)
    return "/n".join(apology)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=False)
