from flask import Flask

# Image class
class image:
    imageLink = ''
    newLength = 0
    newWidth = 0
    imageFormat = ''
    newImageFormat = ''
    def __init__(self):
        pass

app = Flask(__name__)

@app.route('/')
def homePage():
    i = image()
    print(i.imageLink)
    return 'Go to /api/imageformat'

@app.route('/api/imageformat')
def imageFormat():
    return 'image format'



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
