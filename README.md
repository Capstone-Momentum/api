## Setting Up the API

### Install requirements file
`pip3 install -r requirements.txt`

### Run Flask app
`flask run`

If `flask run` gives you an error saying that it cannot find a Flask App, run this command in bash (mac): `export FLASK_APP=application.py` or this command using cmd (windows): `set FLASK_APP=application.py`.

### Make a request
Download Postman or GraphIQL
Run `pip3 install awscli`
Run `aws configure`
This will prompt you to enter an Access Key and a Secret Access key which you can get using your AWS account in the My Security Credentials section of your account. 
