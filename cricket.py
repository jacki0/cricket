import requests
import random
import threading


class PerpetualTimer():
    def __init__(self, t, hfunction):
        self.hFunction = hfunction
        self.t=t
        self.thread = threading.Timer(self.t, self.handle_function)
        self.hFunction = hfunction

    def handle_function(self):
        self.hFunction()
        self.thread = threading.Timer(self.t, self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()


def get_request(get=None):
    """ Sends a GET request to a random URL from the list.

    """
    try:
        get = requests.get(url_extraction())
    finally:
        return get


def url_extraction(url_list=[]):
    """ Chooses a random URL from the list.

    """
    with open('list.txt') as file:
        url_list = [row.strip() for row in file]
    return random.choice(['http://', 'https://']) + random.choice(url_list)


t = PerpetualTimer(9, get_request)
t.start()
