# Image Processing API (Flask Version)

## Overview

This is a Flask-based image processing API that allows users to upload an image, process it, and download the modified version. The API supports background removal using `rembg` and allows users to specify image quality and format.

## Why Flask?

This project was originally written in Django but has been migrated to Flask due to its lightweight nature, making it more suitable for quick deployments and microservices.

## Features

- Accepts image uploads via `multipart/form-data`
- Supports PNG, JPG, JPEG, WEBP, TIFF, and TIF formats
- Background removal using `rembg`
- Adjustable image quality (0-100)
- Allows output format conversion
- Returns the processed image as a downloadable file

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/image-processing-api-flask.git
   cd image-processing-api-flask
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

1. Export the Flask app:

   ```sh
   export FLASK_APP=app.py  # On Windows: set FLASK_APP=app.py
   ```

2. Run the Flask server:

   ```sh
   gunicorn app:app
   ```

## API Endpoints

### 1. Process Image

- **Endpoint:** `POST /image-proc`
- **Request Type:** `multipart/form-data`
- **Parameters:**
  - `image` (file, required): The image to be processed
  - `quality` (integer, optional): Image quality (0-100, default: 75)
  - `format` (string, optional): Output format (`png`, `jpg`, `jpeg`, `webp`, `tiff`, default: `png`)
  - `removebg` (boolean, optional): Whether to remove the background (default: `false`)

#### Example Request (Using `cURL`)

```sh
curl -X POST http://127.0.0.1:5000/image-proc \
     -F "image=@sample.jpg" \
     -F "quality=80" \
     -F "format=png" \
     -F "removebg=true" \
     -o output.png
```

## Technologies Used

- **Flask** - Lightweight web framework
- **Pillow (PIL)** - Image processing
- **rembg** - Background removal
- **io.BytesIO** - In-memory file handling
- **gunicorn** - Running the flask backend

## Future Improvements

- Add authentication and rate limiting
- Support for additional image transformations
- Deploy as a Dockerized microservice
