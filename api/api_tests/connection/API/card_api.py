from api.api_tests.connection.lib import Card
from api.api_tests.connection.trello_connection import TrelloAPI
from log_lib import logger


class CardAPI(TrelloAPI):

    def create_card(self, list_id, card_name='Temporary Card'):
        params = {'idList': list_id, 'name': card_name, **self.auth_params}
        response = self.http.post("cards", params=params)
        response.raise_for_status()
        card_data = response.json()
        return Card(card_data)

    def delete_card(self, card_id):
        response = self.http.delete(f"cards/{card_id}", params=self.auth_params)
        if response.status_code == 200:
            logger.info("Card deleted successfully")
            return response.json()
        elif response.status_code == 404:
            logger.warning(f"Card with ID {card_id} not found")
        else:
            logger.error(f"Error deleting card: {response.status_code} - {response.text}")
            raise Exception
