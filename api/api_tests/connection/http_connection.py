import requests
from log_lib import logger


class HTTPConnection:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"Sending GET request to {url} with params: {params}")
        response = requests.get(url, params=params)
        logger.info(f"Received response from {url}: {response.status_code}")
        return response

    def post(self, endpoint, data=None, json=None, params=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"Sending POST request to {url} with data: {data}, json: {json}, params: {params}")
        response = requests.post(url, data=data, json=json, params=params)
        logger.info(f"Received response from {url}: {response.status_code}")
        return response

    def put(self, endpoint, data=None, params=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"Sending PUT request to {url} with data: {data}, params: {params}")
        response = requests.put(url, data=data, params=params)
        logger.info(f"Received response from {url}: {response.status_code}")
        return response

    def delete(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"Sending DELETE request to {url} with params: {params}")
        response = requests.delete(url, params=params)
        logger.info(f"Received response from {url}: {response.status_code}")
        return response
