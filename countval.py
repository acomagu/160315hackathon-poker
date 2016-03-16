import requests
import re

def calculate(arr):
    attshare = {} 
    numberco = {}
    countcal = 0

    maxnum = 0
    for card in arr:
        if card[0] in numberco:
            numberco[card[0]] += 1
            maxnum = numberco[card[0]]
        else:
            numberco[card[0]] = 1

    for card in arr:
        if card[1] in attshare:
            attshare[card[1]] += 1
        else:
            attshare[card[1]] = 1

    if maxnum == 4:
        countcal += 1000
    elif maxnum ==3:
        countcal += 100
    elif maxnum == 2:
        countcal += 50

    return countcal

def request():
    return requests.get('https://enova-no-limit-code-em.herokuapp.com/sandbox/players/deal-phase-key').json()

print(request())
