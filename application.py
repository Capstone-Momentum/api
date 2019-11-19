from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from graphql_schema.root import schema
from os import environ

application = Flask(__name__)
CORS(application)
application.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
environ['AWS_ACCESS_KEY_ID'] = 'AKIA2QNHZYF3UP4HMEXZ'
environ['AWS_SECRET_ACCESS_KEY'] = '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'

@application.route("/")
def hello_world():
    return "Hello world"
