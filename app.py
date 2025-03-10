from flask import Flask, jsonify
from process_image.proc import image_proc_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(image_proc_bp, url_prefix='/api')
@app.route('/')
def index():
    return jsonify({
        'status': 'success',
        'message': 'wrong endpoint, hit the /process-image endpoint with a post request'
    })


if __name__ == '__main__':
    app.run()
