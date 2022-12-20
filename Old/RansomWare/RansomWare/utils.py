import requests

def send(message):
    requests.post(url="WEBHOOK", data={"content":message})

def better_round(number, decimals):
    multiplier = 10 ** decimals
    return int(number * multiplier) / multiplier
