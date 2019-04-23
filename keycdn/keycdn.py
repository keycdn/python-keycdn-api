import requests
import json


class Api(object):
    """KeyCDN Python API Client"""

    def __init__(self, ApiKey):
        self.__api_key = ApiKey
        self.__endpoint = 'https://api.keycdn.com'
        self.session = requests

    def set_api_key(self, ApiKey):
        """setter for ApiKey

        Args:
            ApiKey (str): The API key.
        """
        self.__api_key = ApiKey

    def get_api_key(self):
        """getter for ApiKey

        Returns:
            str: The current API key
        """
        return self.__api_key

    def set_endpoint(self, endpoint):
        """setter for endpoint

        Args:
            ApiKey (str): The API key.
        """
        self.__endpoint = endpoint

    def get_endpoint(self):
        """getter for endpoint

        Returns:
            str: The current API key
        """
        return self.__endpoint

    def get(self, call, params={}):
        """Make a GET call.

        Args:
            call (str): API endpoint
            params (dict): Additional parameters.

        Returns:
            dict: Result of API call.
        """
        return self.__execute(call, 'GET', params)

    def post(self, call, params={}):
        """Make a POST call.

        Args:
            call (str): API endpoint
            params (dict): Additional parameters.

        Returns:
            dict: Result of API call.
        """
        return self.__execute(call, 'POST', params)


    def put(self, call, params={}):
        """Make a PUT call.

        Args:
            call (str): API endpoint
            params (dict): Additional parameters.

        Returns:
            dict: Result of API call.
        """
        return self.__execute(call, 'PUT', params)

    def delete(self, call, params={}):
        """Make a DELETE call.

        Args:
            call (str): API endpoint
            params (dict): Additional parameters.

        Returns:
            dict: Result of API call.
        """
        return self.__execute(call, 'DELETE', params)

    def __execute(self, call, method, params):
        url = '{}/{}'.format(self.__endpoint, call)
        if method == 'GET':
            r = self.session.get(url, auth=(self.__api_key, ''), data=params)
        elif method == 'POST':
            r = self.session.post(url, auth=(self.__api_key, ''), data=params)
        elif method == 'PUT':
            r = self.session.put(url, auth=(self.__api_key, ''), data=params)
        elif method == 'DELETE':
            r = self.session.delete(url, auth=(self.__api_key, ''), json=params)
        else:
            raise ValueError('Only the methods GET, POST, PUT, DELETE are supported.')

        return r.json()
