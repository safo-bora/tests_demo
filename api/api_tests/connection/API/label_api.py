from api.api_tests.connection.lib import Label
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
            raise Exception

    def create_label(self, id_board, label_name="Test name", color="red"):
        params = {
            'name': label_name,
            'color': color,
            'idBoard': id_board,
            **self.auth_params
        }
        response = self.http.post("labels", params=params)
        print(response)
        response.raise_for_status()
        label_data = response.json()
        return Label(label_data)

    def get_label(self, label_id):
        response = self.http.get(f"labels/{label_id}", params=self.auth_params)
        response.raise_for_status()
        label_data = response.json()
        return Label(label_data)

    def update_label(self, label_id, new_name):
        params = {'name': new_name, **self.auth_params}
        response = self.http.put(f"labels/{label_id}", params=params)
        response.raise_for_status()
        updated_label_data = response.json()
        return Label(updated_label_data)

    def update_field_on_a_label(self, label_id, field_id, value):
        params = {'value': value, **self.auth_params}
        response = self.http.put(f"labels/{label_id}/{field_id}", params=params)
        response.raise_for_status()
        updated_field_data = response.json()
        return updated_field_data
