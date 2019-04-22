import requests
import json


class Api(object):
    """KeyCDN Python API Client"""

    def __init__(self, ApiKey):
        self.__api_key = ApiKey
        self.__endpoint = 'https://api.keycdn.com'

    def set_api_key(self, ApiKey):
        """setter for ApiKey"""
        self.__api_key = ApiKey

    def get_api_key(self):
        """getter for ApiKey"""
        return self.__api_key

    def set_endpoint(self, endpoint):
        """setter for endpoint"""
        self.__endpoint = endpoint

    def get_endpoint(self):
        """getter for endpoint"""
        return self.__endpoint

    def get(self, call, params={}):
        """
            call String
            params Dict
            returns Dict
        """
        return self.__execute(call, 'GET', params)

    def post(self, call, params={}):
        """
            call String
            params Dict
            returns Dict
        """
        return self.__execute(call, 'POST', params)


    def put(self, call, params={}):
        """
            call String
            params Dict
            returns Dict
        """
        return self.__execute(call, 'PUT', params)

    def delete(self, call, params={}):
        """
            call String
            params Dict
            returns Dict
        """
        return self.__execute(call, 'DELETE', params)

    def __execute(self, call, method, params):
        """
            Raises Connection and ValueError
            Returns a Dict
        """
        url = '{}/{}'.format(self.__endpoint, call)
        r = None
        if method == 'GET':
            r = requests.get(url, auth=(self.__api_key, ''), data=params)
        elif method == 'POST':
            r = requests.post(url, auth=(self.__api_key, ''), data=params)
        elif method == 'PUT':
            r = requests.put(url, auth=(self.__api_key, ''), data=params)
        elif method == 'DELETE':
            r = requests.delete(url, auth=(self.__api_key, ''), data=params)
        else:
            raise ValueError('Only the methods GET, POST, PUT, DELETE are supported.')

        return r.json()
