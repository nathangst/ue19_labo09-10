
import requests


def make_request():
    response = requests.get('https://www.punapi.com/api/random')
    return response.status_code


make_request()
