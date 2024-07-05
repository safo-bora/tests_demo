from api.api_tests.connection.trello_connection import TrelloAPI
from log_lib import logger


class LabelAPI(TrelloAPI):

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
