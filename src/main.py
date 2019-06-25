from flask import Flask, request
import requests
from PIL import Image
from io import BytesIO
import base64


# Gets image from url and converts it to Image object
def get_image_from_url(image_link):
    response = requests.get(image_link)
    image = Image.open(BytesIO(response.content))

    return image


# Resizes image to specified dimentions
def resize_image(image, width, height):
    resized_image = image.resize((width, height))

    return resized_image


def save_image(image):
    image.save("image.png")


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

    # Gets image from URL
    image = get_image_from_url(image_url)

    # =====>>> Image format pipeline <<<=====
    # Resize image
    width = request.args.get("width")
    height = request.args.get("height")
    image = resize_image(image, width, height)

    # Change image formt

    
    # Converts image to base64 string
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    image_base64_bytes = base64.b64encode(buffered.getvalue())
    image_base64_string = image_base64_bytes.decode("utf-8")

    # Returns formatted image
    return f"""<img src="data:image;base64, {image_base64_string}" />"""


# Runs server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
