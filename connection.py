import requests

# get_url = 'https://enova-no-limit-code-em.herokuapp.com/sandbox/players/deal-phase-key'
api_key = 'cf0187c2-9181-4204-9a6e-e38ce6d81845'
get_url = 'https://enova-no-limit-code-em.herokuapp.com/api/players/' + api_key
post_url = get_url + '/action'

def get_field():
    res = requests.get(get_url).json()
    print(res)
    return res

def act(params):
    print(params)
    return requests.post(post_url, params=params)
