from flask import Flask

hello = Flask(__name__)


# What Req it will understand
@hello.route("/")  # http://www.google.com/ , Homepage
def home():
    return "Hello, world!"


hello.run(port=5000)
