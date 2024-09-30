import requests

URL = 'https://api.api-ninjas.com/v1/animals?name='
API_KEY = 'UkkpAvnGuZ8I1p6h4hTfkA==b9sZdFDa2MqJyuyC'


def fetch_animal_data(name):
    new_url = f'{URL}{name}'
    res = requests.get(new_url, headers={'X-Api-Key': API_KEY}).json()
    return res


def is_animal_exist(data):
    """
    Check if the animal data returned is not empty.
    Returns True if exists, otherwise False.
    """
    return bool(data)