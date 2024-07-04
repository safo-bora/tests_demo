import random

from api.api_tests.connection.trello_connection import TrelloAPI
from api.api_tests.connection.config import BOARD_ID
from log_lib import logger


class TestTrelloAPI:
    def setup_method(self):
        """Setup method to initialize TrelloAPI and create a temporary card before each test."""
        logger.info("Setting up test method...")
        self.trello_api = TrelloAPI()
        lists = self.trello_api.fetch_lists(BOARD_ID)
        list_id = lists[0]['id'] if lists else self.trello_api.create_list(BOARD_ID, "New List")['id']
        card_info = self.trello_api.create_card(list_id, "Temporary Card")
        self.card_id = card_info['id']
        logger.info(f"Temporary card created with ID: {self.card_id}")

    def teardown_method(self):
        """Teardown method to delete the temporary card after each test."""
        logger.info("Tearing down test method...")
        self.trello_api.delete_card(self.card_id)
        logger.info("Temporary card deleted successfully.")

    def test_get_membership_of_board(self):
        memberships = self.trello_api.get_membership_of_board(BOARD_ID)
        expected_fields = ['id', 'idMember', 'memberType', 'unconfirmed', 'deactivated']
        for field in expected_fields:
            assert field in memberships[0], f"The field : {field} not in the response"

    def test_get_actions_of_board(self):
        new_name = "Test get action"
        self.trello_api.update_board(BOARD_ID, new_name)
        actions = self.trello_api.get_actions_of_board(BOARD_ID)
        # Check that board name changed in the last action
        assert actions[0]["data"]["board"]["name"] == new_name, "Wrong last action"

    def test_get_card_on_board(self):
        card_info = self.trello_api.get_card_on_board(BOARD_ID, self.card_id)
        assert card_info["name"] == "Temporary Card"

    def test_get_cards_on_board(self):
        cards = self.trello_api.get_cards_on_board(BOARD_ID)
        assert len(cards) > 0, "There are should be at least one card"
        assert cards[-1]["id"] == self.card_id

    def test_create_label(self):
        color = random.choice(("red", "green", "blue"))
        label = self.trello_api.create_label_on_board(board_id=BOARD_ID, color=color)

        assert label["color"] == color, f"Wrong color : {label["color"]} should be : {color}"

        # TODO add а correct way to clean up test data
        self.trello_api.delete_label(label["id"])

    def test_delete_label(self):
        label_id = self.trello_api.create_label_on_board(board_id=BOARD_ID)["id"]

        labels_before = self.trello_api.get_label_on_board(BOARD_ID)

        self.trello_api.delete_label(label_id)
        labels_after = self.trello_api.get_label_on_board(BOARD_ID)

        assert len(labels_after) < len(labels_before), "Amount of labels didn't change"
        for label in labels_after:
            assert label["id"] != label_id, "Label didn't delete"



