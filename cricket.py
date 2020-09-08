import requests
import random


def get_request(extract_url):
    """ Sends a GET request to a random URL from the list.
    
    """
    get = requests.get(extract_url)

    return get


def url_extraction():
    """ Chooses a random URL from the list.

    """
    url_list = []
    with open('list.txt') as file:
        url_list = [row.strip() for row in file]

    return random.choice(['http://', 'https://']) + random.choice(url_list)
