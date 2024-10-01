import requests
import os
from dotenv import load_dotenv

URL = 'https://api.api-ninjas.com/v1/animals?name='


def fetch_animal_data(name):
    new_url = f'{URL}{name}'
    load_dotenv()  # This line will lod the  variables from the .env file
    api_key = os.getenv("API_KEY")  # This will access the API key
    res = requests.get(new_url, headers={'X-Api-Key': api_key}).json()
    return res


def is_animal_exist(data):
    """
    Check if the animal data returned is not empty.
    Returns True if exists, otherwise False.
    """
    return bool(data)
