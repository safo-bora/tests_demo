import unittest
from unittest.mock import patch
from trello_api import get_action_details, update_action, delete_action


class TestTrelloAPI(unittest.TestCase):

    @patch('trello_api.requests.get')
    def test_get_action_details(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'id': 'action_id', 'type': 'commentCard'}

        action_id = 'action_id'
        result = get_action_details(action_id)
        self.assertIsNotNone(result)
        self.assertEqual(result['id'], action_id)

    @patch('trello_api.requests.put')
    def test_update_action(self, mock_put):
        mock_put.return_value.status_code = 200
        mock_put.return_value.json.return_value = {'id': 'action_id', 'text': 'Updated text'}

        action_id = 'action_id'
        new_text = 'Updated text'
        result = update_action(action_id, new_text)
        self.assertIsNotNone(result)
        self.assertEqual(result['text'], new_text)

    @patch('trello_api.requests.delete')
    def test_delete_action(self, mock_delete):
        mock_delete.return_value.status_code = 200

        action_id = 'action_id'
        result = delete_action(action_id)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
