# Dynamo
# jakonen@github
from flask import Flask, render_template
from flask import request
import requests
import json
import os


# Load env variables
zone_id = os.getenv('CFZONE')
api_key = os.getenv('CFAPI')
auth_mail = os.getenv('CFEMAIL')


# Define constants
API_URL = "https://api.cloudflare.com/client/v4/zones/"
TOKEN = os.getenv('DYNOPASS')
DOMAIN = ".vey.cool"
REQ_HEADER = {
    "X-Auth-Email": auth_mail,
    "X-Auth-Key": api_key,
    "Content-Type": "application/json"
    }


# Sends a POST request to the DNS API
# and calls it to create a new record
def api_new_dns(sub_domain, ip):
    # Define request parameters
    target = API_URL + zone_id + "/dns_records"
    request_json = '{"type": "A", "name": "' + sub_domain + DOMAIN + '", "content": "' + ip + '"}'

    # Make a request
    req = requests.post(target,
                        headers=REQ_HEADER,
                        data=request_json
                        )

    # Return the API response
    return req.text


# Sends a GET request to the DNS API
# and fetches all the record data
def api_fetch_dns():
    # Define request parameters
    target = API_URL + zone_id + "/dns_records"

    # Make a request
    req = requests.get(target, headers=REQ_HEADER)

    # Return the API response
    return req.text


# Sends a DELETE request to the DNS API
# and calls it to delete a specific record
def api_drop_dns(record_id):
    # Define request parameters
    target = API_URL + zone_id + "/dns_records/" + record_id

    # Make a request
    req = requests.delete(target,
                          headers=REQ_HEADER
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
@api.route('/create_record', methods=['GET', 'POST'])
def create_record():
    # Parse POST parameters
    data = json.loads(request.data)

    # Initiate a response to the frontend
    internal_response = {
        "success": True,
        "body": "New DNS record created"
    }

    # Return error on empty fields
    if data[0] == "" or data[1] == "" or data[2] == "":
        internal_response["success"] = False
        internal_response["body"] = "All fields are required"
        return json.dumps(internal_response)

    if data[2] != TOKEN:
        internal_response["success"] = False
        internal_response["body"] = "Wrong password"
        return json.dumps(internal_response)

    # Make a POST request
    dns_response = json.loads(api_new_dns(data[0], data[1]))

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


# Record creation path
@api.route('/fetch_records')
def fetch_records():
    # Initiate a response to the frontend
    internal_response = {
        "success": True,
        "body": "",
        "records": {}
    }

    # Make a GET request
    dns_response = json.loads(api_fetch_dns())

    # Handle errors on record creation
    if not dns_response["success"]:
        internal_response["success"] = False
        internal_response["body"] = "Unable to fetch records"
        return json.dumps(internal_response)

    for record in dns_response["result"]:
        internal_response["records"][record["name"]] = [record["content"], record["id"]]

    # Return data to the frontend
    return json.dumps(internal_response)


# Record deletion path
@api.route('/drop_record', methods=['GET', 'POST'])
def drop_record():
    # Parse POST parameters
    data = request.data.decode("utf-8")

    # Initiate a response to the frontend
    internal_response = {
        "success": True,
        "body": "Record successfully removed"
    }

    # Make a DELETE request
    dns_response = json.loads(api_drop_dns(data))

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
