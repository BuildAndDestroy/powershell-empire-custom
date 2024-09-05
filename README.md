# powershell-empire-custom
Customize powershell-empire to exploit kubernetes


# Modules
* Custom modules for Empire

# Standalone Python
* No python on the environment? Compile and upload to your victim
* Build all containers at once:
```
cd python_standalone
./build_python.sh

docker run --rm -it python-builder-<OS>-<version> sh
docker cp <CONTAINER ID>:/tmp/tmp_localpython.tar.gz .
docker stop <CONTAINER ID>
```

# Standalone socat
* Need standalone socat? Build it and copy it out of the container:
```
docker build -t socat-builder-debian-bullseye .
docker run --rm -it -d socat-builder-debian-bullseye bash
docker cp <CONTAINER ID>:/tmp/socat/socat.b64 .
```
Paste the base64 contents into a file on your compromised machine.
Then cat it out back into binary:
```
cat socat.b64 | base64 -d > socat
chmod 755 socat
```

# fileserver
* Use this directory to create a fileserver, share files over https
* Build for k8s but can be converted over for your standard nginx server

# Empire File Structure

If deploying to the kali install, cp the file structure as follows:

```
sudo cp -r ~/git/powershell-empire-custom/modules/usr/share/powershell-empire/empire/ /usr/share/powershell-empire/
```

If deploying using github, then copy the file structure as follows:

```
cp -r ~/git/powershell-empire-custom/modules/usr/share/powershell-empire/empire/ /path/to/Empire/
```


# Disclaimer
* Not responsible for you breaking the law, think before you type.


# Links

## Empire
* https://github.com/BC-SECURITY/Empire

