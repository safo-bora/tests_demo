import unittest
import requests
from unittest.mock import patch
from app.calculator_service import fetch_calculation_from_web


class TestCalculatorWebFetch(unittest.TestCase):

    @patch('app.calculator_service.requests.get')
    def test_fetch_addition_from_web(self, mock_get):
        """
        Run this test suite to ensure your function handles the web request as
        expected. This mock prevents network calls during testing,
        which speeds up your tests and removes dependencies on external services.
        """
        # Configure the mock to simulate a successful HTTP response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'result': 15}

        # Test fetch_calculation_from_web function
        result = fetch_calculation_from_web(10, 5, 'add')
        self.assertEqual(result, 15)

        # Ensure URL was correctly constructed and called
        mock_get.assert_called_with('https://www.calculator.net/add?x=10&y=5')

    @patch('app.calculator_service.requests.get')
    def test_fetch_addition_error_400(self, mock_get):
        mock_get.return_value.status_code = 400
        mock_get.return_value.raise_for_status.side_effect = \
            requests.exceptions.HTTPError("400 Client Error: Bad Request for url")
        mock_get.return_value.json.return_value = {'error': 'Bad request'}

        result = fetch_calculation_from_web(10, 5, 'add')
        self.assertIsNone(result)

    @patch('app.calculator_service.requests.get')
    def test_fetch_addition_error_500(self, mock_get):
        mock_get.return_value.status_code = 500
        mock_get.return_value.raise_for_status.side_effect = \
            requests.exceptions.HTTPError("500 Server Error: Internal Server Error for url")
        mock_get.return_value.json.return_value = {'error': 'Internal Server Error'}

        result = fetch_calculation_from_web(10, 5, 'add')
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
