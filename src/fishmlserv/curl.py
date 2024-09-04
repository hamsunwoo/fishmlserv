import requests

def get(l, w, url="http://localhost:8765/fish"):
    headers = {
        'accept': 'application/json',
    }

    params = {
        'l': l,
        'w': w,
    }

    response = requests.get(url, params=params, headers=headers)
    j = response.json()
    r = j.get("prediction")

    return r
