from flask import Flask
import os
from flask import render_template, send_from_directory
from textgenrnn import textgenrnn

app = Flask(__name__)

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    textgen = textgenrnn(weights_path='model_weights.hdf5',
                       vocab_path='model_vocab.json',
                       config_path='model.json')
    lyrics = textgen.generate()
    return "\n".join(lyrics)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=False)
