import requests


def fetch_calculation_from_web(x, y, operation):
    """Fetches the calculation result from an external web service."""
    url = f"https://www.calculator.net/{operation}?x={x}&y={y}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()['result']
    except requests.exceptions.HTTPError as e:
        # Log error, return None, or handle it in another appropriate way
        print(f"HTTP error occurred: {e}")  # Simple error logging
        return None
    except Exception as e:
        # General error handling, such as logging or cleaning up resources
        print(f"An error occurred: {e}")
        return None

