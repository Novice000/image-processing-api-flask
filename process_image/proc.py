import os
from flask import Blueprint, jsonify, request, send_file
from rembg import remove
from PIL import Image
from io import BytesIO
import json

image_proc_bp = Blueprint('proc', __name__)

@image_proc_bp.route('/process-image', methods=['POST', 'GET'])
def process_image():
    if request.method == 'POST':
        image = request.files.get('image', None)
        
        if not image:
            return jsonify({'status': 'error', 'error': 'No image uploaded'}), 400
        
        # Validate file type
        name, ext = os.path.splitext(image.filename)
        ext = ext.lower().replace('.', '')
        ext = 'jpeg' if ext == 'jpg' else ext
        
        data = request.form
        quality = data.get('quality', 75)
        format = data.get('format', ext).lower()
        removebg = data.get('removebg', 'false').lower() == 'true'
        
        print(quality, format, removebg)
        print(data)
        
        allowed_extensions = {'png', 'jpg', 'jpeg', 'webp', 'tiff', 'tif'}
        if ext not in allowed_extensions:
            return jsonify({'status': 'error', 'error': 'Only PNG, JPEG, and JPG images are allowed'}), 400
        try:
            image = Image.open(image)
        except Exception as e:
            return jsonify({'status': 'error', 'error': str(e)}), 500

        if removebg:
            image = image.convert('RGBA')
            image = remove(image)
            
            # # Convert to RGB if output format does not support transparency
            # if format in {"jpg", "jpeg"}:
            #     image = image.convert('RGB')
            
            
        try:
            quality = int(quality)
        except:
            return jsonify({'status': 'error', 'error': 'Quality must be an integer'}), 400
        if quality < 0 or quality > 100:
            return jsonify({'status': 'error', 'error': 'Quality must be between 0 and 100'}), 400

        # Save image to memory
        imageBlob = BytesIO()
        save_params = {"format": format.upper()}
        if format in {"jpg", "jpeg"}:
            save_params["quality"] = quality
        image.save(imageBlob, **save_params)
        imageBlob.seek(0)

        return send_file(
            imageBlob,
            mimetype=f'image/{format}',
            as_attachment=True,
            download_name=f'{name}-{quality}%-quality.{format}'
        )

    return jsonify({'status': 'error', 'error': 'Method not allowed'}), 405