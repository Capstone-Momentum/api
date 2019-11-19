
from graphene import Schema
import graphql_schema.datausa.economic.query as datausa_economic_query
import graphql_schema.datausa.economic.mutation as datausa_economic_mutation
import graphql_schema.census.acs.query as census_acs_query
import graphql_schema.census.acs.mutation as census_acs_mutation

class RootQuery(datausa_economic_query.Query,
                census_acs_query.Query):
    pass

class RootMutation(datausa_economic_mutation.Mutation,
                   census_acs_mutation.Mutation):
    pass

schema = Schema(query=RootQuery, mutation=RootMutation)

