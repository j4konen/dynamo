# Dynamo
Interface for creating DNS records on your own website.  
Works with Cloudflare.

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
You have to set the following environmental variables on your server.
* CFAPI - Cloudflare API key
* CFZONE - DNS zone ID
* CFDOMAIN - Your domain on CloudFlare
* CFEMAIL - Cloudflare account email
* DYNOPASS - Custom dynamo password

### Running
Set environmental variables on your server:
```
export CFAPI='0000000000000000000000000000000000000'
export CFZONE='00000000000000000000000000000000'
export CFDOMAIN='example.com'
export CFEMAIL='email@example.com'
export DYNOPASS='password'
```

Execute the python file with `python3 main.py`. If you are using this in a production setting, disable dev mode and use Apache2 or Nginx to proxy traffic to Dynamo's port 8003. Be sure to use a strong DYNOPASS password.

## Links
Read about CloudFlare API: https://api.cloudflare.com/
