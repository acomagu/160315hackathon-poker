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
            # maxnum = numberco[card[0]]
        else:
            numberco[card[0]] = 1

    for card in arr:
        if card[1] in attshare:
            attshare[card[1]] += 1
        else:
            attshare[card[1]] = 1

    for k,v in numberco.items():
        if v == 1:
            countcal += 0
        elif v == 2:
            countcal += 50
        elif v == 3:
            countcal += 300
        elif v == 4:
            countcal += 10000

    for k,v in attshare.items():
        if v == 5:
            countcal += 2000
        elif v == 4:
            countcal += 200
        elif v == 3:
            countcal += 50
        elif v == 2:
            countcal += 0
        elif v== 1:
            countcal += 0

    return countcal
