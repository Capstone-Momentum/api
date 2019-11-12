
from graphene import Schema
import graphql_schema.datausa.economic.query as datausa_economic_data_query
import graphql_schema.datausa.economic.mutation as datausa_economic_data_mutation

class RootQuery(datausa_economic_data_query.Query):
    pass

class RootMutation(datausa_economic_data_mutation.Mutation):
    pass

schema = Schema(query=RootQuery, mutation=RootMutation)

