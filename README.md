# qxn
* Question and Answer django app.

# Installation
* Clone this repo into virtual env
* Install dependencies: `pip install -r requirements.txt`
* Add your custom configuration in `qxn/custom.py`
* Configure your database, or skip it for sqlite
* Run migration: `./manage.py migrate`
* Run server `make run` or `make run2`

## Features
- [x] Includes production-ready WSGI/HTTP server ([bjoern](https://github.com/jonashaag/bjoern)).
- [x] Python 3 ONLY.
- [] Vuejs.

## WSGI/HTTP Server
To use the included WSGI/HTTP server do as follows:
* Activate virtual env
* Run `./server.py` for example: 
* `./server.py` #will run the server by default on localhost:8000
* `./server.py -u /tmp/qxn.sock` # will run the server on unix socket (make since when used behind reverse proxy like nginx).

## License
* Read LICENSE.


