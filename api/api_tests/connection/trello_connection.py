from log_lib import logger
from api.api_tests.connection.config import API_KEY, TOKEN
from api.api_tests.connection.http_connection import HTTPConnection
from api.api_tests.connection.lib import Board


class TrelloAPI:
    def __init__(self):
        self.http = HTTPConnection("https://api.trello.com/1/")
        self.auth_params = {'key': API_KEY, 'token': TOKEN}

    def get_board(self, board_id):
        response = self.http.get(f"boards/{board_id}", params=self.auth_params)
        response.raise_for_status()
        board_data = response.json()
        return Board(board_data)

    def create_list(self, board_id, list_name='New List'):
        params = {'name': list_name, **self.auth_params}
        response = self.http.post(f"boards/{board_id}/lists", params=params)
        response.raise_for_status()
        # TODO: Return list object, not json
        return response.json()

    def create_card(self, list_id, card_name='Temporary Card'):
        params = {'idList': list_id, 'name': card_name, **self.auth_params}
        response = self.http.post("cards", params=params)
        response.raise_for_status()
        # TODO: Return card object, not json
        return response.json()

    def update_board(self, board_id, new_name):
        params = {'name': new_name, **self.auth_params}
        response = self.http.put(f"boards/{board_id}", params=params)
        response.raise_for_status()
        # TODO: Return board object, not json
        return response.json()

    def delete_card(self, card_id):
        response = self.http.delete(f"cards/{card_id}", params=self.auth_params)
        if response.status_code == 200:
            logger.info("Card deleted successfully")
            return response.json()
        elif response.status_code == 404:
            logger.warning(f"Card with ID {card_id} not found")
        else:
            logger.error(f"Error deleting card: {response.status_code} - {response.text}")
        return None

    def fetch_lists(self, board_id):
        response = self.http.get(f"boards/{board_id}/lists", params=self.auth_params)
        response.raise_for_status()
        # TODO: Return collection, not json
        return response.json()

    def get_membership_of_board(self, board_id):
        response = self.http.get(f"boards/{board_id}/memberships", params=self.auth_params)
        response.raise_for_status()
        # TODO: Return collection, not json
        return response.json()

    def get_actions_of_board(self, board_id):
        response = self.http.get(f"boards/{board_id}/actions", params=self.auth_params)
        response.raise_for_status()
        # TODO: Return collection, not json
        return response.json()

    def get_card_on_board(self, board_id, card_id):
        response = self.http.get(f"boards/{board_id}/cards/{card_id}", params=self.auth_params)
        response.raise_for_status()
        # TODO: Return collection, not json
        return response.json()

    def get_cards_on_board(self, board_id):
        response = self.http.get(f"boards/{board_id}/cards", params=self.auth_params)
        response.raise_for_status()
        # TODO: Return collection, not json
        return response.json()

    def get_label_on_board(self, board_id):
        response = self.http.get(f"boards/{board_id}/labels", params=self.auth_params)
        response.raise_for_status()
        # TODO: Return collection, not json
        return response.json()

    def create_label_on_board(self, board_id, label_name="Test_label", color=None):
        params = {'name': label_name, "color": color, **self.auth_params}
        response = self.http.post(f"boards/{board_id}/labels", params=params)
        response.raise_for_status()
        # TODO: Return card object, not json
        return response.json()

    def delete_label(self, label_id):
        response = self.http.delete(f"labels/{label_id}", params=self.auth_params)
        if response.status_code == 200:
            logger.info("Label deleted successfully")
            return response.json()
        elif response.status_code == 404:
            logger.warning(f"Label with ID {label_id} not found")
        else:
            logger.error(f"Error deleting label: {response.status_code} - {response.text}")
        return None


