# Dynamo
Interface for creating DNS records on your own website.  
Currently works just with Cloudflare.

![](https://i.imgur.com/pgih9b8.png)

## Usage

### Depedencies
* flask
* requests

Install the depedencies by executing
```
pip3 install flask requests
```

### Env variables
You have to declare the following environmental variables on your server.
* CFZONE - DNS zone ID
* CFAPI - Cloudflare API key
* CFEMAIL - Cloudflare account email
* DYNOPASS - Custom dynamo password

### Running
Execute the python file with `python3 main.py`.
