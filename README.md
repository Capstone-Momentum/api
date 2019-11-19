## Setting Up the API

### Install requirements file
`pip3 install -r requirements.txt`

### Run Flask app
`flask run`

If `flask run` gives you an error saying that it cannot find a Flask App, run this command in bash (mac): `export FLASK_APP=application.py` or this command using cmd (windows): `set FLASK_APP=application.py`.

In order to check that your back-end is working, download Postman or GraphIQL and send a GET request to your locally hosted Flask App
