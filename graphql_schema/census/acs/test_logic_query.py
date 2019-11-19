
import unittest
from graphql_schema.datausa.economic.query import Query

class TestCesusACSQuery(unittest.TestCase):
    def test_resolve_something(self):
        self.assertEqual('something', Query.resolve_name(None, None))

