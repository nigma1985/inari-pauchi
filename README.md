# inari-pauchi
[Pauchi Kamuy](https://en.wikipedia.org/wiki/Pauchi_Kamuy) is the Ainu kamuy (god) of *insanity*.

[Inari Ōkami](https://en.wikipedia.org/wiki/Inari_%C5%8Ckami) is the Japanese kami of *foxes*, *fertility*, *rice*, *tea* and *sake*, of *agriculture* and *industry*, of *general prosperity* and *worldly success*, and one of the *principal kami* of Shinto.

-----------------------------

## Prerequisits
Run this web application on a linux distribution (developped on Debian)

Please provide a ```/global_config.json``` file with the following structure:
- main_db
  - host
- django
  - SECRET_KEY
  - DEBUG (```true```/```false```)
- mail
  - mail
  - host
  - port
  - TLS (```true```/```false```)
  - user
  - password

Initiate a virtual environment:
- ```python3 -m venv env```
- ```source venv/bin/activate```
- ```pip install -r requirements.txt```

Please run ```python3 manage.py makemigrations``` and ```python3 manage.py migrate``` before starting the server