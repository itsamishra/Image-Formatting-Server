from flask import Flask
import requests

app = Flask(__name__)


def get_image(image_link):
    response = requests.get(image_link, stream=True)
    print(response)
    print('--------------------------------------------------------------------')
    print(response.raw)
    print('--------------------------------------------------------------------')
    print(response.raw.data)


@app.route("/")
def handle_home():
    return "Go to: /api/format-image"


@app.route("/api/format-image")
def handle_format_image():
    get_image(
        "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
    )

    return "Format Image"


# Runs server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
