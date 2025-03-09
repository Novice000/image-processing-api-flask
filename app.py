from flask import Flask, jsonify
from .process_image.proc import image_proc_bp

app = Flask(__name__)
app.register_blueprint(image_proc_bp, url_prefix='')
@app.route('/')
def index():
    return jsonify({
        'status': 'success',
        'message': 'wrong endpoint, hit the /process-image endpoint with a post request'
    })


if __name__ == '__main__':
    app.run()
