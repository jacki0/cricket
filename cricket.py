import requests
import random
import threading

class perpetualTimer():

      def __init__(self,t,hFunction):
         self.t=t
         self.hFunction = hFunction
         self.thread = threading.Timer(self.t,self.handle_function)

      def handle_function(self):
         self.hFunction()
         self.thread = threading.Timer(self.t,self.handle_function)
         self.thread.start()

      def start(self):
         self.thread.start()

      def cancel(self):
         self.thread.cancel()


def get_request():
    """ Sends a GET request to a random URL from the list.

    """
    try:
        get = requests.get(url_extraction())
    except:
        get = 'Traceback'

    return str(get)


def url_extraction():
    """ Chooses a random URL from the list.

    """
    url_list = []
    with open('list.txt') as file:
        url_list = [row.strip() for row in file]

    return random.choice(['http://', 'https://']) + random.choice(url_list)


t = perpetualTimer(5, get_request)
t.start()
