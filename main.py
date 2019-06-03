# Dynamo
# jakonen@github
from flask import Flask, render_template
from flask import request
import requests


API_URL = "https://api.cloudflare.com/client/v4/zones/"


def send_to_dns():
    print(0)


# Initiate the api app
api = Flask(__name__)


@api.route('/')
def index():
    return render_template("index.html")


@api.route('/create', methods=['GET', 'POST'])
def create_record():
    data = request.get_json()
    return "Success"


if __name__ == '__main__':
    api.run(port=8003)
