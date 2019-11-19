
from graphene import InputObjectType, Mutation, String, Boolean, ObjectType

class EconomicDataInput(InputObjectType):
    an_input_field = String(required=True)
    another_input_field = String(required=True)

class EconomicDataMutation(Mutation):
    class Arguments:
        mutation_input = EconomicDataInput(required=True)

    ok = Boolean()
    data = String()
    error = String()

    @staticmethod
    def mutate(parent, info, mutation_input):
        an_input_field = mutation_input.an_input_field
        another_input_field = mutation_input.another_input_field
        try:
            database_query_results = 'normally a result set from a query'
            return EconomicDataMutation(ok=True, data=database_query_results, error=None)
        except Exception as e:
            # Log an error (we'll need to discuss a logging system)
            return EconomicDataMutation(ok=False, data=None, error=str(e))

class Mutation(ObjectType):
    example = EconomicDataMutation.Field()

