import requests
import random
import threading
import json
from datetime import datetime


class PerpetualTimer():
    def __init__(self, t, hfunction):
        self.hFunction = hfunction
        self.t = t
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


def request():
    """ Sends a GET or POST request to a random URL from the list.
        Logs date, time, URL, request type, reply and optionally exception.

    """
    use_url = url_extraction()
    request_type = random.choice(['GET', 'POST'])
    try:
        log = [str(datetime.today()), use_url]
        log[0] = log[0][:log[0].find('.')]
        log.append(request_type)
        if request_type == 'POST':
            log.append(str(requests.post(use_url, timeout=req_timeout))[1:-1])
        else:
            log.append(str(requests.get(use_url, timeout=req_timeout))[1:-1])
    except Exception as ex:
        log.append(str(ex))
    json.dump(log, open('log.json', 'a'), indent=0)


def url_extraction():
    """ Chooses a random URL from the list.
    """
    return random.choice(['http://', 'https://']) + random.choice(urls)


with open('config.json') as file:
    conf = json.load(file)
    min_interval = conf['min_interval']
    max_interval = conf['max_interval']
    req_timeout = conf['timeout']
    urls = conf['urls']


t = PerpetualTimer(random.randint(min_interval, max_interval), request)
t.start()
