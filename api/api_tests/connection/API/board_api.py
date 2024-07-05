from api.api_tests.connection.lib import Board
from api.api_tests.connection.trello_connection import TrelloAPI
from log_lib import logger


class BoardAPI(TrelloAPI):
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

    def update_board(self, board_id, new_name):
        params = {'name': new_name, **self.auth_params}
        response = self.http.put(f"boards/{board_id}", params=params)
        response.raise_for_status()
        # TODO: Return board object, not json
        return response.json()

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