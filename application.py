from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from graphql_schema.root import schema

application = Flask(__name__)
application.secret_key = 'Aahmt5LJHAh0kO+e22wach1sdmOpqMl5MOwQwVUB'
CORS(application)
application.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

@application.route("/")
def hello_world():
    return "Hello world"

@application.route("/test")
def test_world():
    return "Test"

