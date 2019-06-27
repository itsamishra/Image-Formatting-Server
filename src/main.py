from flask import Flask, request
import requests
from PIL import Image, ImageFilter
from io import BytesIO
import base64


# Constants
VALID_FILTERS = [
    "blur",
    "contour",
    "detail",
    "edge_enhance",
    "edge_enhance_more",
    "emboss",
    "sharpen",
    "smooth",
    "smooth_more",
]

# Gets image from url and converts it to Image object
def get_image_from_url(image_link):
    response = requests.get(image_link)
    image = Image.open(BytesIO(response.content))

    return image


# Resizes image to specified dimentions
def resize_image(image, width, height):
    resized_image = image.resize((width, height))

    return resized_image


# Filters image
def filter_image(image, filter_name):
    if filter_name == "blur":
        image = image.filter(ImageFilter.BLUR)
    elif filter_name == "contour":
        image = image.filter(ImageFilter.CONTOUR)
    elif filter_name == "detail":
        image = image.filter(ImageFilter.DETAIL)
    elif filter_name == "edge_enhance":
        image = image.filter(ImageFilter.EDGE_ENHANCE)
    elif filter_name == "edge_enhance_more":
        image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    elif filter_name == "emboss":
        image = image.filter(ImageFilter.EMBOSS)
    elif filter_name == "sharpen":
        image = image.filter(ImageFilter.SHARPEN)
    elif filter_name == "smooth":
        image = image.filter(ImageFilter.SMOOTH)
    elif filter_name == "smooth_more":
        image = image.filter(ImageFilter.SMOOTH_MORE)

    return image


# Create <img> tag from base64 encoded image string
def create_img_html_tag(image_base64_string):
    return f"""<img src="data:image;base64, {image_base64_string}" />"""


# Defines Flask app
app = Flask(__name__)

# Handles home page
@app.route("/")
def handle_home():
    return "Go to: /api/format-image"


# Encodes image as a base64 string
def encode_image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    image_base64_bytes = base64.b64encode(buffered.getvalue())
    image_base64_string = image_base64_bytes.decode("utf-8")

    return image_base64_string


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

    # <======================================================================>
    # <======================= Image format pipeline ========================>
    # <======================================================================>
    # Resize image (user can specify height & width, just height, or just width)
    width = request.args.get("width")
    height = request.args.get("height")
    if width != None and height != None:
        width = int(width)
        height = int(height)
        image = resize_image(image, width, height)
    elif width == None and height != None:
        height = int(height)
        width = int(height * (image.width / image.height))
        image = resize_image(image, width, height)
    elif width != None and height == None:
        width = int(width)
        height = int(width * (image.height / image.width))
        image = resize_image(image, width, height)

    # Crop image
    left = request.args.get("left")
    top = request.args.get("top")
    right = request.args.get("right")
    bottom = request.args.get("bottom")
    if left != None and top != None and right != None and bottom != None:
        image = image.crop((int(left), int(top), int(right), int(bottom)))

    # Filter image
    filter_string = request.args.get("filters")
    if filter_string != None:
        filter_list = filter_string.lower().split(",")
        for filter_name in filter_list:
            if filter_name in VALID_FILTERS:
                image = filter_image(image, filter_name)
                # print(filter_image(image, filter_name))

        image = image.filter(ImageFilter.SHARPEN)

    # Converts image to base64 string
    image_base64_string = encode_image_to_base64(image)

    # DEBUG
    image.save("test.png")
    # DEBUG

    # Returns formatted image
    return create_img_html_tag(image_base64_string)


# Runs server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
