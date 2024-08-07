from api.api_tests.connection.config import API_KEY, TOKEN
from api.api_tests.connection.http_connection import HTTPConnection


class TrelloAPI:
    def __init__(self):
        self.http = HTTPConnection("https://api.trello.com/1/")
        self.auth_params = {'key': API_KEY, 'token': TOKEN}
