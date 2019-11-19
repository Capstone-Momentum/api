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
This will prompt you to enter an Access Key and a Secret Access key which you can get using your AWS account in the My Security Credentials section of your account. Use `us-east-2` as the default region, and None for the default output format.
In Postman, create a GET request for graphql on your local host via `http://local.host:port/graphql`, and in the body specify a test query for getting data from the backend, for example, `query {acs1Variable(tableName: "census_acs1_detailed", variableName:"B19037E_030E", year: 2018) }`.
