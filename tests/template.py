import unittest
from unittest.mock import patch, Mock
import requests


class MyTestCase(unittest.TestCase):

    # mocking an API call and testing that the response is as expected
    # see article for below structure: https://auth0.com/blog/mocking-api-calls-in-python/
    def test_APICall(self):
        """Mocking a whole function"""
        """
        This is an example of mocking the below function. Will need to be replaced
        when we figure out which function we need to mock
        """
        mock_get_patcher = patch('users.requests.get')
        users = [{
            "id": 0,
            "first_name": "Dell",
            "last_name": "Norval",
            "phone": "994-979-3976"
        }]

        # Start patching 'requests.get'.
        mock_get = mock_get_patcher.start()

        # Configure the mock to return a response with status code 200 and a list of users.
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = users

        # TODO Call the service, which will send a request to the server.
        response = requests.get("URL")

        # Stop patching 'requests'.
        mock_get_patcher.stop()

        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), users)


    # basic test that can be used for testing logic
    def test_something(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
