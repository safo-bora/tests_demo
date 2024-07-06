from api.api_tests.connection.lib import Board, BoardList, Card, Label, Membership, Action
from api.api_tests.connection.trello_connection import TrelloAPI


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
        list_data = response.json()
        return BoardList(list_data)

    def update_board(self, board_id, new_name):
        params = {'name': new_name, **self.auth_params}
        response = self.http.put(f"boards/{board_id}", params=params)
        response.raise_for_status()
        updated_board_data = response.json()
        return Board(updated_board_data)

    def fetch_lists(self, board_id):
        response = self.http.get(f"boards/{board_id}/lists", params=self.auth_params)
        response.raise_for_status()
        lists_data = response.json()
        return BoardList(lists_data)

    def get_memberships_of_board(self, board_id):
        response = self.http.get(f"boards/{board_id}/memberships", params=self.auth_params)
        response.raise_for_status()
        memberships_data = response.json()
        return Membership(memberships_data)

    def get_actions_of_board(self, board_id):
        response = self.http.get(f"boards/{board_id}/actions", params=self.auth_params)
        response.raise_for_status()
        actions_data = response.json()
        return Action(actions_data)

    def get_card_on_board(self, board_id, card_id):
        response = self.http.get(f"boards/{board_id}/cards/{card_id}", params=self.auth_params)
        response.raise_for_status()
        card_data = response.json()
        return Card(card_data)

    def get_cards_on_board(self, board_id):
        response = self.http.get(f"boards/{board_id}/cards", params=self.auth_params)
        response.raise_for_status()
        card_data = response.json()
        return Card(card_data)

    def get_labels_on_board(self, board_id):
        response = self.http.get(f"boards/{board_id}/labels", params=self.auth_params)
        response.raise_for_status()
        labels_data = response.json()
        return Label(labels_data)

    def create_label_on_board(self, board_id, label_name="Test_label", color=None):
        params = {'name': label_name, "color": color, **self.auth_params}
        response = self.http.post(f"boards/{board_id}/labels", params=params)
        response.raise_for_status()
        label_data = response.json()
        return Label(label_data)
