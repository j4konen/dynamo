# Dynamo
# jakonen@github
from flask import Flask, render_template
from flask import request
import requests


# Initiate the api app
api = Flask(__name__)


@api.route('/')
def index():
    return render_template("index.html")


@api.route('/create', methods=['GET', 'POST'])
def create():
    data = request.get_json()
    print(data)


if __name__ == '__main__':
    api.run(port=8003)
