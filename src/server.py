from flask import Flask
from flask import send_from_directory
from Storage import Storage
import json

store = Storage()

app = Flask(__name__)


@app.route('/api/macros')
def get_macro_names():
    return json.dumps(store.get_macros("../macros"))


@app.route('/api/scripts')
def get_script_names():
    return json.dumps(store.get_scripts("../scripts"))


@app.route('/images/<path:filename>')
def get_image(filename):
    return send_from_directory("../images/targets", filename)


@app.route('/api/allimages')
def get_all_image():
    return json.dumps(store.get_images("../images/targets"))


if __name__ == '__main__':
    app.run()
