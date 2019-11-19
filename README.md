## Setting Up the API

### Initial Steps
On Windows, we recommend you install Git Bash via https://gitforwindows.org/.

On Mac, we recommend you install Homebrew via https://brew.sh/, then you can run `brew install git`.

All machines should have the latest version of Python installed via https://www.python.org/downloads/.

### Clone this repo
`git clone https://github.com/Capstone-Momentum/api.git`

### Install requirements file
`pip3 install -r requirements.txt`

### Run Flask app
`flask run`

If `flask run` gives you an error saying that it cannot find a Flask App, run this command in bash (mac): `export FLASK_APP=application.py` or this command using cmd (windows): `set FLASK_APP=application.py`.

### Ensure that you can make a request
Download Postman via https://www.getpostman.com/downloads/

Or, download GraphIQL via Homebrew and run `brew cask install graphiql`, or for Windows by clicking on this link: https://github.com/skevy/graphiql-app/releases/download/v0.7.2/GraphiQL-0.7.2.dmg.

Run `pip3 install awscli`

Run `aws configure`

This will prompt you to enter an Access Key and a Secret Access key which you can get using your AWS account in the My Security Credentials section of your account. Use `us-east-2` as the default region, and None for the default output format.

In Postman, create a GET request for graphql on your local host via `http://local.host:port/graphql`, and in the body specify a test query for getting data from the backend, for example, `query {acs1Variable(tableName: "census_acs1_detailed", variableName:"B19037E_030E", year: 2018) }`.

In GraphIQL, specify the grapql route: `http://local.host:port/graphql`, and you can query data using a query string, such as: `query {acs1Variable(tableName: "census_acs1_detailed", variableName:"B19037E_030E", year: 2018) }` and then clicking the play button in the upper left corner of the screen. 
