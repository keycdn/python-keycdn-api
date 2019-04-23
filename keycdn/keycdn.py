import requests
import json


# KeyCDN Python API Client
class Api(object):

    # Constructor takes API Key as param
    def __init__(self, ApiKey, session=None):
        self.__api_key = ApiKey
        self.__endpoint = 'https://api.keycdn.com'
        self.session = requests

    # setter for ApiKey
    def set_api_key(self, ApiKey):
        self.__api_key = ApiKey

    # getter for ApiKey
    def get_api_key(self):
        return self.__api_key

    # setter for endpoint
    def set_endpoint(self, endpoint):
        self.__endpoint = endpoint

    # getter for endpoint
    def get_endpoint(self):
        return self.__endpoint

    '''
        call String
        params Dict
        returns Dict
    '''
    def get(self, call, params={}):
        return self.__execute(call, 'GET', params)

    '''
        call String
        params Dict
        returns Dict
    '''
    def post(self, call, params={}):
        return self.__execute(call, 'POST', params)

    '''
        call String
        params Dict
        returns Dict
    '''
    def put(self, call, params={}):
        return self.__execute(call, 'PUT', params)

    '''
        call String
        params Dict
        returns Dict
    '''
    def delete(self, call, params={}):
        return self.__execute(call, 'DELETE', params)

    '''
        Raises Connection and ValueError
        Returns a Dict
    '''
    def __execute(self, call, method, params):
        url = '{}/{}'.format(self.__endpoint, call)
        r = None
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
