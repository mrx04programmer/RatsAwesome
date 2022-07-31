# Rats Awesome
## Pre - Requisites
| Nombre | Descarga|
|-----------|---|
| python3.7 | [python.org](https://www.python.org/)

* Install requisites for python:
> python3.7 -m pip install -r requirements.txt

## Execute
* Seeing the parameters of the software:
> python3 Rat_Awesome -h
```
usage: Rat_Awesome.py [-h] [-i IP] [-p PORT] [-c CREATE] [-l LISTENER] [-msf METASPLOITCREATE]

optional arguments:
  -h, --help            show this help message and exit
  -i IP, --ip IP        Set IP Localhost
  -p PORT, --port PORT  Set Port of IP Objetive
  -c CREATE, --create CREATE
                        Create file evil with lines scripts backdoor python (set namefile)
  -l LISTENER, --listener LISTENER, --listen LISTENER
                        Start Server waiting victims (set port listener)
  -msf METASPLOITCREATE, --metasploitcreate METASPLOITCREATE
                        Create file RC auto of Metasploit (set namefile & port)
```


* Creating file evil with RatAwesome:
[![asciicast](https://asciinema.org/a/0Bf3sq3OqA2kNxyld42anFMPo.svg)](https://asciinema.org/a/0Bf3sq3OqA2kNxyld42anFMPo)

* Creating the server for the backdoor in the device
[![asciicast](https://asciinema.org/a/GtzLWVSfVPYuWMVC9xLpH7tY7.svg)](https://asciinema.org/a/GtzLWVSfVPYuWMVC9xLpH7tY7)

* Generating the file metasploit RC and show the content
[![asciicast](https://asciinema.org/a/NLoijoPRVFUv6OnfJSLHnX4gE.svg)](https://asciinema.org/a/NLoijoPRVFUv6OnfJSLHnX4gE)

