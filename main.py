# Dynamo
# jakonen@github
from flask import Flask, render_template
from flask import request
import requests
import json
import os


API_URL = "https://api.cloudflare.com/client/v4/zones/"


# Sends a POST request to the DNS API
# and calls it to create a new record
def send_to_dns(sub_domain, ip):
    # Load env variables
    zone_id = os.getenv('CFZONE')
    api_key = os.getenv('CFAPI')
    auth_mail = os.getenv('CFEMAIL')

    # Define request parameters
    target = API_URL + zone_id + "/dns_records"
    request_json = '{"type": "A", "name": "' + sub_domain + '.vey.cool", "content": "' + ip + '"}'

    # Make a request
    req = requests.post(target,
                        headers={
                            "X-Auth-Email": auth_mail,
                            "X-Auth-Key": api_key,
                            "Content-Type": "application/json"
                        },
                        data=request_json
                        )

    # Return the API response
    return req.text


# Initiate the api app
api = Flask(__name__)


# Root path
@api.route('/')
def index():
    # Print index.html
    return render_template("index.html")


# Record creation path
@api.route('/create', methods=['GET', 'POST'])
def create_record():
    # Parse POST parameters
    data = json.loads(request.data)

    # Initiate a response to the frontend
    internal_response = {
        "success": True,
        "body": "New DNS record created"
    }

    # Return error on empty fields
    if data[0] == "" or data[1] == "":
        internal_response["success"] = False
        internal_response["body"] = "Both fields are required"
        return json.dumps(internal_response)

    # Make a POST request
    dns_response = json.loads(send_to_dns(data[0], data[1]))

    # Handle errors on record creation
    if not dns_response["success"]:
        internal_response["success"] = False
        try:
            internal_response["body"] = dns_response["errors"][0]["message"]
        except KeyError:
            internal_response["body"] = "Internal server error"
        except IndexError:
            internal_response["body"] = "Internal server error"
        return json.dumps(internal_response)

    # Return data to the frontend
    return json.dumps(internal_response)


if __name__ == '__main__':
    api.run(port=8003)
