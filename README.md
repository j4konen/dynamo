# Dynamo
Interface for creating DNS records on your own website.  
Works with Cloudflare.

![](https://i.imgur.com/pgih9b8.png)

## Usage

### Docker
This project ships with a Dockerfile. You can deploy Dynamo on your server with Docker.

1. Clone the repo and build the image.
```
git clone https://github.com/sjaks/dynamo.git
cd dynamo/container
docker build -t dynamo .
```
2. Edit the `.env` file. Edit in your desired Dynamo password and information from CloudFlare.
```
$ nano .env
CFAPI=0000000000000000000000000000000000000
CFZONE=00000000000000000000000000000000
CFDOMAIN=example.com
CFEMAIL=email@example.com
DYNOPASS=password
```
3. Start a container based on your new Dynamo image.
```
docker run --name dynamo --env-file .env -p 8003:8003 --rm dynamo
```
4. Open the Dynamo dashboard.
```
http://localhost:8003
```

### Without Docker

#### Depedencies
If you don't want to use Docker, install the depedencies by executing
```
pip3 install flask requests
```

#### Env variables
You have to set the following environmental variables on your server.
* CFAPI - Cloudflare API key
* CFZONE - DNS zone ID
* CFDOMAIN - Your domain on CloudFlare
* CFEMAIL - Cloudflare account email
* DYNOPASS - Custom dynamo password

Set them on your server:
```
export CFAPI='0000000000000000000000000000000000000'
export CFZONE='00000000000000000000000000000000'
export CFDOMAIN='example.com'
export CFEMAIL='email@example.com'
export DYNOPASS='password'
```

#### Running
Execute the python file with `python3 main.py`. If you are using this in a production setting, disable dev mode and use Apache2 or Nginx to proxy traffic to Dynamo's port 8003. Be sure to use a strong DYNOPASS password.

## Links
Read about CloudFlare API: https://api.cloudflare.com/
