# Configs

## fileserver.dockerfile
* Update "yourdomain.com" to your real domain
* Add an A record to your zone file for "fileshare.yourdomain.com"

## fileshare.yourdomain.com.conf
* Change this file to match what you put in the fileserver.dockerfile
* Update the fileshare.yourdomain.com within the file to match what you put in fileserver.dockerfile

## full_deployment.yaml
* Update the .dockerconfigjson entry
* Add your real domain that matches the fileserver.dockerfile
