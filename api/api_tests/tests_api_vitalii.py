import random

from api.api_tests.connection.API.board_api import BoardAPI
from api.api_tests.connection.API.card_api import CardAPI
from api.api_tests.connection.API.label_api import LabelAPI
from api.api_tests.connection.config import BOARD_ID
from log_lib import logger


class TestTrelloAPI:
    def setup_method(self):
        """Setup method to initialize TrelloAPI and create a temporary card before each test."""
        logger.info("Setting up test method...")
        self.board_api = BoardAPI()
        self.card_api = CardAPI()
        self.label_api = LabelAPI()

        lists = self.board_api.fetch_lists(BOARD_ID)
        list_id = lists.lists[0].id if lists else self.board_api.create_list(BOARD_ID, "New List").id
        card_info = self.card_api.create_card(list_id, "Temporary Card")
        self.card_id = card_info.id
        logger.info(f"Temporary card created with ID: {self.card_id}")

    def teardown_method(self):
        """Teardown method to delete the temporary card after each test."""
        logger.info("Tearing down test method...")
        self.card_api.delete_card(self.card_id)
        logger.info("Temporary card deleted successfully.")

    def test_get_membership_of_board(self):
        memberships = self.board_api.get_memberships_of_board(BOARD_ID)
        expected_fields = ['id', 'idMember', 'memberType', 'unconfirmed', 'deactivated']
        for field in expected_fields:
            assert field in memberships.json[0], f"The field : {field} not in the response"

    def test_get_actions_of_board(self):
        new_name = "Test get action"
        self.board_api.update_board(BOARD_ID, new_name)
        actions = self.board_api.get_actions_of_board(BOARD_ID)
        # Check that board name changed in the last action
        assert actions.actions_list[0].board_name == new_name, "Wrong last action"

    def test_get_card_on_board(self):
        card_info = self.board_api.get_card_on_board(BOARD_ID, self.card_id)
        assert card_info.name == "Temporary Card"

    def test_get_cards_on_board(self):
        cards = self.board_api.get_cards_on_board(BOARD_ID)
        assert len(cards.cards) > 0, "There are should be at least one card"

        # Check that new card is on the bord
        cards_ids = list(card.id for card in cards.cards)
        assert self.card_id in cards_ids

    def test_create_label(self):
        color = random.choice(("red", "green", "blue"))
        label = self.board_api.create_label_on_board(board_id=BOARD_ID, color=color)

        assert label.color == color, f"Wrong color : {label.color} should be : {color}"

        # TODO add а correct way to clean up test data
        self.label_api.delete_label(label.id)

    def test_delete_label(self):
        label_id = self.board_api.create_label_on_board(board_id=BOARD_ID).id

        labels_before = self.board_api.get_labels_on_board(BOARD_ID)

        self.label_api.delete_label(label_id)
        labels_after = self.board_api.get_labels_on_board(BOARD_ID)

        assert len(labels_after.labels_list) < len(labels_before.labels_list), "Amount of labels didn't change"
        for label in labels_after.labels_list:
            assert label.id != label_id, "Label didn't delete"
