from flask import Flask, request
import requests


# Gets image file (in bytes) from url
def get_image_from_url(image_link):
    response = requests.get(image_link, stream=True)
    image_bytes = response.raw.data

    return image_bytes


# Defines Flask app
app = Flask(__name__)

# Handles home page
@app.route("/")
def handle_home():
    return "Go to: /api/format-image"


# Handles formate imgae api request
@app.route("/api/format-image")
def handle_format_image():
    query_parameter_dict = request.args

    # Gets image url from query parameters
    image_url = request.args.get("image-url")
    if image_url == None:
        raise Exception("ERROR: 'image-url' query parameter missing")

    # Loads image into memory
    image_file = get_image_from_url(image_url)

    return "Format Image [REPLACE LATER]"


# Runs server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
