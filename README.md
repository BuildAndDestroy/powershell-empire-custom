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


# Disclaimer
* Not responsible for you breaking the law, think before you type.


# Links

## Empire
* https://github.com/BC-SECURITY/Empire

