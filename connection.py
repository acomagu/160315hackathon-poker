import requests

url = 'https://enova-no-limit-code-em.herokuapp.com/sandbox/players/1ad1982-c2c0-491f-87c1-5c330bdc92a7'

def get_field():
    return requests.get(url).json()

def act(params):
    return requests.post(url, params=params)
