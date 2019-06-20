from flask import Flask, request
import requests


# Class that contains image format requests
class ImageFormatRequest:
    def __init__(self, to_resize=False, to_convert_type=False):
        self.to_resize = to_resize
        self.to_convert_type = to_convert_type


def get_image(image_link):
    response = requests.get(image_link, stream=True)
    print(response)
    print("--------------------------------------------------------------------")
    print(response.raw)
    print("--------------------------------------------------------------------")
    print(response.raw.data)


# Checks whether all query parameters are present
def all_query_parameters_parsed(query_parameter_list):
    if (
        "to_resize" in query_parameter_list
        and "to_convert_type" in query_parameter_list
    ):
        return True
    else:
        return False


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
    # If all query parameters are parsed, continues with image formatting
    if all_query_parameters_parsed(query_parameter_dict.keys()):
        # Extracts value from parameters
        to_resize = (
            True if query_parameter_dict["to_resize"].lower() == "true" else False
        )
        to_convert_type = (
            True if query_parameter_dict["to_convert_type"].lower() == "true" else False
        )

        # Creates ImageFormatRequest object
        image_format_request = ImageFormatRequest(
            to_resize=to_resize, to_convert_type=to_convert_type
        )
        print(image_format_request.to_resize)
        print(image_format_request.to_convert_type)
    # If any query parameter(s) is/are missing, throws error
    else:
        raise Exception("ERROR: Some query parameter(s) is/are missing")

    # get_image(
    #     "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
    # )

    return "Format Image"


# Runs server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
