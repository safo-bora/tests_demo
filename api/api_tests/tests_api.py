from api.api_tests.connection.API.board_api import BoardAPI
from api.api_tests.connection.API.card_api import CardAPI
from api.api_tests.connection.config import BOARD_ID
from api.api_tests.connection.lib import assert_properties
from log_lib import logger


class TestTrelloAPI:
    def setup_method(self):
        """Setup method to initialize TrelloAPI and create a temporary card before each test."""
        logger.info("Setting up test method...")
        self.board_api = BoardAPI()
        self.card_api = CardAPI()

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

    def test_get_board(self):
        board_name = "Test Board Name"
        self.board_api.update_board(BOARD_ID, board_name)
        board = self.board_api.get_board(BOARD_ID)
        expected_props = {'name': board_name, 'closed': False, 'voting': 'disabled'}
        assert_properties(board, expected_props)

    def test_update_board_name(self):
        new_name = "New Board Name"
        updated_board_info = self.board_api.update_board(BOARD_ID, new_name)
        assert updated_board_info.name == new_name, f"Board name was not updated to '{new_name}'"

    def test_delete_card(self):
        # Delete the card
        deleted_card_info = self.card_api.delete_card(self.card_id)
        assert deleted_card_info is not None, "Card deletion failed"
        assert 'limits' in deleted_card_info, "Deleted card info does not contain 'limits' key"

        # Fetch cards after deletion
        updated_cards = self.board_api.fetch_lists(BOARD_ID)

        # Verify that the deleted card is no longer in the list of cards
        deleted_card_ids = [card.id for card in updated_cards.lists]
        assert self.card_id not in deleted_card_ids, "Card was not deleted"
