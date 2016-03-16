import requests

get_url = 'https://enova-no-limit-code-em.herokuapp.com/sandbox/players/deal-phase-key'
post_url = get_url + '/action'

def get_field():
    return requests.get(url).json()

def act(params):
    return requests.post(post_url, params=params)
