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
CFAPI=
CFZONE=
CFDOMAIN=
CFEMAIL=
DYNOPASS=
```
3. Start a container based on your new Dynamo image.
```
docker run --name dynamo --env-file .env -p 8003:8003 --rm dynamo
```
4. Open the Dynamo dashboard.
```
http://localhost:8003
```

### Env variables
Dynamo uses the following environmental variables.
* CFAPI - Cloudflare API key
* CFZONE - DNS zone ID
* CFDOMAIN - Your domain on CloudFlare
* CFEMAIL - Cloudflare account email
* DYNOPASS - Custom dynamo password

### HTTPS and port 80
Dynamo runs by default on port `8003`. The Docker configuration reveals that port and you can access the dashboard at `http://localhost:8003`.
The Docker image can be used for production but usually you may want to enable HTTPS and serve the dashboard on port `80`.

You will need to setup a proxy with either Nginx or Apache 2 to point traffic from port `80` to Dynamo's port `8003`.
By doing this, you can also issue a SSL/TLS certificate on your site and enable HTTPS.

#### Example Nginx configuration
```
server {
    listen 80;
    ...
    location / {
        proxy_pass http://127.0.0.1:8003;
    }
    ...
}
```

## Links
Read about CloudFlare API: https://api.cloudflare.com/
