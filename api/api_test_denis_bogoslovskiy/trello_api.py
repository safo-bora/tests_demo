import requests

# Trello API key and token
API_KEY = '622d9357a1ca45a03441214f1f718150'
TOKEN = 'ATTAf60046fda242a5da6083b6bdbeb489f07c0bae525870ac7521566c4e5e66c4863E721EA6'

BASE_URL = 'https://api.trello.com/1'


def get_action_details(action_id):
    url = f'{BASE_URL}/actions/{action_id}'
    query = {
        'key': API_KEY,
        'token': TOKEN
    }
    response = requests.get(url, params=query)

    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            print('Response content is not valid JSON')
            return None
    else:
        print(f'Error: Received status code {response.status_code}')
        print(f'Response content: {response.content}')
        return None


def update_action(action_id, text):
    url = f'{BASE_URL}/actions/{action_id}'
    query = {
        'text': text,
        'key': API_KEY,
        'token': TOKEN
    }
    response = requests.put(url, params=query)

    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            print('Response content is not valid JSON')
            return None
    else:
        print(f'Error: Received status code {response.status_code}')
        print(f'Response content: {response.content}')
        return None


def delete_action(action_id):
    url = f'{BASE_URL}/actions/{action_id}'
    query = {
        'key': API_KEY,
        'token': TOKEN
    }
    response = requests.delete(url, params=query)

    if response.status_code == 200:
        return True
    else:
        print(f'Error: Received status code {response.status_code}')
        print(f'Response content: {response.content}')
        return False

