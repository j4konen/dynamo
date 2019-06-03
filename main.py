# Dynamo
# jakonen@github
from flask import Flask, render_template
from flask import request
import requests
import json
import os


API_URL = "https://api.cloudflare.com/client/v4/zones/"


def send_to_dns(sub_domain, ip):
    zone_id = os.getenv('CFZONE')
    api_key = os.getenv('CFAPI')
    auth_mail = os.getenv('CFEMAIL')

    target = API_URL + zone_id + "/dns_records"
    request_json = '{"type": "A", "name": "' + sub_domain + '.vey.cool", "content": "' + ip + '"}'
    print(request_json)

    req = requests.post(target,
                        headers={"X-Auth-Email": auth_mail, "X-Auth-Key": api_key, "Content-Type": "application/json"},
                        data=request_json
                        )

    return req.text


# Initiate the api app
api = Flask(__name__)


@api.route('/')
def index():
    return render_template("index.html")


@api.route('/create', methods=['GET', 'POST'])
def create_record():
    data = json.loads(request.data)
    dns_response = json.loads(send_to_dns(data[0], data[1]))

    internal_response = {
        "success": True,
        "body": ""
    }

    # Handle errors on record creation
    if not dns_response["success"]:
        internal_response["success"] = False
        try:
            internal_response["body"] = dns_response["errors"][0]["ff"]
        except KeyError:
            internal_response["body"]= "Internal server error"
        except IndexError:
            internal_response["body"] = "Internal server error"
        return json.dumps(internal_response)

    return internal_response


if __name__ == '__main__':
    api.run(port=8003)
