import pytest
import requests
import json

from api.api_tests.config import BOARD_ID, API_KEY, TOKEN

BASE_URL = "https://api.trello.com/1/"


class TestTrelloAPI:
    card_id: str

    @pytest.fixture(scope="class", autouse=True)
    def setup_card(self, request):
        """Fixture to create and delete a card for testing, attached to the class instance."""
        # Fetch lists or create a new list if none exist
        lists_url = f"{BASE_URL}boards/{BOARD_ID}/lists?key={API_KEY}&token={TOKEN}"
        response = requests.get(lists_url)
        lists = response.json()
        if not lists:
            # Create a new list if no lists are available
            create_list_url = f"{BASE_URL}boards/{BOARD_ID}/lists?key={API_KEY}&token={TOKEN}&name=New List"
            list_response = requests.post(create_list_url)
            list_id = list_response.json()['id']
        else:
            list_id = lists[0]['id']

        # Create a card
        create_card_url = f"{BASE_URL}cards?key={API_KEY}&token={TOKEN}&idList={list_id}&name=Temporary Card"
        card_response = requests.post(create_card_url)
        if card_response.status_code != 200:
            pytest.fail("Failed to create a card, cannot proceed with api_tests.")

        # Attach the card_id to the class instance for use in api_tests
        request.cls.card_id = card_response.json()['id']
        yield
        # Delete the card after api_tests
        delete_card_url = f"{BASE_URL}cards/{request.cls.card_id}?key={API_KEY}&token={TOKEN}"
        requests.delete(delete_card_url)

    def test_get_board(self):
        """Test to fetch details of a specific board and verify key fields in the response."""
        url = f"{BASE_URL}boards/{BOARD_ID}?key={API_KEY}&token={TOKEN}"
        response = requests.get(url)
        assert response.status_code == 200
        data = response.json()

        # Verify the 'id' and 'name' are as expected (assuming you know the expected name)
        expected_name = "Updated Name"
        assert data['name'] == expected_name, "Board name does not match expected"

        # Verify additional properties to ensure the full response is as expected
        assert data['closed'] == False, "Board should not be closed"
        assert data['prefs']['permissionLevel'] == 'org', "Permission level should be 'org'"
        assert data['prefs']['voting'] == 'disabled', "Voting should be disabled"
        assert data['prefs']['comments'] == 'members', "Comments permissions should be for members"
        assert data['prefs']['selfJoin'] == True, "Self-join should be enabled"
        assert data['prefs']['cardCovers'] == True, "Card covers should be enabled"
        assert data['prefs']['background'] == 'gradient-crystal', "Background should be 'gradient-crystal'"

        # Optionally verify more complex structures like label names or prefs
        assert not any(data['labelNames'].values()), "Label names should be empty"

    def test_update_board_name(self):
        """Test to update a board's name."""
        url = f"{BASE_URL}boards/{BOARD_ID}?name=Updated Name&key={API_KEY}&token={TOKEN}"
        response = requests.put(url)
        assert response.status_code == 200
        assert response.json()['name'] == 'Updated Name'

    def test_delete_card(self):
        """Test to delete a specific card."""
        url = f"{BASE_URL}cards/{self.card_id}?key={API_KEY}&token={TOKEN}"
        response = requests.delete(url)
        assert response.status_code == 200
        response_data = json.loads(response.text)
        # Ensure that if there is content, it's only the 'limits' key
        if response_data:  # Check if the dictionary is not empty
            assert response_data.keys() == {'limits'}, f"Unexpected response content: {response.text}"
