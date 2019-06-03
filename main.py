# Dynamo
# jakonen@github
from flask import Flask, render_template
from flask import request
import requests
import os


API_URL = "https://api.cloudflare.com/client/v4/zones/"


def send_to_dns(sub_domain, ip):
    zone_id = os.getenv('CFZONE')
    api_key = os.getenv('CFAPI')
    auth_mail = os.getenv('CFEMAIL')

    target = API_URL + zone_id + "/dns_records"
    request_json = {"type": "A", "name": sub_domain + ".vey.cool", "content": ip}
    print(request_json)

    req = requests.post(target,
                        headers={"X-Auth-Email": auth_mail, "X-Auth-Key": api_key, "Content-Type": "application/json"},
                        data=request_json
                        )

    print(req.text)


send_to_dns("hello", "8.8.8.8")


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
