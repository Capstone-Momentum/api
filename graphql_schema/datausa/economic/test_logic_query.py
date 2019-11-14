
import unittest
from graphql_schema.datausa.economic.query import Query

class TestDataUSAEconomicQuery(unittest.TestCase):
    def test_resolve_name(self):
        self.assertEqual('DataUSA Economic Data Can Be Returned Here', Query.resolve_name(None, None))

