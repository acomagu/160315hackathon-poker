import requests

# get_url = 'https://enova-no-limit-code-em.herokuapp.com/sandbox/players/deal-phase-key'
get_url = 'https://enova-no-limit-code-em.herokuapp.com/api/players/a1ad1982-c2c0-491f-87c1-5c330bdc92a7'
post_url = get_url + '/action'

def get_field():
    res = requests.get(get_url).json()
    print(res)
    return res
def act(params):
    print(params)
    return requests.post(post_url, params=params)
